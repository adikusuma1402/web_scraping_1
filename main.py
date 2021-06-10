from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

#mengambil url, jika hasilnya response 200, berarti kita diijinkan
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

# #mengambil tag header
# header = soup.header
# # print(header)
#
# #mendapatkan tag h1
# h1 = soup.h1
# # print(h1)
#
# #mengambil string dari tag didalam tag
# text_1 = soup.p
# # print(text_1.string)
#
# #mengambil tag a didalam header
# awal_header = soup.header.a
# # print(awal_header)
#
# #mengambil attribute nya saja
# # print(awal_header.attrs)
#
# #mencari attribut tertentu di dalam tag dengan find
# soup.find('div', {'class': 'side-collapse in'})
# print(soup.find('div', {'class': 'side-collapse in'}))

#mencari attribut tertentu di dalam tag dengan find_all

harga_produk = soup.find_all('h4', class_ = 'pull-right price')

nama_produk = soup.find_all('a', class_ = 'title')

deskripsi_produk = soup.find_all('p', class_ = 'description')

review_produk = soup.find_all('p', class_ = 'pull-right')

#mengambil teksnya dari harga_produk
list_harga = []
for i in harga_produk:
    harga = i.text
    list_harga.append(harga)


#mengambil text dari nama_produk
list_nama_prooduk = []
for i in nama_produk:
    nama = i.text
    list_nama_prooduk.append(nama)

#mengambil teks dari deskripsi_produk
list_deskripsi = []
for i in deskripsi_produk:
    desc = i.text
    list_deskripsi.append(desc)


#mengambil teks dari review_produk
list_review = []
for i in review_produk:
    review = i.text
    list_review.append(review)

tabel = pd.DataFrame({'Nama_Produk': list_nama_prooduk,
                      'Harga_produk':list_harga,
                      'Deskripsi': list_deskripsi,
                      'Jumlah_Review': list_review
                      })

tabel.to_csv('hasil_scraping.csv')