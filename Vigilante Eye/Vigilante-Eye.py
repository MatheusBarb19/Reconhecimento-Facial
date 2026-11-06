
"""
VigilantEye é um software de monitoramento de sinais comportamentais
e visuais associados à sonolência, fadiga e distração.

"""

# --------- Importação de Bibliotecas --------- #

import cv2
import mediapipe as mp
import time
import math
from pathlib import Path
import json
from datetime import datetime


# --------- Localização do Modelo --------- #

# Obtém o diretório onde está localizado este arquivo Python.
diretorio_python = Path(__file__).resolve().parent

# Define o caminho para o modelo Face Landmarker.
caminho_modelo = diretorio_python / "models" / "face_landmarker.task"

# Verifica se o arquivo do modelo existe.
if not caminho_modelo.exists():
    print(f"Erro: O arquivo do modelo não foi encontrado em {caminho_modelo}.")
    raise SystemExit

# --------- Histórico de Eventos --------- #

# Define o caminho do arquivo de histórico na pasta do projeto.
ARQUIVO_HISTORICO = diretorio_python / "historico_eventos.jsonl"


def formatar_data_hora(data_hora=None):
    """
    Formata a data e hora no padrão DD-MM-AAAA
    e inclui o fuso horário.
    """

    if data_hora is None:
        data_hora = datetime.now().astimezone()

    horario = data_hora.strftime("%d-%m-%YT%H:%M:%S%z")

    # Adiciona os dois pontos no fuso horário.
    return horario[:-2] + ":" + horario[-2:]


def registrar_evento(tipo_evento, **dados):
    """
    Registra um evento identificado pelo VigilantEye
    em formato JSONL.
    """

    evento = {
        "evento": tipo_evento,
        **dados
    }

    try:
        # Abre o arquivo em modo de acréscimo, preservando registros anteriores.
        with ARQUIVO_HISTORICO.open("a", encoding="utf-8") as arquivo:
            arquivo.write(
                json.dumps(evento, ensure_ascii=False) + "\n"
            )

    except OSError as erro:
        print(f"Erro ao registrar evento: {erro}")

# --------- Inicialização do MediaPipe --------- #

# Acessa as ferramentas de visão computacional do MediaPipe.
BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
RunningMode = mp.tasks.vision.RunningMode

# Configura o modelo para trabalhar com vídeos.
opcoes = FaceLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path=str(caminho_modelo)
    ),
    running_mode=RunningMode.VIDEO,
    num_faces=1
)


# --------- Pontos de Referência dos Olhos --------- #

# Índices dos pontos faciais utilizados para identificar os olhos.
PONTOS_OLHO_1 = [33, 160, 158, 133, 153, 144]
PONTOS_OLHO_2 = [362, 385, 387, 263, 373, 380]

# Agrupa os pontos dos dois olhos.
PONTOS_OLHOS = [PONTOS_OLHO_1, PONTOS_OLHO_2]


# --------- Cálculo do EAR (Eye Aspect Ratio) --------- #

def calcular_ear(rosto, indices, largura, altura):

    # Obtém as coordenadas dos seis pontos do olho.
    pontos = []

    for indice in indices:
        ponto = rosto[indice]

        x = ponto.x * largura
        y = ponto.y * altura

        pontos.append((x, y))

    # Calcula as distâncias verticais entre as pálpebras.
    distancia_vertical_1 = math.dist(pontos[1], pontos[5])
    distancia_vertical_2 = math.dist(pontos[2], pontos[4])

    # Calcula a distância horizontal do olho.
    distancia_horizontal = math.dist(pontos[0], pontos[3])

    # Evita divisão por zero.
    if distancia_horizontal == 0:
        return 0.0

    # Calcula o Eye Aspect Ratio.
    ear = (
        distancia_vertical_1 + distancia_vertical_2
    ) / (2 * distancia_horizontal)

    return ear


# --------- Cálculo do MAR (Mouth Aspect Ratio) --------- #

def calcular_mar(rosto, largura, altura):

    # Índices dos pontos utilizados para analisar a abertura da boca.
    PONTO_SUPERIOR = 13
    PONTO_INFERIOR = 14
    PONTO_ESQUERDO = 78
    PONTO_DIREITO = 308

    # Obtém as coordenadas dos pontos em pixels.
    ponto_superior = (
        int(rosto[PONTO_SUPERIOR].x * largura),
        int(rosto[PONTO_SUPERIOR].y * altura)
    )

    ponto_inferior = (
        int(rosto[PONTO_INFERIOR].x * largura),
        int(rosto[PONTO_INFERIOR].y * altura)
    )

    ponto_esquerdo = (
        int(rosto[PONTO_ESQUERDO].x * largura),
        int(rosto[PONTO_ESQUERDO].y * altura)
    )

    ponto_direito = (
        int(rosto[PONTO_DIREITO].x * largura),
        int(rosto[PONTO_DIREITO].y * altura)
    )

    # Calcula as distâncias vertical e horizontal da boca.
    distancia_vertical = math.dist(
        ponto_superior,
        ponto_inferior
    )

    distancia_horizontal = math.dist(
        ponto_esquerdo,
        ponto_direito
    )

    # Evita divisão por zero.
    if distancia_horizontal == 0:
        return 0.0

    # Calcula o Mouth Aspect Ratio.
    mar = distancia_vertical / distancia_horizontal

    return mar


