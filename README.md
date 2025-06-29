# ⏱️ Cálculo de Tempo de Tiros

Um app simples em **Streamlit** para somar e subtrair tempos no formato `MM:SS:CS` (minutos, segundos, centésimos).

## 🚀 Como usar

1️⃣ Clone o repositório ou abra o app no Streamlit Cloud.  
2️⃣ Rode o app localmente com:
```bash
streamlit run app.py
```
3️⃣ No app, digite os tempos no formato `MM:SS:CS` (exemplo: `09:11:93`).
4️⃣ Escolha a operação: soma ou subtração.
5️⃣ Veja o resultado formatado na tela.

## 🌐 Deploy no Streamlit Cloud

Você pode abrir diretamente no [Streamlit Cloud](https://streamlit.io/cloud) conectando seu repositório clonado e clicando em **Deploy**.

## 📦 Requisitos

* Python 3.7+
* streamlit

Instale as dependências com:

```bash
pip install -r requirements.txt
```

## ⚠️ Observações

* O app ajusta o resultado da subtração para positivo caso o resultado seja negativo.
* O formato esperado é sempre `MM:SS:CS`, com 2 dígitos para minutos, segundos e centésimos.

---

✅ Feito por Danilo Alves
