import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from scipy.stats import chi2_contingency

df = pd.read_csv('sonveri2.csv')

#deneme amaçlı film türleri ile şiddet içeriği karşılaştırıldı
# Çapraz tabloyu oluştur
cross_tab = pd.crosstab(df['Genre'], df['Violence'])

# Ki-kare testi
chi2, p, _, _ = chi2_contingency(cross_tab)

# Hipotezi test et
alpha = 0.05
if p < alpha:
    print("H0 hipotezi reddedilir, Genre ve Violence arasında anlamlı bir bağlantı vardır.")
else:
    print("H0 hipotezi reddedilemez, Genre ve Violence arasında anlamlı bir bağlantı yoktur.")

# "Votes" sütunundaki virgülleri temizle
df['Votes'] = df['Votes'].str.replace(',', '')

# "Votes" sütununu float'a dönüştür
df['Votes'] = pd.to_numeric(df['Votes'], errors='coerce')

# Bağımlı (y) ve bağımsız (X) değişkenleri belirle
y = df['Rate']
X = df[['Votes', 'Duration']]

# Veriyi eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Eksik değerleri doldur
imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

# Regresyon modelini oluştur
model = LinearRegression()

# Modeli eğit
model.fit(X_train_imputed, y_train)

# Modeli kullanarak tahmin yap
y_pred = model.predict(X_test_imputed)

# Modelin performansını değerlendir
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

###################################################################################
#Film içeriklerine göre film önerisi yap
# Bağımlı (y) ve bağımsız (X) değişkenleri belirle
X = df[['Violence', 'Alcohol', 'Frightening', 'Profanity', 'Nudity']]
y = df['Genre']

# # Label Encoding : verdiğimiz sütunlar kategorik veriler içerdiği için sayısal verilere dönüştürüyor.
label_encoder = LabelEncoder()
X.loc[:, 'Violence'] = label_encoder.fit_transform(X['Violence'])
X.loc[:, 'Alcohol'] = label_encoder.fit_transform(X['Alcohol'])
X.loc[:, 'Frightening'] = label_encoder.fit_transform(X['Frightening'])
X.loc[:, 'Profanity'] = label_encoder.fit_transform(X['Profanity'])
X.loc[:, 'Nudity'] = label_encoder.fit_transform(X['Nudity'])


# Veriyi eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Sınıflandırma modelini oluştur
model = RandomForestClassifier()    #daha güvenilir sonuçlar elde edilmesini sağlar, karar ağaçları kullanılır, daha geniş uygulama yelpazesi için kullanılabilir

# Modeli eğit
model.fit(X_train, y_train)

# Modelin performansını değerlendir
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Modelin doğruluğu: {accuracy}")

# Kullanıcıdan dereceleri al
user_ratings = {
    'Violence': input("Şiddet derecesini (Mild, Moderate, Severe) girin: "),
    'Alcohol': input("Alkol derecesinini (Mild, Moderate, Severe) girin: "),
    'Frightening': input("Korku derecesini ni (Mild, Moderate, Severe) girin: "),
    'Profanity': input("Argo derecesini (Mild, Moderate, Severe) girin: "),
    'Nudity': input("Çıplaklık derecesini (Mild, Moderate, Severe) girin: ")
}

# Kullanıcının girdiği dereceleri Label Encoding(kategorik verileri sayısal verilere dönüştürür) ile uygun hale getir
user_ratings_encoded = {
    'Violence': label_encoder.transform([user_ratings['Violence']])[0],
    'Alcohol': label_encoder.transform([user_ratings['Alcohol']])[0], 
    'Frightening': label_encoder.transform([user_ratings['Frightening']])[0],
    'Profanity': label_encoder.transform([user_ratings['Profanity']])[0],
    'Nudity': label_encoder.transform([user_ratings['Nudity']])[0]
}

# Kullanıcının girdiği derecelere göre film türü tahmini yap
user_genre_prediction = model.predict([[user_ratings_encoded['Violence'], user_ratings_encoded['Alcohol'],
                                       user_ratings_encoded['Frightening'], user_ratings_encoded['Profanity'],
                                       user_ratings_encoded['Nudity']]])

# Sütun adını kontrol et ve düzelt
genre_column_name = 'Genre' 

# Tahmin edilen film türüne göre bir film önerisi yap
recommended_film = df[df[genre_column_name] == user_genre_prediction[0]]['Name'].iloc[0]
recommended_film1 = df[df[genre_column_name] == user_genre_prediction[1]]['Name'].iloc[1]
recommended_film2 = df[df[genre_column_name] == user_genre_prediction[2]]['Name'].iloc[2]

print(f"Önerilen Film: {recommended_film}")
print(f"Önerilen Film: {recommended_film1}")
print(f"Önerilen Film: {recommended_film2}")




