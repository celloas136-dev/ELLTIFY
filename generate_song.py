import os
import json
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

# 1. Dapatkan lokasi folder persis tempat script ini disimpan
base_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Gabungkan lokasi tersebut dengan folder "audio"
audio_folder = os.path.join(base_dir, "audio")

if not os.path.exists(audio_folder):
    print(f"Error: Folder '{audio_folder}' tidak ditemukan!")
    exit()

daftar_lagu = []
files = [f for f in os.listdir(audio_folder) if f.endswith('.mp3')]

if len(files) == 0:
    print(f"Folder 'audio' ketemu, tapi tidak ada file .mp3 di dalamnya!")
    exit()

for file in files:
    file_path = os.path.join(audio_folder, file)
    
    # Nilai bawaan jika metadata MP3 kosong atau gagal dibaca
    artist = "Unknown Artist"
    title = file.replace('.mp3', '') 

    try:
        # Coba baca Metadata / ID3 Tag dari KTP asli MP3-nya
        audio_info = MP3(file_path, ID3=EasyID3)
        
        # Ambil judul jika ada
        if 'title' in audio_info:
            title = audio_info['title'][0]
            
        # Ambil nama artis jika ada
        if 'artist' in audio_info:
            artist = audio_info['artist'][0]
    except Exception as e:
        # Jika gagal dibaca, biarkan pakai nilai bawaan di atas
        pass

    lagu = {
        "title": title,
        "artist": artist,
        "audio": f"audio/{file}",
        "icon": "fa-music",
        # Default cover spotify, biar tampilannya tetap rapi
        "img": "https://i.scdn.co/image/ab6761610000e5eb8ae7f2aaa9817a704a87ea36" 
    }
    daftar_lagu.append(lagu)

print("KODE UNTUK INDEX.HTML ANDA:")
print("--------------------------------------------------")
print("const daftarLagu = " + json.dumps(daftar_lagu, indent=4) + ";")
print("--------------------------------------------------")