import streamlit as st

st.set_page_config(
    page_title="Teste de hospedagem",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Minha aplicação Python na Web")

st.success("Hospedagem funcionando!")

st.write("Este é meu primeiro sistema publicado na internet.")

nome = st.text_input("Digite seu nome")

if st.button("Enviar"):
    st.write(f"Olá, {nome}!")

st.divider()

st.subheader("Teste de funcionamento")

st.metric("Status", "Online")
