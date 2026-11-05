"""Vigilante Eye é um software de monitoramento e vigilância de sinais comportamentais e visuais 
associados à sonolência, fadiga e distração. """

#--------- Importação de Bibliotecas ---------#
import cv2
import mediapipe as mp


#----- Inicialização da Webcam -----  #
webcam = cv2.VideoCapture(0) # bre a webcam padrão do computador.

if not webcam.isOpened(): #Se a webcam não for aberta exiir mensagem
    print("Erro: não foi possível acessar a webcam.")
    exit()

