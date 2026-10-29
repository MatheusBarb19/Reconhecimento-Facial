# OBJETIVO: Estimar a idade e classificar a emoção predominante
# de cada rosto encontrado em uma imagem utilizando o DeepFace.

import cv2  # Biblioteca utilizada para carregar imagens.
from deepface import DeepFace  # Biblioteca para análise de atributos faciais.

#=============================
# 1. CARREGAMENTO DA IMAGEM
#=============================

imagem = cv2.imread("teste.jpg") #Carrega a imagem para reconhecimento facial

# Verificar se foi carregado
if imagem is None:
    print("Erro: não foi possível carregar a imagem.")

else:
    try:
        #=============================
        # 2. ANÁLISE DA FACIAL
        #=============================

        #Analisa a imagem para reconhecer a idade e emoção da pessoa
        resultado = DeepFace.analyze(imagem, actions=['age', 'emotion'], enforce_detection=True) 

        #=============================
        # 3. EXIBIR RESULTADOS
        #=============================

        for indice, rosto in enumerate(resultado, start=1):
            idade = rosto["age"]  # Obtém a idade estimada do rosto.
            emocao = rosto["dominant_emotion"]  # Obtém a emoção predominante do rosto.
            emocoes = rosto["emotion"]  # Obtém todas as emoções detectadas no rosto.

            #Exibe os resultados de cada rosto encontrado na imagem
            print(f"\n ====== Rosto {indice}===============")
            print(f"Idade estimada: {idade} anos")
            print(f"Emoção predominante: {emocao}")

            #exibe as pontuações de cada emoção detectada no rosto
            print("Pontuações de emoções:")

            for emocao, pontuacao in emocoes.items():
                print(f"{emocao}: {pontuacao:.2f}")

    except Exception as erro:  
        print(f"Erro ao analisar a imagem: {erro}")