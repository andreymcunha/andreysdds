import streamlit as st

def calcular_saudade(nome):
    saudade_maxima = 10
    if nome.lower() == "tuany" or nome.lower() == "tuca":
        return saudade_maxima
    else:
        return 0

def main():
    st.title("Controle de Saudade do Andrey")
    nome = st.text_input("Digite o nome da pessoa que você sente saudade:")
    
    if nome:
        nivel_saudade = calcular_saudade(nome)
        if nivel_saudade > 0:
            st.success(f"O Andrey sente muita falta da {nome}! 💔")
            st.progress(nivel_saudade / 10)
            st.markdown("<div style='text-align: center; font-size: 34px;'>PRA CARALHO kekeke</div>", unsafe_allow_html=True)
        else:
            st.error("O Andrey não sente a sua falta. 😎")

if __name__ == "__main__":
    main()