# --------- Configurações de Monitoramento --------- #

# Limite inicial para identificar olhos fechados.
LIMIAR_EAR = 0.22

# Tempo mínimo para considerar um fechamento prolongado.
TEMPO_FECHAMENTO_PROLONGADO = 1.5

# Intervalo inicial para considerar uma piscada.
TEMPO_MINIMO_PISCADA = 0.05
TEMPO_MAXIMO_PISCADA = 0.50

# Variáveis de controle dos olhos.
olhos_fechados_desde = None
inicio_fechamento = None

piscadas = 0
status_olhos = "OLHOS ABERTOS"


# --------- Configurações de Detecção de Bocejos --------- #

# Limite inicial para identificar abertura significativa da boca.
LIMIAR_MAR = 0.60

# Tempo mínimo de abertura para considerar um possível bocejo.
TEMPO_MINIMO_BOCEJO = 1.0

# Variáveis de controle da boca.
boca_aberta_desde = None
inicio_bocejo = None
bocejos = 0
status_boca = "BOCA FECHADA"


# --------- Inicialização da Webcam --------- #

# Abre a webcam padrão do computador.
webcam = cv2.VideoCapture(0)

# Verifica se a webcam foi aberta corretamente.
if not webcam.isOpened():
    print("Erro: não foi possível acessar a webcam.")
    raise SystemExit

print("Webcam inicializada com sucesso!")


# --------- Processamento de Quadros da Webcam --------- #

# Registra o instante inicial para gerar os timestamps do MediaPipe.
tempo_inicial = time.monotonic()

