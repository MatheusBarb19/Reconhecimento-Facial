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

