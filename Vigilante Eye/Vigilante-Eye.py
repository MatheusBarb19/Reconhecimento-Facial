"""
VigilantEye é um software de monitoramento de sinais comportamentais e visuais associados à sonolência,
fadiga e distração.
"""

# --------- Importação de Bibliotecas --------- #
import cv2
import mediapipe as mp
import time
from pathlib import Path


#---------- Localização do Modelo ------------ #
#obtem  o diretório onde está localizado o arquivo .py
diretorio_python = Path(__file__).resolve().parent

# Define o caminho para FaceLandMaker
caminho_modelo = diretorio_python / "models" / "face_landmarker.task"

# Verifica se o arquivo do modelo existe
if not caminho_modelo.exists():
    print(f"Erro: O arquivo do modelo não foi encontrado em {caminho_modelo}.")
    exit()

# ---------- Inicialização do MediaPipe --------- #

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



# --------- Inicialização da Webcam --------- #

# Abre a webcam padrão do computador.
webcam = cv2.VideoCapture(0)

# Verifica se a webcam foi aberta corretamente.
if not webcam.isOpened():
    print("Erro: não foi possível acessar a webcam.")
    exit()

print("Webcam inicializada com sucesso!")

# -------- Processamento de Quadros da Webcam --------- #

tempo_inicial = time.monotonic()  # Marca o tempo inicial para cálculo de FPS

try:
    with FaceLandmarker.create_from_options(opcoes) as detector: #Carrega o modelo

        while True:
            # Captura um quadro da webcam.
            sucesso, frame = webcam.read()

            if not sucesso:
                print("Erro: não foi possível capturar o quadro da webcam.")
                break

        imagem_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Converte o quadro para RGB

        imagem_mp = mp.Image(image_format=mp.ImageFormat.SRGB, data=imagem_rgb)  # Cria uma imagem compatível com MediaPipe