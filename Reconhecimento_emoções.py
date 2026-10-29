import cv2
from deepface import DeepFace

# Inicia a webcam
webcam = cv2.VideoCapture(0)

while True:
    sucesso, frame = webcam.read()  # Lê a imagem da webcam

    if not sucesso:  # Verifica se a imagem foi lida corretamente
        break #Quebra o loop caso a imagem não tenha sido lida corretamente

    try:
        # Analisa a imagem para reconhecer a idade e emoção da pessoa
        resultado = DeepFace.analyze(frame, actions=['age', 'emotion'], enforce_detection=False)  

        #Obtém a emoção dominante
        emocao = resultado[0]["dominant_emotion"]

        #Exibe na tela a emoção dominante
        cv2.putText(frame, f"Emocao: {emocao}", (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)