import streamlit as st
from app.analyzer import analisar_projeto_php
from app.generator import gerar_codigo_php
from app.improver import sugerir_melhorias_php

st.set_page_config(page_title="🤖 PHP AI Assistant")
st.title("🤖 Assistente PHP com IA (Starcoder)")

padroes = {}

# Analisar projeto
caminho = st.text_input("📁 Caminho do projeto PHP:")
if st.button("Analisar Padrões do Projeto"):
    padroes = analisar_projeto_php(caminho)
    st.subheader("✅ Padrões detectados:")
    st.json(padroes)

# Gerar novo código
descricao = st.text_input("📝 Descreva o que você quer gerar:")
if st.button("Gerar Código PHP"):
    if not padroes:
        st.warning("Analise o projeto primeiro para detectar padrões.")
    else:
        codigo = gerar_codigo_php(padroes, descricao)
        st.subheader("✨ Código gerado:")
        st.code(codigo, language='php')

# Sugestão de melhorias
arquivo = st.file_uploader("📄 Envie um arquivo PHP para revisar:")
if arquivo:
    conteudo = arquivo.read().decode()
    if st.button("Sugerir Melhorias"):
        sugestoes = sugerir_melhorias_php(conteudo)
        st.subheader("💡 Sugestões de melhoria:")
        st.markdown(sugestoes)
