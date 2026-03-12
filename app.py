import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Ticket Broker | Terminal", layout="wide")

st.markdown("""
    <style>
    .stApp, .stHeader, .main, [data-testid="stSidebar"], [data-testid="stHeader"] {
        background-color: #000000 !important;
    }
    
    h1, h2, h3, h4, h5, h6, p, label, span, div {
        color: #ffffff !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #111111 !important;
        border: 1px solid #333333 !important;
    }
    
    ul[role="listbox"] {
        background-color: #111111 !important;
    }
    
    li[role="option"] {
        background-color: #111111 !important;
        color: #ffffff !important;
    }

    [data-testid="stMetricValue"] {
        color: #00ffa3 !important;
        font-size: 2.8rem !important;
        font-weight: bold !important;
    }
    
    div[data-baseweb="input"] > div, 
    .stNumberInput div {
        background-color: #111111 !important;
        border: 1px solid #333333 !important;
    }

    hr { border: 0.5px solid #222222 !important; }
    div[data-testid="stExpander"] { border: none !important; }
    
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

diretorio = os.path.dirname(os.path.abspath(__file__))
try:
    model = joblib.load(os.path.join(diretorio, 'modelo_preço_voos.pkl'))
    encoders = joblib.load(os.path.join(diretorio, 'encoders_voos.pkl'))
except:
    st.error("Certifique-se de que o modelo_preço_voos.pkl e os encoders estão na mesma pasta.")
    st.stop()

st.markdown("<h1 style='text-align: center;'>💹 TICKET BROKER TERMINAL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666 !important;'>Análise de Valor Justo e Arbitragem</p>", unsafe_allow_html=True)
st.markdown("---")

container_resultado = st.container()

st.markdown("---")

st.markdown("### ⚙️ CONFIGURAÇÃO DA OPERAÇÃO")
c1, c2, c3 = st.columns(3)

with c1:
    origem = st.selectbox("ORIGEM", encoders['Origin'].classes_)
    destino = st.selectbox("DESTINO", encoders['Destination'].classes_)
with c2:
    cia = st.selectbox("COMPANHIA", encoders['Airline'].classes_)
    classe = st.selectbox("CLASSE", encoders['Class'].classes_)
with c3:
    distancia = st.number_input("DISTÂNCIA (KM)", value=1000)
    dias = st.slider("ANTECEDÊNCIA (DIAS)", 1, 150, 30)
    preco_mercado = st.number_input("PREÇO ATUAL (R$)", value=500.0)

input_df = pd.DataFrame([{
    'Origin': encoders['Origin'].transform([origem])[0],
    'Destination': encoders['Destination'].transform([destino])[0],
    'Airline': encoders['Airline'].transform([cia])[0],
    'Distance_km': distancia,
    'Days_Before_Departure': dias,
    'Class': encoders['Class'].transform([classe])[0]
}])

valor_justo = model.predict(input_df)[0]
spread = preco_mercado - valor_justo
porcentagem = (spread / valor_justo) * 100

with container_resultado:
    st.markdown("### 📊 VEREDITO")
    res1, res2, res3 = st.columns([1, 1, 1.5])
    
    with res1:
        st.metric("PREÇO JUSTO", f"R$ {valor_justo:.2f}")
    with res2:
        st.metric("SPREAD", f"R$ {spread:.2f}", f"{porcentagem:.2f}%", delta_color="inverse")
    with res3:
        if preco_mercado <= valor_justo:
            st.markdown(f"""
                <div style='border: 1px solid #00ffa3; padding: 20px; border-radius: 5px; background-color: #001a0f; text-align: center;'>
                    <h2 style='color: #00ffa3 !important; margin: 0;'>✅ COMPRA AUTORIZADA</h2>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div style='border: 1px solid #ff4b4b; padding: 20px; border-radius: 5px; background-color: #1a0000; text-align: center;'>
                    <h2 style='color: #ff4b4b !important; margin: 0;'>🚨 AGUARDAR MELHORIA</h2>
                </div>
            """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("##### 📍 DETALHES DA OPERAÇÃO")
st.write(f"**Rota Selecionada:** {origem} para {destino} | **Ticker:** {cia} | **Categoria:** {classe}")

st.caption("Terminal v1.4 | Dados processados via Random Forest Regressor")