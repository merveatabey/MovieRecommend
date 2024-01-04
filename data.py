import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('imdb.csv')     #veri setini yükle

#Veri manipülasyonu
print(df.isnull().sum())   #eksik verileri kontrol et
#eksik veri bulunmamaktadır.

df["Date"]=pd.to_datetime(df["Date"])    #boş tarih NaT(not a time) değeri yoktur
#print(df.to_string())

# Boş değerleri içeren satırları sil

df = df.dropna(subset=['Duration'])

#print(df.to_string())

df = df.dropna(subset=['Episodes'])
#print(df.to_string())

#df.to_csv("sonveri.csv")

#tekrar eden satırları sil
df=df.drop_duplicates()
print(df.to_string())

# "Rate" sütunu içinde "no rate" değeri geçen satırları sil
df = df[df['Rate'] != 'No Rate']
df = df[df['Votes'] != 'No Rate']
df = df[df['Name'] != 'No Rate']
df = df[df['Date'] != 'No Rate']
df = df[df['Duration'] != 'No Rate']
df = df[df['Genre'] != 'No Rate']
df = df[df['Type'] != 'No Rate']
df = df[df['Certificate'] != 'No Rate']
df = df[df['Episodes'] != 'No Rate']
df = df[df['Nudity'] != 'No Rate']
df = df[df['Violence'] != 'No Rate']
df = df[df['Profanity'] != 'No Rate']
df = df[df['Alcohol'] != 'No Rate']
df = df[df['Frightening'] != 'No Rate']


df = df[df['Rate'] != 'None']
df = df[df['Votes'] != 'None']
df = df[df['Name'] != 'None']
df = df[df['Date'] != 'None']
df = df[df['Duration'] != 'None']
df = df[df['Genre'] != 'None']
df = df[df['Type'] != 'None']
df = df[df['Certificate'] != 'None']
df = df[df['Episodes'] != 'None']
df = df[df['Nudity'] != 'None']
df = df[df['Violence'] != 'None']
df = df[df['Profanity'] != 'None']
df = df[df['Alcohol'] != 'None']
df = df[df['Frightening'] != 'None']

#tekrar eden satırlar silindikten sonraki son veri
df.to_csv("sonveri2.csv")





