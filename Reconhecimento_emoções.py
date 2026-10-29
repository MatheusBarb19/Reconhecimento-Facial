
# OBJETIVO: Estimar a idade e classificar a emoção predominante
# de um rosto utilizando a webcam, OpenCV e DeepFace.

import cv2  # Biblioteca para captura e processamento de imagens.
from deepface import DeepFace  # Biblioteca para análise facial.

# ============================================================
# 1. INICIALIZAÇÃO DA WEBCAM
# ============================================================

webcam = cv2.VideoCapture(0)  # Abre a webcam padrão do computador.

# Verifica se a webcam foi aberta corretamente.
if not webcam.isOpened():
    print("Erro: não foi possível acessar a webcam.")
    exit()

# ============================================================
# 2. CONFIGURAÇÃO DAS VARIÁVEIS
# ============================================================

contador_quadros = 0  # Conta quantos quadros foram capturados.
intervalo_analise = 10  # Executa a análise a cada 10 quadros.

emocao = "Aguardando rosto..."  # Texto inicial da emoção.
idade = None  # Armazena a idade estimada mais recente.

# ============================================================
# 3. CAPTURA E ANÁLISE EM TEMPO REAL
# ============================================================

try:
    while True:

        # Captura um quadro da webcam.
        sucesso, frame = webcam.read()

        # Encerra o programa caso a captura falhe.
        if not sucesso:
            print("Erro: não foi possível capturar a imagem.")
            break

        # Atualiza o contador de quadros capturados.
        contador_quadros += 1

        # Executa a análise somente no intervalo definido.
        if contador_quadros % intervalo_analise == 0:

            try:
                # Analisa o quadro para estimar a idade e classificar emoções.
                # enforce_detection=True exige que um rosto seja detectado.
                resultado = DeepFace.analyze(
                    img_path=frame,
                    actions=["age", "emotion"],
                    enforce_detection=True
                )

                # Verifica se a análise retornou algum resultado.
                if resultado:

                    # Obtém os dados do primeiro rosto encontrado.
                    rosto = resultado[0]

                    # Armazena a emoção predominante.
                    emocao = rosto["dominant_emotion"]

                    # Armazena a idade estimada pelo modelo.
                    idade = rosto["age"]

            except Exception as erro:
                # Informa que não foi possível realizar a análise.
                # A mensagem é atualizada na próxima tentativa.
                emocao = "Rosto nao detectado"
                idade = None

                # Exibe o erro no terminal para facilitar a depuração.
                print(f"Erro durante a análise: {erro}")

        # ====================================================
        # 4. EXIBIÇÃO DOS RESULTADOS NA TELA
        # ====================================================

        # Exibe a emoção predominante no quadro.
        cv2.putText(
            frame,
            f"Emocao: {emocao}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        # Exibe a idade estimada, caso exista um resultado.
        if idade is not None:
            texto_idade = f"Idade estimada: {idade} anos"

            cv2.putText(
                frame,
                texto_idade,
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        # Mostra a imagem com os resultados da análise.
        cv2.imshow("Analise Facial em Tempo Real", frame)

        # Encerra o programa quando a tecla ESC for pressionada.
        if cv2.waitKey(1) & 0xFF == 27:
            break

finally:
    # Libera a webcam mesmo se ocorrer algum erro.
    webcam.release()

    # Fecha todas as janelas abertas pelo OpenCV.
    cv2.destroyAllWindows()
