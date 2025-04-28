import httpx

async def fetch_detail(pokemon):
    """Hàm bất đồng bộ lấy chi tiết Pokémon"""
    async with httpx.AsyncClient() as client:
        detail_response = await client.get(pokemon["url"])
        if detail_response.status_code == 200:
            detail_data = detail_response.json()
            
            pokemon_id = detail_data["id"]
            name = detail_data["name"]
            types = [t["type"]["name"] for t in detail_data["types"]]
            
            # Kiểm tra nếu có sprite image (hình ảnh trực tiếp)
            image_url = detail_data["sprites"].get("front_default")  # Hoặc thay bằng "front_shiny", "back_default" tùy theo nhu cầu
            
            return {
                "id": pokemon_id,
                "name": name,
                "types": types,
                "image_url": image_url  # Lấy ảnh từ URL trực tiếp trong sprites
            }
