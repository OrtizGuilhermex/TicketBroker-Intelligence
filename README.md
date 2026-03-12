# 💹 Ticket Broker Intelligence (TBI)

**Terminal de Alta Performance para Arbitragem e Predição de Valor Justo em Tickets Aéreos**

O **Ticket Broker Intelligence** é uma solução avançada de análise de dados que utiliza **Machine Learning** para decifrar a volatilidade do mercado aéreo.

O objetivo central é fornecer ao operador o **Fair Value (Preço Justo)** de uma rota, permitindo a identificação imediata de **spreads lucrativos** e **oportunidades de compra (arbitragem)**.

---

# 🔍 Visão Geral

No mercado aéreo, os preços flutuam baseados em **algoritmos complexos de demanda**.

O **TBI** inverte essa lógica em favor do usuário, utilizando um **regressor treinado em milhares de pontos de dados** para projetar **onde o preço deveria estar**.

## 📊 O conceito de Fair Value

Diferente de uma busca comum, o **TBI calcula o equilíbrio estatístico** entre diversos fatores relevantes do mercado.

### ✈️ Antecedência Crítica

O impacto exato de **quantos dias faltam para o voo**.

### 🌍 Peso de Rota

A **distância e relevância econômica** entre origem e destino.

### 🎫 Segmentação

Diferenciação técnica entre classes de passagem:

* Econômica
* Executiva
* First Class

---

# 🧠 Arquitetura de Inteligência

O motor preditivo foi construído utilizando **Ensemble Learning** com o algoritmo **Random Forest Regressor**.

### 🔹 Processamento de Dados

* **Label Encoding** para variáveis categóricas
* Conversão de **cidades e companhias aéreas** em valores numéricos

### 🔹 Modelo

* **Random Forest Regressor (Scikit-Learn)**
* **100+ estimadores** para maior robustez preditiva

### 🔹 Persistência

* Serialização do modelo via **Joblib**
* Carregamento instantâneo no terminal

---

# 🖥️ Interface do Terminal

O design foi construído sob a filosofia **Premium Dark Mode**, focando apenas nos elementos essenciais para **tomada de decisão rápida**.

### 📊 Dashboard de Veredito

Exibe:

* **Valor Justo (Fair Value)**
* **Spread**
* **Status da Ordem**

### ⚙️ Painel de Parâmetros

Permite ajustes de:

* Distância da rota
* Dias até o voo
* Preço atual do mercado

### 📜 Log de Operação

Apresenta **detalhamento técnico da rota analisada** ao final da interface.

---

# 🛠️ Tecnologias

| Tecnologia   | Função                 |
| ------------ | ---------------------- |
| Python 3.10+ | Linguagem principal    |
| Streamlit    | Interface do terminal  |
| Scikit-Learn | Machine Learning       |
| Pandas       | Manipulação de dados   |
| Joblib       | Persistência do modelo |

---

# 📥 Instalação

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/ticket-broker-intelligence.git
cd ticket-broker-intelligence
```

---

## 2️⃣ Instale as dependências

```bash
pip install streamlit pandas scikit-learn joblib
```

---

## 3️⃣ Treine o modelo

Caso ainda **não possua os arquivos `.pkl`**, execute:

```bash
python train_voos.py
```

Isso irá gerar o modelo treinado utilizado pelo sistema de análise.

---

## 4️⃣ Execute a aplicação

```bash
streamlit run app.py
```

Após iniciar, o **Streamlit abrirá automaticamente no navegador**.

---

# 🎮 Como Operar

## 1️⃣ Defina a Rota

Insira os dados da viagem:

* ✈️ **Origem**
* 🛬 **Destino**
* 🏢 **Companhia aérea**

---

## 2️⃣ Ajuste o Timeframe

Utilize o **slider** para definir **quantos dias faltam para a viagem**.

---

## 3️⃣ Insira o Preço de Mercado

Digite o valor encontrado em **sites de busca de passagens**.

Exemplos:

* Google Flights
* Skyscanner
* Decolar
* Kayak

---

## 4️⃣ Analise o Veredito

O sistema compara o **preço atual com o valor justo previsto pelo modelo**.

### ✅ COMPRA AUTORIZADA

O preço está **abaixo ou igual ao valor justo estimado**.

➡️ Indica oportunidade de compra.

---

### 🚨 AGUARDAR MELHORIA

O ativo está **supervalorizado pelo mercado (spread positivo)**.

➡️ Recomendação: aguardar redução de preço.

---

# 🧩 Status do Projeto

**Versão:** v1.7
**Estado:** ✅ Operacional

