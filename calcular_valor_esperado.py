import streamlit as st

def calcular_valor_esperado(chance):
    if chance <= 0:
        return "A chance deve ser maior que zero."
    else:
        valor_esperado = 1 / (chance / 100)
        return f"O valor esperado é: {round(valor_esperado, 2)}"

def main():
    st.title("Valor Esperado")
    chance = st.number_input("Informe a chance:", min_value=0.01, max_value=100.0, value=50.0, step=0.01)
    valor_esperado = calcular_valor_esperado(chance)

    st.write(Odd_esperada)

if __name__ == "__main__":
    main()
