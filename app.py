import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator

# Garante o download do dicionário de sentimentos VADER
nltk.download('vader_lexicon')

# Inicializa o analisador de sentimentos
sia = SentimentIntensityAnalyzer()

# Interface do usuário com Streamlit
st.title("Análise de Sentimentos em Português")
st.write("Digite um texto abaixo para descobrir se o sentimento é Positivo, Negativo ou Neutro.")

# Caixa de texto para o usuário digitar em português
texto_usuario = st.text_area("Seu texto:", placeholder="Ex: Eu adorei este produto, ele é maravilhoso!")

# Botão para iniciar a análise
if st.button("Analisar Sentimento"):
    if texto_usuario.strip() != "":
        
        # Como o VADER funciona em inglês, traduzimos o texto do português para o inglês
        texto_traduzido = GoogleTranslator(source='pt', target='en').translate(texto_usuario)
        
        # Faz a análise de sentimento no texto traduzido
        scores = sia.polarity_scores(texto_traduzido)
        score_compound = scores['compound']
        
        # Define a classificação com base na pontuação compound
        if score_compound >= 0.05:
            resultado = "Positivo"
            cor = "green"
        elif score_compound <= -0.05:
            resultado = "Negativo"
            cor = "red"
        else:
            resultado = "Neutro"
            cor = "gray"
            
        # Exibe os resultados na tela
        st.markdown(f"### Resultado: :{cor}[{resultado}]")
        st.write(f"**Pontuação Compound:** {score_compound}")
        st.caption(f"*Texto traduzido para análise:* {texto_traduzido}")
    else:
        st.warning("Por favor, digite algum texto antes de analisar.")