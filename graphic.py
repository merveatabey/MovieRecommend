import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('sonveri2.csv')

# Temel istatistikleri görüntüle
statistics = df.describe()
print(statistics)

# Film türlerinin frekansını bulma
genre_counts = df['Genre'].value_counts()

# Film puanlarının histogram grafiği       
#6.3 puan alan filmlerin sayısı
plt.figure(figsize=(10, 6))
plt.hist(df['Rate'], bins='auto', edgecolor='black')
plt.title('Film Puanlarının Histogramı')
plt.xlabel('Puanlar')
plt.ylabel('Film Sayısı')
plt.show()


# Pair plot grafiği
sns.pairplot(df[['Rate', 'Votes', 'Duration', 'Nudity', 'Violence', 'Profanity', 'Alcohol', 'Frightening']])
plt.suptitle('Pair Plot Grafiği', y=1.02)
plt.show()

# plt.figure(figsize=(12,6))
# # Seaborn barplot kullanımı
# sns.boxplot(x='Type', y='Rate', data=df, palette='Set2', hue='Type', legend=False)  # legend=False gerekmiyor


# # Matplotlib ile eksen etiketleri düzenleme
# plt.xlabel('Film türleri')
# plt.ylabel('Frekans')3

# plt.title('En çok tercih edilen film türleri')
# plt.xticks(rotation=45)  # Eksen etiketlerini döndürme
# plt.show()

######################################################################################################

# Scatter plot oluştur
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Rate', y='Genre', data=df, hue='Genre', palette='Set2', s=100)
plt.title('Film Türleri ve Puanları')
plt.xlabel('Rate')
plt.ylabel('Film Türleri')
plt.legend(title='Film Türleri')
plt.show()


# Box plot grafiği
#Her film türünün puanları karşılaştırıldı
plt.figure(figsize=(10, 6))
sns.boxplot(x='Type', y='Rate', data=df, palette='Set2')
plt.title('Film Türüne Göre Puanlar')
plt.xlabel('Film Türleri')
plt.ylabel('Puanlar')
plt.show()







# Pie plot grafiği
#film ve dizi karşılaştırması
type_counts = df['Type'].value_counts()     #türlerin frekanslarını bulma
plt.figure(figsize=(8, 8))
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral', 'lightgreen'])
plt.title('Film Türlerinin Dağılımı')
plt.show()


# Crosstab ile ilişkiyi bulma
cross_table = pd.crosstab(df['Type'], df['Certificate'])

# Heat map grafiği
#türe göre sertifika karşılaştırılması
plt.figure(figsize=(10, 6))
sns.heatmap(cross_table, annot=True, cmap='YlGnBu', fmt='d', cbar_kws={'label': 'Film Sayısı'})
plt.title('Genre ve Certificate İlişkisi')
plt.xlabel('Certificate')
plt.ylabel('Type')
plt.show()


# Bubble plot grafiği
plt.figure(figsize=(10, 6))
plt.scatter(df['Rate'], df['Votes'], s=df['Duration']*5, alpha=0.7, c='skyblue', edgecolors='black', linewidths=1)
plt.title('Film Puanları, Oy Sayısı ve Süre İlişkisi')
plt.xlabel('Puanlar')
plt.ylabel('Oy Sayısı')
plt.show()


# Violin plot grafiği
#alkol temalı filmlerin puanı
plt.figure(figsize=(10, 6))
sns.violinplot(x='Alcohol', y='Rate', data=df, palette='pastel')
plt.title('Genre ve Rate İlişkisi')
plt.xlabel('Genre')
plt.ylabel('Rate')
plt.show()


# Swarm plot grafiği
#zamana göre küfürlü içerik
plt.figure(figsize=(10, 6))# sns.swarmplot(x='Profanity', y='Date', data=df, hue='Genre', palette='Set2', legend=False)
plt.title('Genre ve Rate İlişkisi')
plt.xlabel('Profanity')
plt.ylabel('Date')
plt.show()

# Cat plot grafiği
plt.figure(figsize=(10, 6))
sns.catplot(x='Votes', y='Type', data=df, kind='box', palette='Set2', hue='Type', legend=False)
plt.title('Genre ve Rate İlişkisi')
plt.xlabel('Votes')
plt.ylabel('Type')
plt.show()



