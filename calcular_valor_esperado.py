import streamlit as st

def calcular_odd_esperada(chance, odd_casa_apostas):
    if chance <= 0:
        return "A chance deve ser maior que zero."
    else:
        odd_esperada = 1 / (chance / 100)
        if odd_esperada < odd_casa_apostas:
            return f"Odd esperada: {round(odd_esperada, 2)}. Pode apostar, Odd EV+."
        elif odd_esperada > odd_casa_apostas:
            return f"Odd esperada: {round(odd_esperada, 2)}. Não aposte, Odd EV-."
        else:
            return f"Odd esperada: {round(odd_esperada, 2)}. O valor da Odd na casa de apostas é igual à Odd Esperada."

def main():
    st.title("Cálculo da Odd Esperada")
    chance = st.number_input("Informe a chance:", min_value=0.01, max_value=100.0, value=50.0, step=0.01)
    odd_casa_apostas = st.number_input("Informe a Odd na casa de apostas:", min_value=0.01, value=2.0, step=0.01)
    odd_esperada = calcular_odd_esperada(chance, odd_casa_apostas)

    st.write(odd_esperada)

if __name__ == "__main__":
    main()

