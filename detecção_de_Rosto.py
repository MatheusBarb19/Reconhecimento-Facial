
# OBJETIVO: Detectar rostos em tempo real utilizando OpenCV e MediaPipe.

import cv2  # Biblioteca utilizada para capturar e processar imagens.
import mediapipe as mp  # Biblioteca utilizada para detectar rostos.

# ============================================================
# 1. INICIALIZAÇÃO DA WEBCAM
# ============================================================

webcam = cv2.VideoCapture(0)  # Abre a webcam padrão do computador.

# Verifica se a webcam foi aberta corretamente.
if not webcam.isOpened():
    print("Erro: não foi possível acessar a webcam.")
    exit()

# ============================================================
# 2. CONFIGURAÇÃO DA DETECÇÃO FACIAL
# ============================================================

reconhecer_rosto = mp.solutions.face_detection  # Acessa a solução de detecção facial do MediaPipe.

# Cria o detector facial.
# model_selection=0: modelo indicado para rostos próximos à câmera.
# min_detection_confidence=0.6: confiança mínima de 60% para aceitar uma detecção.
reconhecedor_rosto = reconhecer_rosto.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.6
)

# Ferramenta utilizada para desenhar as detecções na imagem.
desenho_facial = mp.solutions.drawing_utils

# ============================================================
# 3. CAPTURA E PROCESSAMENTO DOS QUADROS
# ============================================================

try:
    while True:

        # Captura um quadro da webcam.
        verificador, frame = webcam.read()

        # Encerra o programa se a imagem não for capturada corretamente.
        if not verificador:
            print("Erro: não foi possível capturar a imagem.")
            break

        # Converte a imagem de BGR para RGB.
        # O OpenCV utiliza BGR por padrão, enquanto o MediaPipe espera RGB.
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Envia a imagem convertida para o detector facial.
        lista_facial = reconhecedor_rosto.process(frame_rgb)

        quantidade_rostos = (
            len(lista_facial.detections)
            if lista_facial.detections
            else 0
        )   
        
        # Verifica se algum rosto foi detectado.
        if lista_facial.detections:

            # Percorre todos os rostos encontrados no quadro.
            for rosto in lista_facial.detections:

                # Desenha a caixa delimitadora e os indicadores da detecção.
                desenho_facial.draw_detection(frame, rosto)

#================================
# Exibição da Contagem na Tela
#================================

        #define o texto qe será exibido na tela
        texto = f"Rostos detectados: {quantidade_rostos}"

        # Escreve a quantidade de rostos no canto superior esquerdo.
        cv2.putText(
            frame,  # Imagem em que o texto será desenhado.
            texto,  # Texto que será exibido.
            (20, 40),  # Posição do texto: X=20, Y=40.
            cv2.FONT_HERSHEY_SIMPLEX,  # Fonte utilizada.
            0.8,  # Tamanho do texto.
            (0, 255, 0),  # Cor verde em formato BGR.
            2  # Espessura das letras.
        )

        # Exibe a imagem com as detecções e a contagem.
        cv2.imshow("Deteccao e Contagem de Rostos", frame)

        # Aguarda 5 milissegundos e verifica se a tecla ESC foi pressionada.
        if cv2.waitKey(5) & 0xFF == 27:
            break

finally:
    # Libera a webcam mesmo se ocorrer algum erro durante a execução.
    webcam.release()

    # Fecha todas as janelas abertas pelo OpenCV.
    cv2.destroyAllWindows()

    # Encerra o detector e libera seus recursos.
    reconhecedor_rosto.close()
