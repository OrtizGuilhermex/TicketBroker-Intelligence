import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv('airline_ticket_prices_dataset.csv')

encoders = {}
for col in ['Origin', 'Destination', 'Airline', 'Class']:
    le =LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

features = ['Origin', 'Destination', 'Airline', 'Distance_km', 'Days_Before_Departure', 'Class']
X = df[features]
y = df['Price_USD']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X,y)

joblib.dump(model, 'modelo_preço_voos.pkl')
joblib.dump(encoders, 'encoders_voos.pkl')

print("✅ Engine de Preço Justo treinada com sucesso!")