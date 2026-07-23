# titulo
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

# streamlit - frontend e backend

import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

st.set_page_config(page_title="ChatBot com IA")

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY") or os.getenv("API_KEY")
if not api_key:
    st.error(
        "Chave da OpenAI não configurada. "
        "Crie um arquivo .env baseado no .env.example."
    )
    st.stop()

modelo = OpenAI(api_key=api_key) # criar uma instancia do modelo de IA

#st.write("# ChatBot com IA") # markdown
st.markdown("<h1 style='text-align: center;'>ChatBot com IA</h1>", unsafe_allow_html=True) # html para centralizar o titulo

# session_state = memoria do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# adicionar uma mensagem
# st.session_state["lista_mensagens"].append(mensagem)

# exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # user -> ser humano
    # assistant -> inteligencia artificial
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # resposta da IA
    try:
        with st.spinner("Gerando resposta..."):
            resposta_modelo = modelo.chat.completions.create(
                messages=st.session_state["lista_mensagens"],
                model="gpt-4o"
            )
    except OpenAIError:
        st.session_state["lista_mensagens"].pop()
        st.error(
            "Não foi possível obter uma resposta da OpenAI. "
            "Confira sua chave, conexão e limites da conta."
        )
        st.stop()
    
    resposta_ia = resposta_modelo.choices[0].message.content

    # exibir a resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)

# rodar o chatbot: streamlit run main.py
