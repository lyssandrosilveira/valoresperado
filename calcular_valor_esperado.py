import streamlit as st

def calcular_odd_esperada(chance, odd_casa_apostas):
    if chance <= 0:
        return "A chance deve ser maior que zero."
    else:
        odd_esperada = 1 / (chance / 100)
        if odd_esperada < odd_casa_apostas:
            return f"Odd esperada: <span style='color:green'>{round(odd_esperada, 2)}</span>. Pode apostar, Odd EV+."
        elif odd_esperada >= odd_casa_apostas:
            return f"Odd esperada: <span style='color:red'>{round(odd_esperada, 2)}</span>. Não aposte, Odd EV-."

def main():
    st.title("Cálculo da Odd Esperada")
    chance = st.number_input("Informe a probabilidade de vitória:", min_value=0.01, max_value=100.0, value=50.0, step=0.01)
    odd_casa_apostas = st.number_input("Informe a Odd na casa de apostas:", min_value=0.01, value=2.0, step=0.01)
    odd_esperada = calcular_odd_esperada(chance, odd_casa_apostas)

    st.markdown(odd_esperada, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