try:

    with FaceLandmarker.create_from_options(opcoes) as detector:

        while True:

            # Captura um quadro da webcam.
            sucesso, frame = webcam.read()

            if not sucesso:
                print("Erro: não foi possível capturar o quadro da webcam.")
                break

            # Obtém as dimensões do quadro.
            altura, largura, _ = frame.shape

            # Converte o quadro de BGR para RGB.
            imagem_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Cria uma imagem compatível com o MediaPipe.
            imagem_mp = mp.Image(
                image_format=mp.ImageFormat.SRGB,
                data=imagem_rgb
            )

            # Calcula o tempo em milissegundos.
            timestamp_ms = int(
                (time.monotonic() - tempo_inicial) * 1000
            )

            # Realiza a detecção facial.
            resultado = detector.detect_for_video(
                imagem_mp,
                timestamp_ms
            )

            # Obtém o tempo atual para os cálculos de duração.
            tempo_atual = time.monotonic()

            # --------- Verificação de Detecção Facial --------- #

            if resultado.face_landmarks:

                # Percorre os rostos encontrados.
                for rosto in resultado.face_landmarks:

                    # --------- Detecção de Bocejos --------- #

                    # Calcula a abertura da boca.
                    mar = calcular_mar(rosto, largura, altura)

                    # Verifica se a abertura da boca ultrapassou o limite.
                    if mar > LIMIAR_MAR:

                        # Registra o instante em que a boca começou a abrir.
                        if boca_aberta_desde is None:
                            boca_aberta_desde = tempo_atual
                            inicio_bocejo = datetime.now().astimezone()

                        # Calcula há quanto tempo a boca permanece aberta.
                        tempo_boca_aberta = tempo_atual - boca_aberta_desde

                        # Verifica se a abertura é prolongada.
                        if tempo_boca_aberta >= TEMPO_MINIMO_BOCEJO:
                            status_boca = "POSSIVEL BOCEJO"
                        else:
                            status_boca = "BOCA ABERTA"

                    else:

                        # Verifica se houve uma abertura anterior.
                        if boca_aberta_desde is not None:

                            tempo_boca_aberta = tempo_atual - boca_aberta_desde

                            # Confirma e registra o possível bocejo.
                            if tempo_boca_aberta >= TEMPO_MINIMO_BOCEJO:

                                bocejos += 1

                                registrar_evento(
                                    "BOCEJO",
                                    inicio=formatar_data_hora(inicio_bocejo)
                                )

                            # Reinicia o controle.
                            boca_aberta_desde = None
                            inicio_bocejo = None

                        status_boca = "BOCA FECHADA"
                        
                        # Exibe o valor do MAR.
                        cv2.putText(
                            frame,
                            f"MAR: {mar:.2f}",
                            (30, 150),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (255, 255, 0),
                            2
                        )

                    # --------- Detecção de Piscadas --------- #

                    # Armazena o EAR calculado para cada olho.
                    valores_ear = []

                    # Percorre os dois conjuntos de pontos dos olhos.
                    for pontos_olho in PONTOS_OLHOS:

                        # Calcula o EAR do olho atual.
                        ear = calcular_ear(
                            rosto,
                            pontos_olho,
                            largura,
                            altura
                        )

                        valores_ear.append(ear)

                        # Desenha os pontos de referência do olho.
                        for indice in pontos_olho:

                            ponto = rosto[indice]

                            x_pixel = int(ponto.x * largura)
                            y_pixel = int(ponto.y * altura)

                            cv2.circle(
                                frame,
                                (x_pixel, y_pixel),
                                3,
                                (0, 255, 0),
                                -1
                            )

                    # Calcula a média do EAR dos dois olhos.
                    ear_medio = sum(valores_ear) / len(valores_ear)

                    # Verifica se os olhos estão fechados.
                    if ear_medio < LIMIAR_EAR:

                        # Registra o instante em que os olhos fecharam.
                        if olhos_fechados_desde is None:
                            olhos_fechados_desde = tempo_atual
                            inicio_fechamento = datetime.now().astimezone()

                        # Calcula o tempo de fechamento.
                        tempo_fechado = (
                            tempo_atual - olhos_fechados_desde
                        )

                        # Verifica se o fechamento é prolongado.
                        if tempo_fechado >= TEMPO_FECHAMENTO_PROLONGADO:
                            status_olhos = "FECHAMENTO PROLONGADO"
                        else:
                            status_olhos = "OLHOS FECHADOS"

                    else:

                        # Verifica se houve um fechamento anterior.
                        if olhos_fechados_desde is not None:

                            tempo_fechado = (
                                tempo_atual - olhos_fechados_desde
                            )
                            
                            # Verifica se o fechamento foi prolongado.
                            if tempo_fechado >= TEMPO_FECHAMENTO_PROLONGADO:

                                # Registra o horário em que os olhos foram abertos.
                                fim_fechamento = datetime.now().astimezone()

                                registrar_evento(
                                    "FECHAMENTO_OLHOS_PROLONGADO",
                                    inicio=formatar_data_hora(inicio_fechamento),
                                    fim=formatar_data_hora(fim_fechamento),
                                    duracao_segundos=round(tempo_fechado, 2)
                                )

                            # Conta somente fechamentos dentro do intervalo
                            # inicial definido para uma piscada.
                            if (
                                TEMPO_MINIMO_PISCADA
                                <= tempo_fechado
                                <= TEMPO_MAXIMO_PISCADA
                            ):
                                piscadas += 1

                            # Reinicia o controle.
                            olhos_fechados_desde = None
                            inicio_fechamento = None

                        status_olhos = "OLHOS ABERTOS"

                    # --------- Exibição das Informações --------- #

                    # Exibe o valor do EAR.
                    cv2.putText(
                        frame,
                        f"EAR: {ear_medio:.3f}",
                        (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 255, 255),
                        2
                    )

                    # Exibe a quantidade de piscadas.
                    cv2.putText(
                        frame,
                        f"Piscadas: {piscadas}",
                        (30, 85),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (255, 255, 255),
                        2
                    )

                    # Exibe o status dos olhos.
                    cv2.putText(
                        frame,
                        status_olhos,
                        (30, 120),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 0, 255)
                        if status_olhos == "FECHAMENTO PROLONGADO"
                        else (0, 255, 0),
                        2
                    )

                    # Exibe o status da boca.
                    cv2.putText(
                        frame,
                        status_boca,
                        (30, 180),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 0, 255)
                        if status_boca == "POSSIVEL BOCEJO"
                        else (0, 255, 0),
                        2
                    )

                    # Exibe a quantidade de possíveis bocejos.
                    cv2.putText(
                        frame,
                        f"Bocejos: {bocejos}",
                        (30, 210),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (255, 255, 255),
                        2
                    )

            else:

                # Se o rosto desaparecer, reinicia os controles de duração.
                # Isso evita que um período sem detecção seja contabilizado.
                olhos_fechados_desde = None
                boca_aberta_desde = None

                status_olhos = "ROSTO NAO DETECTADO"
                status_boca = "ROSTO NAO DETECTADO"

                # Exibe o aviso de ausência de detecção facial.
                cv2.putText(
                    frame,
                    "ROSTO NAO DETECTADO",
                    (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 255),
                    2
                )

                # Mantém os contadores visíveis.
                cv2.putText(
                    frame,
                    f"Piscadas: {piscadas}",
                    (30, 85),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 255, 255),
                    2
                )

                cv2.putText(
                    frame,
                    f"Bocejos: {bocejos}",
                    (30, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 255, 255),
                    2
                )

            # --------- Exibição do Resultado --------- #

            cv2.imshow(
                "VigilantEye - Monitoramento Facial",
                frame
            )

            # Encerra quando a tecla ESC for pressionada.
            if cv2.waitKey(1) == 27:
                break

finally:

    # Libera a webcam e fecha todas as janelas abertas.
    webcam.release()
    cv2.destroyAllWindows()

    print("Monitoramento encerrado.")
