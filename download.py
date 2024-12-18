import json
import os
import urllib.request

api_url = "https://osu.ppy.sh/api/v2/seasonal-backgrounds"

with urllib.request.urlopen(api_url) as response:
    data = response.read().decode("utf-8")

data_dict = json.loads(data)

folder_name = f"osu_season_backs_{data_dict["ends_at"]}"

print(f"Создаю папку {folder_name}...")
os.makedirs(folder_name, exist_ok=True)

print(f"Перехожу в папку {folder_name}...")
os.chdir(folder_name)

background_urls = [bg["url"] for bg in data_dict["backgrounds"]]
for url in background_urls:
    filename = os.path.basename(url)
    print(f"Скачиваю {filename}...")
    urllib.request.urlretrieve(url, filename)

print("Загрузка завершена")
