from class_EquacaoII import EquacaoII
import streamlit as st

class EquacaoIIUI:
    def main():
        st.header("Equação de II Grau: y = ax**2 + bx + c")
        a = (st.text_input("Informe o valor de A:"))
        b = (st.text_input("Informe o valor de B:"))
        c = (st.text_input("Informe o valor de C:"))
        if st.button("Calcular"):
            e = EquacaoII(float(a),float(b),float(c))
            st.write(f"Delta = {e.calc_Delta()}")
            x1, x2 = e.calc_Baskara()
            st.write(f"x1 = {x1:.2f}")
            st.write(f"x2 = {x2:.2f}")