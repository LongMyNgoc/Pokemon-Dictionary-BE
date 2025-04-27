# app/services/pokemon_service.py

import asyncio
from utils.pokemon_list.http_pokemon_list import fetch_detail
from utils.fetch_page_data.fetch_page_data import fetch_page_data

async def get_all_pokemons():
    base_url = "https://pokeapi.co/api/v2/pokemon"
    limit = 100  # Số lượng tối đa lấy mỗi lần
    total_pokemon = 1025  # Tổng số Pokémon

    pokemons = []

    # Tạo danh sách các task bất đồng bộ cho nhiều trang
    tasks = []
    for offset in range(0, total_pokemon, limit):
        current_limit = min(limit, total_pokemon - offset)  # Điều chỉnh limit để không lấy quá 1025
        url = f"{base_url}?limit={current_limit}&offset={offset}"
        tasks.append(fetch_page_data(url))  # Thêm các task vào danh sách

    # Chạy tất cả các task song song
    page_data = await asyncio.gather(*tasks)

    # Lấy chi tiết Pokémon từ các page data đã tải
    for data in page_data:
        results = data["results"]
        pokemon_details = await asyncio.gather(*[fetch_detail(p) for p in results])
        pokemons.extend(pokemon_details)

    return pokemons

