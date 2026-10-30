# 🎭 Reconhecimento Facial e Análise de Emoções com Python

Projeto desenvolvido em **Python** com foco no estudo de **Visão Computacional e Inteligência Artificial**, utilizando OpenCV, MediaPipe e DeepFace.

O objetivo é explorar técnicas de detecção facial, processamento de imagens, estimativa de idade e classificação de emoções, tanto em imagens estáticas quanto em tempo real através da webcam.

## 📋 Funcionalidades

O projeto é composto por três aplicações independentes:

### 👤 1. Detecção Facial em Tempo Real

Utiliza a biblioteca **MediaPipe** em conjunto com **OpenCV** para detectar rostos através da webcam.

**Principais recursos:**
- Captura de vídeo em tempo real.
- Detecção de rostos.
- Contagem de rostos identificados na imagem.
- Exibição das detecções na tela.

**Tecnologias:**
- Python
- OpenCV
- MediaPipe

### 😊 2. Análise Facial em Imagens

Utiliza a biblioteca **DeepFace** para analisar uma imagem e retornar informações estimadas sobre as características faciais.

**Informações analisadas:**
- Estimativa de idade.
- Classificação da emoção predominante.

**Exemplo de saída:**

```text
Idade estimada: 23
Emoção predominante: happy
```

**Tecnologias:**
- Python
- OpenCV
- DeepFace

### 📹 3. Análise de Emoções em Tempo Real

Realiza a captura de imagens através da webcam e utiliza o DeepFace para classificar a expressão facial predominante.

**Classificações possíveis:**
- Happy 😄
- Sad 😢
- Angry 😠
- Surprise 😲
- Fear 😨
- Disgust 🤢
- Neutral 😐

**Tecnologias:**
- Python
- OpenCV
- DeepFace
- Webcam

## 🛠️ Tecnologias e Bibliotecas

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem de programação |
| OpenCV | Captura e processamento de imagens |
| MediaPipe | Detecção facial |
| DeepFace | Análise facial e classificação de emoções |
| TensorFlow | Suporte a modelos de inteligência artificial |

## ⚙️ Instalação e Configuração

### Pré-requisitos

- Python instalado.
- Git instalado.
- Webcam para executar as aplicações em tempo real.

### 1. Clone o repositório

```bash
git clone https://github.com/MatheusBarb19/Reconhecimento-Facial.git
```

### 2. Acesse a pasta do projeto

```bash
cd Reconhecimento-Facial
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute uma das aplicações

**Detecção facial:**

```bash
python Reconhecimento.py
```

**Análise facial em imagem:**

```bash
python Reconhecimento_rosto.py
```

**Análise de emoções em tempo real:**

```bash
python Reconhecimento_emocoes.py
```

## 📂 Estrutura do Projeto

```text
Reconhecimento-Facial/
│
├── Reconhecimento.py
├── Reconhecimento_rosto.py
├── Reconhecimento_emocoes.py
├── requirements.txt
├── Pipfile
└── README.md
```

## 🎯 Objetivos de Aprendizado

Este projeto foi desenvolvido para colocar em prática conhecimentos relacionados a:

- Programação com Python.
- Visão Computacional.
- Processamento de Imagens.
- Detecção Facial.
- Inteligência Artificial.
- Utilização de bibliotecas e modelos de IA.
- Gerenciamento de projetos com Git e GitHub.

## ⚠️ Observações e Limitações

- A idade apresentada pelo sistema é uma estimativa gerada pelo modelo.
- As emoções são classificações computacionais baseadas em expressões faciais e não representam necessariamente o estado emocional real de uma pessoa.
- A precisão dos resultados pode variar conforme iluminação, qualidade da imagem, posição do rosto e características do modelo utilizado.
- Este projeto possui finalidade educacional e experimental, não sendo destinado a diagnósticos ou avaliações psicológicas.

## 👨‍💻 Autor

**Matheus Barbosa**

Desenvolvedor em constante aprendizado, explorando Python, Inteligência Artificial e Visão Computacional.

- GitHub: [MatheusBarb19](https://github.com/MatheusBarb19)
- Repositório: [Reconhecimento Facial](https://github.com/MatheusBarb19/Reconhecimento-Facial)

---

⭐ Se este projeto despertou seu interesse, fique à vontade para explorar o código e acompanhar minha evolução!
