from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

# Setup Selenium
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Menjalankan tanpa membuka jendela browser
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Inisialisasi driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Buka Tokopedia
url = "https://www.tokopedia.com/"
driver.get(url)

# Tunggu agar halaman termuat
time.sleep(5)

# Ambil elemen produk
produk_list = driver.find_elements(By.CLASS_NAME, "prd_link-product-name")

# Menulis ke file CSV
with open("produk.csv", 'w', newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["No", "Nama Produk"])  # Menambahkan header

    for i, produk in enumerate(produk_list[:100], start=1):  # Batasi hanya 100 produk
        title = produk.text.strip()
        writer.writerow([i, title])
        print(f"{i}. {title}")

# Tutup browser
driver.quit()

print("Scraping selesai! Data disimpan di produk.csv.")
