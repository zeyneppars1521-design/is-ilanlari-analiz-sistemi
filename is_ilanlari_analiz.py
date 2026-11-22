import pandas as pd

veriler = {
    "Pozisyon": [
        "Python Developer",
        "Data Analyst",
        "AI Engineer",
        "Software Developer",
        "Data Scientist",
        "Python Developer"
    ],

    "Sehir": [
        "İstanbul",
        "Ankara",
        "İstanbul",
        "İzmir",
        "Ankara",
        "İzmir"
    ],

    "Deneyim": [
        "Junior",
        "Mid",
        "Senior",
        "Junior",
        "Senior",
        "Mid"
    ],

    "Maas": [
        25000,
        35000,
        55000,
        28000,
        60000,
        38000
    ]
}

df = pd.DataFrame(veriler)

print(df)

# Toplam ilan sayısı
print("Toplam ilan:", len(df))

# İlan bulunan şehirler
print("Şehirler:", df["Sehir"].unique())

# En yüksek maaş
print("En yüksek maaş:", df["Maas"].max())

# En yüksek maaşlı pozisyon
en_yuksek = df.loc[df["Maas"].idxmax()]

print("En yüksek maaşlı pozisyon:", en_yuksek["Pozisyon"])

sonuc = df[
    (df["Sehir"] == "Ankara") &
    (df["Maas"] >= 35000) &
    (df["Deneyim"] != "Junior")
]

print("Arama kriterlerine uygun ilanlar:")
print(sonuc)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))

plt.bar(df["Pozisyon"], df["Maas"])

plt.title("Pozisyonlara Göre Maaş Dağılımı")
plt.xlabel("Pozisyon")
plt.ylabel("Maaş (TL)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("reports/maas_analizi.png")
plt.show()
df.to_excel("reports/is_ilanlari_raporu.xlsx", index=False)

print("Excel raporu oluşturuldu!")

# Genel maaş istatistikleri

print("\n--- MAAŞ ANALİZİ ---")

print("Ortalama maaş:", df["Maas"].mean())
print("En düşük maaş:", df["Maas"].min())
print("En yüksek maaş:", df["Maas"].max())

# Şehirlere göre ilan sayısı

print("\n--- ŞEHİRLERE GÖRE İLAN SAYISI ---")

print(df["Sehir"].value_counts())

# Deneyim seviyelerine göre ilan sayısı

print("\n--- DENEYİM SEVİYELERİ ---")

print(df["Deneyim"].value_counts())