import yfinance as yf
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Hisselerin sembollerini belirleyin
symbols =  [ "THYAO.IS","ASELS.IS", "BOSSA.IS", "BRISA.IS", "AYES.IS" ,"AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]

# Geçmiş verileri indirin
historical_data = yf.download(symbols, start='2023-11-11', end='2024-01-01')['Adj Close']

# Verileri günlük getiriye dönüştürün
returns = historical_data.pct_change().dropna()

# Özellik mühendisliği: Ortalama getiri ve volatiliteyi hesaplayın
features = pd.DataFrame()
features['mean_return'] = returns.mean()
features['volatility'] = returns.std()

# Verileri ölçeklendirin
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# K-means kümeleme uygulayın
num_clusters = 3  # Değiştirilebilir: İstenen küme sayısı
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
features['cluster'] = kmeans.fit_predict(scaled_features)

# Kümeleri yazdırın
for cluster in range(num_clusters):
    print(f"Cluster {cluster + 1}:\n{features[features['cluster'] == cluster]}\n")

# Buradan sonra, her kümeye göre al, sat veya tut stratejilerini belirleyebilirsiniz.

# Her kümenin ortalama getirisini hesaplayın
mean_returns = features.groupby('cluster')['mean_return'].mean()

# Her kümenin volatilitesini hesaplayın
volatility = features.groupby('cluster')['volatility'].mean()

# Her küme için bir risk/getiri profili oluşturun
risk_return = pd.DataFrame({
    'cluster': mean_returns.index,
    'mean_return': mean_returns,
    'volatility': volatility
})

# Risk/getiri profiline göre bir al, sat veya tut stratejisi belirleyin
strategy = []
for cluster in range(num_clusters):
    if risk_return.loc[cluster, 'mean_return'] > 0 and risk_return.loc[cluster, 'volatility'] < 0.2:
        strategy.append('al')
    elif risk_return.loc[cluster, 'mean_return'] < 0 and risk_return.loc[cluster, 'volatility'] > 0.2:
        strategy.append('sat')
    else:
        strategy.append('tut')

# Sonuçları yazdırın
print('Kümelere göre al, sat veya tut stratejileri:')
for cluster in range(num_clusters):
    print(f"Cluster {cluster + 1}: {strategy[cluster]}")