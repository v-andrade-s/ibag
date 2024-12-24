import streamlit as st
import random
import datetime

class Integrante:
    def __init__(self, nome, instrumento):
        self.nome = nome
        self.instrumento = instrumento

    def __str__(self):
        return f"{self.nome} ({self.instrumento})"

class GrupoDeLouvor:
    def __init__(self, nome_grupo):
        self.nome_grupo = nome_grupo
        self.integrantes = []  

    def adicionar_integrante(self, nome, instrumento):
        integrante = Integrante(nome, instrumento)
        self.integrantes.append(integrante)

    def gerar_escala(self):
        # Agrupar integrantes por instrumento
        instrumentos = {}
        for integrante in self.integrantes:
            if integrante.instrumento not in instrumentos:
                instrumentos[integrante.instrumento] = []
            instrumentos[integrante.instrumento].append(integrante)

        # Criar escala para cada instrumento
        data_inicial = datetime.date(2025, 1, 5)  
        num_semanas = 5  
        escalas_por_instrumento = {}

        for instrumento, integrantes in instrumentos.items():
            escalas_por_instrumento[instrumento] = []
            for i in range(num_semanas):
                integrante_index = i % len(integrantes)
                escalas_por_instrumento[instrumento].append(integrantes[integrante_index])

        # Criar escala geral por dia de culto
        escala_por_data = {}
        for i in range(num_semanas):
            data = data_inicial + datetime.timedelta(weeks=i)
            data_str = data.strftime('%d/%m/%Y')
            escala_por_data[data_str] = []
            for instrumento in instrumentos:
                escala_por_data[data_str].append(escalas_por_instrumento[instrumento][i])

        # Construir a string da escala
        escala_str = f"Escala para Janeiro de 2025 ({self.nome_grupo}):\n\n"
        for data_str, integrantes_do_dia in escala_por_data.items():
            escala_str += f"Culto em {data_str}:\n"
            for integrante in integrantes_do_dia:
                escala_str += f"- {integrante}\n"
            escala_str += "\n"

        return escala_str


def main():
    st.title("Escala de Louvor")

    # Inicializar st.session_state
    if 'integrantes' not in st.session_state:
        st.session_state.integrantes = []

    # Cadastrar integrantes
    st.header("Cadastrar Integrantes")
    nome = st.text_input("Nome do integrante:")
    instrumento = st.text_input("Instrumento:")
    if st.button("Adicionar Integrante"):
        integrante = Integrante(nome, instrumento)
        st.session_state.integrantes.append(integrante) 
        st.success(f"{nome} ({instrumento}) adicionado ao grupo!")

    # Limpar integrantes
    if st.button("Limpar Integrantes"):
        st.session_state.integrantes = []  
        st.warning("Lista de integrantes limpa!")

    # Gerar escala
    st.header("Gerar Escala")
    if st.button("Gerar Escala para Janeiro de 2025"):
        grupo = GrupoDeLouvor("Louvor da Igreja") 
        grupo.integrantes = st.session_state.integrantes  
        escala = grupo.gerar_escala()
        st.text(escala)

if __name__ == "__main__":
    main()