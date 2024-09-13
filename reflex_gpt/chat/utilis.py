import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('cloudflare_bypass.log', mode='w')
    ]
)

import os
import re
import json
import time
import warnings
# from dotenv import load_dotenv
from curl_cffi import requests
from bs4 import BeautifulSoup

import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# path = os.path.join(BASE_DIR, 'Chatgpt', 'chat', 'cookies_headers.json')


# Menonaktifkan peringatan dari modul 'curl_cffi'
warnings.filterwarnings('ignore', module='curl_cffi')

# load_dotenv()


def filter_special_characters(text: str) -> str:
    # Regex pattern untuk mencocokkan karakter non-huruf, non-angka, dan non-tanda baca
    pattern = r'[^a-zA-Z0-9.,!?\'"]'
    
    # Menghapus karakter khusus
    filtered_text = re.sub(pattern, ' ', text)
    
    return filtered_text


def save_captcha_key(url, result):
    json_filename = "captcha.json"

    # Mendapatkan captcha_key dari URL
    captcha_key = url.split("captcha_key=")[-1]

    # Membaca data yang ada dari file JSON, atau membuat dictionary kosong jika file belum ada
    if os.path.exists(json_filename):
        with open(json_filename, "r") as json_file:
            data = json.load(json_file)
    else:
        data = {}
    
    data[captcha_key] = result

    # Menyimpan data kembali ke file JSON
    with open(json_filename, "w") as json_file:
        json.dump(data, json_file, indent=4)

    logging.info(f"Data dengan captcha_key '{captcha_key}' berhasil disimpan ke dalam '{json_filename}'.")


from urllib.parse import urlparse, parse_qs

def extract_captcha_params(url):
    # Parsing URL
    parsed_url = urlparse(url)
    
    # Mengambil query string dari URL
    query_string = parsed_url.query
    
    # Parsing query string menjadi dictionary
    params = parse_qs(query_string)
    
    # Mengambil nilai uuid dan captcha_key dari dictionary
    uuid = params.get('uuid', [None])[0]
    captcha_key = params.get('captcha_key', [None])[0]
    
    return uuid, captcha_key



def check_key_in_json(file_path, key_to_check):
    """
    Memeriksa apakah key yang diberikan ada di dalam file JSON dan mengembalikan value-nya.
    """
    try:
        # Membuka dan memuat data dari file JSON
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Memeriksa apakah key ada dalam data JSON
        if key_to_check in data:
            logging.info(f"Key '{key_to_check}' ditemukan di dalam JSON dengan value: {data[key_to_check]}")
            return data[key_to_check]
        else:
            logging.info(f"Key '{key_to_check}' tidak ditemukan di dalam JSON.")
            return 
    
    except FileNotFoundError:
        logging.info(f"File '{file_path}' tidak ditemukan.")
        return 
    
    except json.JSONDecodeError:
        logging.info(f"File '{file_path}' bukan file JSON yang valid.")
        return 



def update_env_variable(variable_name, variable_value, file_path='.env'):
    # Membaca isi file .env terlebih dahulu
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Memodifikasi hanya baris yang berisi variable_name
        with open(file_path, 'w') as file:
            updated = False
            for line in lines:
                if line.startswith(f'{variable_name}='):
                    file.write(f'{variable_name}={variable_value}\n')
                    updated = True
                else:
                    file.write(line)

            # Jika tidak ditemukan, tambahkan variable di akhir file
            if not updated:
                file.write(f'{variable_name}={variable_value}\n')
        
        return True
    except FileNotFoundError:
        # Jika file tidak ada, buat baru dengan variable
        with open(file_path, 'w') as file:
            file.write(f'{variable_name}={variable_value}\n')
        
        return None
