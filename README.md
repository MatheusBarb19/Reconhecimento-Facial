# 🎭 Visão Computacional e Inteligência Artificial com Python

Repositório dedicado ao desenvolvimento de aplicações práticas utilizando **Python, Visão Computacional e Inteligência Artificial**.

O objetivo é explorar técnicas de detecção facial, processamento de imagens, análise de expressões faciais e monitoramento de sinais visuais associados à sonolência.

Atualmente, o repositório reúne quatro aplicações independentes, desenvolvidas como parte dos meus estudos e evolução na área de tecnologia.

## 📋 Projetos

### 👤 1. Detecção e Contagem de Rostos em Tempo Real

Aplicação desenvolvida com **OpenCV e MediaPipe** para detectar rostos através da webcam e contabilizar as detecções realizadas em cada quadro.

**Funcionalidades:**
- Captura de vídeo em tempo real.
- Detecção facial.
- Contagem de rostos identificados.
- Exibição das detecções na imagem.

**Tecnologias:** Python, OpenCV e MediaPipe.

**Arquivo:** `detecção_de_Rosto.py`

### 😊 2. Análise Facial em Imagens

Aplicação que utiliza a biblioteca **DeepFace** para analisar imagens estáticas e retornar estimativas relacionadas ao rosto identificado.

**Informações analisadas:**
- Estimativa de idade.
- Classificação da emoção predominante.

**Exemplo de saída:**

```text
Idade estimada: 23
Emoção predominante: happy
```

**Tecnologias:** Python, OpenCV e DeepFace.

**Arquivo:** `Reconhecimento_rosto.py`

### 📹 3. Reconhecimento de Emoções em Tempo Real

Aplicação que utiliza a webcam para capturar imagens continuamente e analisar expressões faciais com o DeepFace.

**Classificações possíveis:**
- Happy 😄
- Sad 😢
- Angry 😠
- Surprise 😲
- Fear 😨
- Disgust 🤢
- Neutral 😐

A aplicação também realiza estimativas de idade e apresenta os resultados durante a captura de vídeo.

**Tecnologias:** Python, OpenCV e DeepFace.

**Arquivo:** `Reconhecimento_emoções.py`

### 👁️ 4. VigilantEye — Real-Time Driver Drowsiness Monitoring System

Projeto experimental desenvolvido com o objetivo de explorar técnicas de Visão Computacional e Inteligência Artificial para identificar sinais visuais associados à sonolência de condutores.

A aplicação utiliza o **MediaPipe Face Landmarker** para detectar pontos de referência faciais em tempo real através da webcam.

**Etapa atualmente implementada:**
- Captura de vídeo em tempo real.
- Detecção facial.
- Identificação e visualização de pontos de referência (*facial landmarks*).

**Próximas etapas planejadas:**
- Análise da abertura e do fechamento dos olhos.
- Identificação de padrões associados a piscadas prolongadas.
- Análise da abertura da boca para investigar possíveis bocejos.
- Combinação de indicadores visuais.
- Desenvolvimento de alertas.

**Tecnologias:** Python, OpenCV, MediaPipe e NumPy.

**Arquivo principal:** `Vigilante-Eye.py`

**Modelo utilizado:** `face_landmarker.task`

> **Observação:** VigilantEye é um protótipo experimental e educacional. Não é um equipamento certificado de segurança e não deve ser utilizado como substituto de sistemas de monitoramento validados ou da atenção do condutor.

## 🛠️ Tecnologias e Bibliotecas

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem de programação |
| OpenCV | Captura e processamento de imagens |
| MediaPipe | Detecção facial e pontos de referência |
| DeepFace | Análise facial e classificação de emoções |
| TensorFlow | Suporte a modelos de inteligência artificial |
| NumPy | Operações e processamento numérico |

## ⚙️ Instalação e Configuração

### Pré-requisitos

- Python 3.11.
- Git instalado.
- Webcam para executar as aplicações em tempo real.

### 1. Clone o repositório

```bash
git clone https://github.com/MatheusBarb19/Reconhecimento-Facial.git
```

### 2. Acesse a pasta

```bash
cd Reconhecimento-Facial
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

Confira se o arquivo `requirements.txt` contém as dependências necessárias para todos os projetos, incluindo MediaPipe e NumPy para o VigilantEye.

## ▶️ Como executar os projetos

Execute os comandos a partir da pasta principal do repositório.

**Detecção e contagem de rostos:**

```bash
python detecção_de_Rosto.py
```

**Análise facial em imagens:**

```bash
python Reconhecimento_rosto.py
```

**Reconhecimento de emoções em tempo real:**

```bash
python Reconhecimento_emoções.py
```

**VigilantEye:**

```bash
python "Vigilante Eye/Vigilante-Eye.py"
```

## 📂 Estrutura do Repositório

```text
Reconhecimento-Facial/
│
├── detecção_de_Rosto.py
├── Reconhecimento_rosto.py
├── Reconhecimento_emoções.py
│
├── teste.jpg
├── requirements.txt
├── Pipfile
├── README.md
│
└── Vigilante Eye/
    │
    ├── Vigilante-Eye.py
    ├── descrição.txt
    │
    └── models/
        └── face_landmarker.task
```

## 🎯 Objetivos de Aprendizado

Este repositório representa minha evolução prática no desenvolvimento de aplicações utilizando:

- Programação com Python.
- Visão Computacional.
- Processamento de imagens e vídeos.
- Detecção e análise facial.
- Inteligência Artificial.
- Utilização de bibliotecas e modelos de IA.
- Desenvolvimento de aplicações em tempo real.
- Gerenciamento de projetos com Git e GitHub.

## ⚠️ Observações e Limitações

- A idade apresentada pelas aplicações é uma estimativa gerada pelo modelo.
- As classificações de emoções são inferências computacionais baseadas em expressões faciais e não representam necessariamente o estado emocional real de uma pessoa.
- A precisão dos resultados pode variar conforme iluminação, qualidade da imagem, posição do rosto e características dos modelos utilizados.
- O VigilantEye ainda está em desenvolvimento e suas funcionalidades de identificação de sonolência são experimentais.
- Os projetos possuem finalidade educacional e de estudo, não sendo destinados a diagnósticos ou avaliações psicológicas.

## 👨‍💻 Autor

**Matheus Barbosa**

Desenvolvedor em constante aprendizado, explorando Python, Inteligência Artificial e Visão Computacional.

- GitHub: [MatheusBarb19](https://github.com/MatheusBarb19)
- Repositório: [Reconhecimento-Facial](https://github.com/MatheusBarb19/Reconhecimento-Facial)

---

⭐ Se este repositório despertou seu interesse, fique à vontade para explorar os projetos e acompanhar minha evolução!