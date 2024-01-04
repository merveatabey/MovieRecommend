import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import shapiro
from scipy.stats import normaltest
from scipy.stats import anderson


df = pd.read_csv('sonveri2.csv')

#Normal Dağılım ve Görsel Normallik Testler

# Örnek: Rate değişkeninin histogramı

plt.figure(figsize=(10, 6))
sns.histplot(df['Rate'], kde=True, color='skyblue')
plt.title('Rate Değişkeninin Histogramı')
plt.xlabel('Rate')
plt.ylabel('Frekans')
plt.show()

#histogramda birden fazla zirve olduğu için normal dağılıma uymamaktadır


plt.figure(figsize=(10, 6))
sns.histplot(df['Votes'], kde=True, color='skyblue')
plt.title('Vote Değişkeninin Histogramı')
plt.xlabel('Vote')
plt.ylabel('Frekans')
plt.show()



plt.figure(figsize=(10, 6))
sns.histplot(df['Duration'], kde=True, color='skyblue')
plt.title('Duration Değişkeninin Histogramı')
plt.xlabel('Duration')
plt.ylabel('Frekans')
plt.show()

###############################################################################################

#İstatistiksel Normallik Testleri

# Örnek: 'Rate' değişkeni üzerinde Shapiro-Wilk Testi


df['Rate'] = pd.to_numeric(df['Rate'], errors='coerce')
df = df.dropna(subset=['Rate'])
stat, p_value = shapiro(df['Rate'])

# Test İstatistiği ve p-value değerlerini yazdırma
print(f'Test İstatistiği: {stat}, p-value: {p_value}')

# p-value değerini kullanarak hipotez testi yapma
alpha = 0.05  # Anlamlılık düzeyi
if p_value > alpha:
    print("H0 hipotezi reddedilemez, veri seti normal dağılıma uyar.")
else:
    print("H0 hipotezi reddedilir, veri seti normal dağılıma uymaz.")



df['Votes'] = pd.to_numeric(df['Votes'], errors='coerce')
df = df.dropna(subset=['Votes'])

# Votes için ki kare testi
stat, p_value = normaltest(df['Votes'])
print(f'D\'Agostino\'s K^2 Test - Statistic: {stat}, p-value: {p_value}')

if p_value > alpha:
    print("H0 hipotezi reddedilemez. Veri normal bir dağılıma uyar.")
else:
    print("H0 hipotezi reddedildi. Veri normal bir dağılıma uymamaktadır.")



# Örnek: 'Duration' değişkeni üzerinde Anderson-Darling Testi
result = anderson(df['Duration'], dist='norm')

# Test İstatistiği, Kritik Değerler ve Anlamlılık Düzeyi değerlerini yazdırma
print(f'Test İstatistiği: {result.statistic}')
print(f'Kritik Değerler: {result.critical_values}')
print(f'Anlamlılık Düzeyi: {result.significance_level}')

# Test İstatistiği ile karşılaştırarak hipotez testi yapma
alpha = 0.05  # Anlamlılık düzeyi
if result.statistic < result.critical_values[2] and result.significance_level > alpha:
    print("H0 hipotezi reddedilemez, veri seti normal dağılıma uyar.")
else:
    print("H0 hipotezi reddedilir, veri seti normal dağılıma uymaz.")



# 'Rate' değişkeninin standart sapmasını hesapla
rate_std = np.std(df['Rate'])
print(f"Rate Değişkeninin Standart Sapması: {rate_std}")

# 'Rate' değişkeninin çeyrekler arası aralığını (IQR) hesapla
Q1 = np.percentile(df['Rate'], 25)
Q3 = np.percentile(df['Rate'], 75)
rate_iqr = Q3 - Q1
print(f"Rate Değişkeninin Çeyrekler Arası Aralığı (IQR): {rate_iqr}")


#rate için z skorla aykırı değerleri temizledik 

# Örnek: 'Rate' değişkeni için Z-skor hesaplama
z_scores = (df['Rate'] - np.mean(df['Rate'])) / np.std(df['Rate'])

# Aykırı değer sınırını belirleme (standart sapmanın 3 katı olarak alalım)
outlier_threshold = 4.47

# Aykırı değerleri tespit etme
outliers = np.where(np.abs(z_scores) > outlier_threshold)[0]

# Aykırı değerleri silme
df_cleaned = df.drop(df.index[outliers])

# Temizlenmiş veri setinin sayısını yazdır
print(f"Temizlenmiş Veri Seti Sayısı: {len(df_cleaned)}")


# 'Rate' değişkeni üzerinde Shapiro-Wilk testi yapma
stat, p_value = shapiro(df['Rate'])

# Test istatistiği ve p değerini yazdırma
print(f"Shapiro-Wilk Test İstatistiği: {stat}")
print(f"P Değeri: {p_value}")

# P değerini kullanarak hipotez testi yapma
alpha = 0.05  # Anlamlılık düzeyi
if p_value > alpha:
    print("H0 hipotezi reddedilemez, veri seti normal dağılıma uyar.")
else:
    print("H0 hipotezi reddedilir, veri seti normal dağılıma uymaz.")



