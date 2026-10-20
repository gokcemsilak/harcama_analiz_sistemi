from datetime import datetime
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
 


connection =  mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME") 
    )
print("MySQL bağlantısı başarılı!")

#kullanıcı bilgileri girecek, Python bu bilgileri MySQL'e gönderecek.

def harcama_ekle():   
    aciklama = input("Harcama açıklaması:").strip()
    kategori = input("Kategori:").strip()
    try:

        tutar = float(input("Tutar:"))
    except ValueError:
        print("Hata: Lütfen geçerli bir sayısal tutar giriniz!")
        return # hatalı girişte fonksiyonu burada sonlandırır ve veritabanına eksik-hatalı veri girmez
    if tutar <= 0:
        print("Hata : Tutar sıfırdan büyük olmalıdır")
        return
    tarih  = input("Tarih (YYYY-AA-GG):").strip()
    try:
        tarih_obj = datetime.strptime(tarih, "%Y-%m-%d").date()
    except ValueError:
        print("Hata: Geçersiz tarih formatı! Lütfen YYYY-AA-GG(Örn: 2026-10-20) formatında giriniz.")
        return
    sql = """
    INSERT INTO harcamalar (aciklama, kategori,  tutar, tarih)
    VALUES (%s, %s, %s, %s)
    """
    veri = (aciklama, kategori, tutar, tarih)

    cursor = connection.cursor()
    cursor.execute(sql, veri)
    connection.commit()

   
    print("Harcama başarıyla eklendi!")

# Harcamaları MySQL'den Python'a çekelim

def harcamalari_listele():
    sql = "SELECT * FROM harcamalar"
    cursor = connection.cursor()
    cursor.execute(sql)
    sonuclar = cursor.fetchall()
    for id, aciklama, kategori, tutar, tarih in sonuclar:
            print(f"ID: {id} | {aciklama} | {kategori} | {tutar} TL | {tarih}")

def harcama_sil():
    try:
        id = int(input("Silmek istediğiniz harcamanın ID'si:"))
    except ValueError:
        print("Hata: ID tamsayı olmalıdır")
        return
    sql = "DELETE FROM harcamalar WHERE id = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (id,))
    connection.commit()
    if cursor.rowcount > 0:
        print("Harcama başarıyla silindi!")
    else:
        print("Bu ID ile eşleşen harcama bulunamadı.")

def harcama_guncelle(): 
    try:

        id = int(input("Güncellemek istediğiniz harcamanın ID'si:"))
        yeni_tutar = float(input("Yeni tutarı giriniz:"))
    except ValueError:
        print("Hata: ID tam sayı, tutar ise geçerli bir sayı olmalıdır")
        return 
    if yeni_tutar <= 0:
            print("Hata : Tutar sıfırdan büyük olmalıdır")
            return 

    sql = "UPDATE harcamalar SET tutar = %s WHERE id = %s " 
    cursor = connection.cursor()
    cursor.execute(sql, (yeni_tutar, id))
    connection.commit()
    if cursor.rowcount > 0:
        print("Harcama başarıyla güncellendi!")
    else:
        print("Bu ID ile eşleşen harcama bulunamadı.")

def toplam_harcama():

    sql = "SELECT SUM(tutar) FROM harcamalar ;"
    cursor = connection.cursor()
    cursor.execute(sql)
    sonuc = cursor.fetchone()

    toplam = sonuc[0] if sonuc[0] is not None else 0
    print(f"Toplam harcama: {toplam} TL")

def kategori_analizi():

    sql = """
    SELECT kategori, SUM(tutar)
    FROM harcamalar
    GROUP BY kategori
    """
    
    cursor = connection.cursor()
    cursor.execute(sql)
    sonuclar = cursor.fetchall()

    for kategori, toplam in sonuclar:
        print(f"Kategori: {kategori} | Toplam tutar: {toplam} TL")  


# şu anda öenü sistemi kurucaz, program açılınca kullanıcıya seçenek suncaz 
while True: # progrmaın menüyü sürekli göstermesini sağlıcak

    print("\n===========================")
    print(" HARCAMA ANALİZ SİSTEMİ ")
    print("=============================")
    print("1 - Harcama Ekle")
    print("2 - Harcamaları Listele")
    print("3 - Harcama Sil")
    print("4 - Harcama Güncelle")
    print("5 - Toplam Harcamayı Görüntüle")
    print("6 - Kategori Bazında Harcama Analizi")
    print("7 - Çıkış")
    secim = input("Seçiminiz:")
    if secim == "1":
        harcama_ekle()

    elif secim == "2":
        harcamalari_listele()

    elif secim == "3":      
       harcama_sil()

    elif secim == "4":
        harcama_guncelle()

    elif secim == "5":
        toplam_harcama()

    elif secim == "6":
        kategori_analizi()

    elif secim == "7":
        print("Çıkış yapılıyor!")
        break
    else:
        print("Geçersiz seçim!")
