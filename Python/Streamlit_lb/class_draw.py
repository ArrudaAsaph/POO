import streamlit as st

class Draw:
    def __init__(self,quantidade):
        self.quantidade = quantidade
        self.cont = 0
        self.space = " "
        

    def draw(self):
        if self.quantidade == 0:
            return 0
        else:
            
            st.write(" " * self.cont ,f"{"#    " * self.quantidade}")
            self.quantidade -= 1
            self.cont += 1
            self.space += self.space
            return self.draw()



class DrawUI:
    def main():
        st.header("Desenhe sua piramide inversa! ")
        a = (st.text_input("Informe a quantidade de bases que deseja:"))
        if st.button("Calcular"):
            d = Draw(int(a))

            d.draw()
            
