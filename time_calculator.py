import streamlit as st
from datetime import timedelta

def parse_tempo(tempo_str):
    """Converte string MM:SS:CS para timedelta"""
    try:
        partes = tempo_str.strip().split(':')
        if len(partes) != 3:
            return None
        minutos = int(partes[0])
        segundos = int(partes[1])
        centesimos = int(partes[2])
        # 1 centésimo = 10 milissegundos
        return timedelta(minutes=minutos, seconds=segundos, milliseconds=centesimos * 10)
    except:
        return None

def format_timedelta(td):
    """Converte timedelta para string MM:SS:CS"""
    total_seconds = int(td.total_seconds())
    minutos = total_seconds // 60
    segundos = total_seconds % 60
    centesimos = int((td.microseconds // 10000) % 100)
    return f"{minutos:02d}:{segundos:02d}:{centesimos:02d}"

st.title("⏱️ Cálculo de Tempo de Tiros")

st.write("Digite os tempos no formato **MM:SS:CS** (exemplo: 09:11:93)")

tempo1 = st.text_input("Tempo 1", "00:00:00")
tempo2 = st.text_input("Tempo 2", "00:00:00")

op = st.radio("Operação", ["Soma", "Subtração"])

if st.button("Calcular"):
    td1 = parse_tempo(tempo1)
    td2 = parse_tempo(tempo2)

    if td1 is None or td2 is None:
        st.error("⚠️ Formato inválido. Use MM:SS:CS (ex: 09:11:93)")
    else:
        if op == "Soma":
            resultado = td1 + td2
        else:
            resultado = td1 - td2
            if resultado.total_seconds() < 0:
                st.warning("O resultado ficou negativo, converti para positivo.")
                resultado = -resultado
        st.success(f"Resultado: {format_timedelta(resultado)}")
