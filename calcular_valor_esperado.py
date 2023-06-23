import streamlit as st

def calcular_odd_esperada(chance):
    if chance <= 0:
        return "A chance deve ser maior que zero."
    else:
        odd_esperada = 1 / (chance / 100)
        return f"Odd esperada: {round(odd_esperada, 2)}"

def main():
    st.title("Cálculo da Odd Esperada")
    chance = st.number_input("Informe a chance:", min_value=0.01, max_value=100.0, value=50.0, step=0.01)
    odd_esperada = calcular_odd_esperada(chance)

    st.write(odd_esperada)

if __name__ == "__main__":
    main()
