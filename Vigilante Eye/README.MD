# 👁️ VigilantEye — Monitoramento de Sinais de Sonolência e Fadiga

O **VigilantEye** é um protótipo experimental desenvolvido em Python, utilizando Visão Computacional para identificar sinais visuais e comportamentais que podem estar associados à sonolência e à fadiga.

O projeto utiliza pontos de referência faciais (*Face Landmarks*) para analisar movimentos dos olhos e da boca em tempo real, identificando eventos como piscadas, fechamentos prolongados dos olhos e possíveis bocejos.

Além do monitoramento em tempo real, o sistema registra os eventos identificados e gera relatórios individuais ao final de cada sessão.

O projeto foi desenvolvido como parte dos meus estudos e da minha evolução na área de Visão Computacional.

## 🎯 Funcionalidades

- **Detecção facial em tempo real:** identificação de pontos de referência faciais utilizando MediaPipe.
- **Análise dos olhos (EAR):** cálculo do *Eye Aspect Ratio* para acompanhar a abertura e o fechamento dos olhos.
- **Contagem de piscadas:** identificação e contabilização de piscadas.
- **Fechamento prolongado dos olhos:** identificação de períodos em que os olhos permanecem fechados por tempo superior ao limite configurado.
- **Análise da boca (MAR):** cálculo do *Mouth Aspect Ratio* para acompanhar a abertura da boca.
- **Identificação de possíveis bocejos:** detecção baseada na abertura da boca e no tempo de duração.
- **Histórico de eventos:** armazenamento dos eventos identificados em arquivo JSONL.
- **Relatório por sessão:** geração de arquivos JSON com estatísticas e informações de cada execução.

## 🛠️ Tecnologias utilizadas

- **Python 3.11**
- **OpenCV:** captura e processamento de imagens da webcam.
- **MediaPipe:** detecção facial e identificação de pontos de referência.
- **JSON / JSONL:** armazenamento do histórico de eventos e relatórios das sessões.

## 📂 Estrutura do projeto

```text
Vigilante Eye/
│
├── Vigilante-Eye.py
├── historico_eventos.jsonl
│
├── models/
│   └── face_landmarker.task
│
└── relatorios_sessoes/
    └── relatorio_YYYYMMDD_HHMMSS.json
```

**Descrição dos arquivos e diretórios:**

- `Vigilante-Eye.py`: código principal da aplicação.
- `historico_eventos.jsonl`: histórico de eventos identificados durante as execuções.
- `models/`: diretório que armazena o modelo utilizado pelo MediaPipe.
- `relatorios_sessoes/`: diretório que armazena os relatórios individuais de cada sessão.

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/MatheusBarb19/Reconhecimento-Facial.git
```

### 2. Acesse a pasta do projeto

```bash
cd Reconhecimento-Facial/"Vigilante Eye"
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

No Windows:

```bash
source .venv/Scripts/activate
```

### 5. Instale as dependências

```bash
pip install opencv-python mediapipe
```

### 6. Configure o modelo

O projeto utiliza o modelo `face_landmarker.task`, que deve estar localizado dentro da pasta `models/`.

Certifique-se de que o arquivo esteja disponível antes de executar a aplicação.

## ▶️ Como executar

Com o ambiente virtual ativado e o modelo configurado, execute:

```bash
python Vigilante-Eye.py
```

A aplicação utilizará a webcam para realizar o monitoramento em tempo real.

Para encerrar a execução, pressione a tecla **ESC**.

Ao finalizar, o sistema exibirá o resumo da sessão e salvará o respectivo relatório.

## 📊 Armazenamento de dados

O VigilantEye utiliza dois formatos para armazenar informações:

### Histórico de eventos — JSONL

Cada evento é registrado individualmente, permitindo manter um histórico contínuo das ocorrências identificadas.

Exemplo:

```json
{"evento":"BOCEJO","inicio":"06-11-2026T15:01:00-03:00"}
{"evento":"FECHAMENTO_OLHOS_PROLONGADO","inicio":"06-11-2026T15:01:10-03:00","fim":"06-11-2026T15:01:12-03:00","duracao_segundos":2.0}
```

### Relatório da sessão — JSON

Ao encerrar o monitoramento, é gerado um relatório com informações como:

- Identificador da sessão;
- Horário de início e término;
- Duração total;
- Quantidade de piscadas;
- Quantidade de bocejos;
- Quantidade de fechamentos prolongados;
- Maior duração de fechamento dos olhos.

Os relatórios são armazenados individualmente na pasta `relatorios_sessoes/`.

## 🎥 Demonstração

<!-- Adicione aqui o vídeo ou GIF demonstrando o funcionamento do VigilantEye -->

## 📚 Aprendizados

O desenvolvimento deste projeto proporcionou a oportunidade de aprofundar conhecimentos em:

- Processamento de imagens e vídeos;
- Visão Computacional com OpenCV;
- Detecção facial e Face Landmarks com MediaPipe;
- Aplicação de cálculos matemáticos em imagens;
- Análise de características faciais;
- Manipulação e persistência de dados com JSON e JSONL;
- Organização de código e desenvolvimento de aplicações em Python.

## ⚠️ Observação importante

O VigilantEye é um protótipo experimental desenvolvido exclusivamente para fins educacionais e de estudo.

Os eventos identificados representam estimativas baseadas em características visuais e não constituem diagnósticos ou avaliações clínicas.

O projeto não é um sistema de segurança certificado ou validado para utilização durante a condução de veículos.

## 👨‍💻 Autor

**Matheus Barbosa**

Desenvolvedor de Software | Estudos em Python, Inteligência Artificial e Visão Computacional.

[GitHub](https://github.com/MatheusBarb19)