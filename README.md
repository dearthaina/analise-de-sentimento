# 📊 Análise de Sentimentos em Português

Uma aplicação web simples, elegante e extremamente direta para análise de sentimentos de textos em português. O projeto utiliza o framework **Streamlit** para a interface gráfica e o algoritmo **VADER (NLTK)** para processamento de linguagem natural (NLP).

Como o VADER é calibrado nativamente para o inglês, esta aplicação integra de forma transparente a biblioteca **deep-translator**, permitindo analisar textos em português com altíssima precisão de forma leve e rápida.

---

## 🚀 Funcionalidades

* 🇧🇷 **Suporte a Português:** Tradução automática em tempo real antes do processamento.
* 🤖 **Análise Inteligente:** Retorna se o texto é **Positivo**, **Negativo** ou **Neutro**.
* 📈 **Métrica Clara:** Exibe a pontuação exata (*Compound Score*) gerada pelo algoritmo.

---

## 📦 Pré-requisitos e Instalação

Certifique-se de ter o **Python 3.8 ou superior** instalado na sua máquina.

### 1. Clonar ou criar a pasta do projeto
Coloque os arquivos `app.py` e `requirements.txt` no mesmo diretório.

### 2. Instalar as dependências
Abra o seu terminal na pasta do projeto e execute o comando:

```bash
pip install -r requirements.txt
