#!/bin/bash

api_url="https://osu.ppy.sh/api/v2/seasonal-backgrounds"

folder_name="osu_season_backs_$(curl -s "$api_url" | jq -r '.ends_at')"

echo "Создаю папку $folder_name..."
mkdir -p "$folder_name"

echo "Перехожу в папку $folder_name..."
cd "$folder_name" || exit

curl -s "$api_url" | jq -r '.backgrounds[].url' | while read -r url; do
    filename="${url##*/}"
    echo "Скачиваю $filename..."
    curl -s -O "$url"
done

echo "Загрузка завершена"
