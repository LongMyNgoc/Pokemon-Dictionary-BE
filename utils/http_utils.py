# app/utils/http_utils.py

import httpx

async def fetch_page_data(url):
    """Hàm bất đồng bộ lấy dữ liệu của một trang"""
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            return {"error": "Failed to fetch Pokémon list"}
        return response.json()

async def fetch_detail(pokemon):
    """Hàm bất đồng bộ lấy chi tiết Pokémon"""
    async with httpx.AsyncClient() as client:
        detail_response = await client.get(pokemon["url"])
        if detail_response.status_code == 200:
            detail_data = detail_response.json()
            pokemon_id = detail_data["id"]
            name = detail_data["name"]
            types = [t["type"]["name"] for t in detail_data["types"]]
            formatted_id = str(pokemon_id).zfill(3)
            image_url = f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{formatted_id}.png"
            return {
                "id": pokemon_id,
                "name": name,
                "types": types,
                "image_url": image_url
            }
