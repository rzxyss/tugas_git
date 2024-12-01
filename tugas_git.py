data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen':{
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi' : 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai' : 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# Nomor 1
print("Nomor 1")
for i,j in data_panen.items():
    print(f"Lokasi : {j["nama_lokasi"]}")
    for hasil in j["hasil_panen"].items():
        print(f"Hasil Panen : {hasil}")
        
# Nomor 2
print("\nNomor 2")
print(f"Data Panen Jagung Dari Lokasi 2 adalah {data_panen["lokasi2"]["hasil_panen"]["jagung"]}")

# Nomor 3
print("\nNomor 3")
print(f"Nama Dari Lokasi 3 adalah {data_panen["lokasi3"]["nama_lokasi"]}")

# Nomor 4
print("\nNomor 4")
jumlah_hasil_padi = 0
jumlah_hasil_kedelai = 0
for i,j in data_panen.items():
    jumlah_hasil_padi += j["hasil_panen"]["jagung"]

for k,l in data_panen.items():
    jumlah_hasil_kedelai += l["hasil_panen"]["kedelai"]
    
print(f"Jumlah Hasil Panen Padi : {jumlah_hasil_padi}")
print(f"Jumlah Hasil Panen Kedelai : {jumlah_hasil_kedelai}")