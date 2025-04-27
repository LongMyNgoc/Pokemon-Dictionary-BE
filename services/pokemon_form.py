# app/services/pokemon_service.py

import asyncio
from utils.fetch_pokemon_form.fetch_pokemon_form import fetch_detail
from utils.fetch_page_data.fetch_page_data import fetch_page_data

async def get_all_pokemons_form():
    base_url = "https://pokeapi.co/api/v2/pokemon"
    limit = 100  # Số lượng tối đa lấy mỗi lần
    offset_start = 1025  # Offset bắt đầu từ Pokémon thứ 1026 (ID = 1026)
    offset_end = 1302  # Offset kết thúc tại Pokémon thứ 1302

    pokemons = []

    # Tạo danh sách các task bất đồng bộ cho nhiều trang
    tasks = []
    for offset in range(offset_start, offset_end, limit):
        current_limit = min(limit, offset_end - offset)  # Điều chỉnh limit để không lấy quá 1302
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
