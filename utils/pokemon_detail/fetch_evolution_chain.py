import httpx

async def fetch_evolution_chain(evolution_chain_url, client):
    """Lấy chuỗi tiến hóa của Pokémon."""
    try:
        # Tăng thời gian timeout lên 10 giây (theo yêu cầu của bạn)
        timeout = httpx.Timeout(10.0)  # 10 giây
        evolution_chain_response = await client.get(evolution_chain_url, timeout=timeout)
        
        if evolution_chain_response.status_code == 200:
            evolution_data = evolution_chain_response.json()
            return evolution_data["evolution_chain"]["url"]
    except httpx.ConnectTimeout:
        print(f"Không thể kết nối tới {evolution_chain_url} trong thời gian quy định.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
    
    return None


async def fetch_evolution_details(evolution_chain_url, client):
    """Lấy chi tiết tiến hóa của Pokémon, bao gồm id, name, types và image_url."""
    evolution_details = []
    
    async def traverse_evolution_chain(current_evolution):
        # Kiểm tra nếu chuỗi tiến hóa có dữ liệu
        if current_evolution:
            # Lấy thông tin Pokémon trong chuỗi tiến hóa
            evolution_pokemon_url = current_evolution["species"]["url"]
            evolution_pokemon_id = evolution_pokemon_url.split("/")[-2]

            # Lấy thông tin chi tiết về Pokémon từ URL của PokeAPI
            evolution_pokemon_response = await client.get(f"https://pokeapi.co/api/v2/pokemon/{evolution_pokemon_id}/")

            if evolution_pokemon_response.status_code == 200:
                evolution_pokemon_data = evolution_pokemon_response.json()
                # Lấy thông tin types và hình ảnh từ PokeAPI
                types = [t["type"]["name"] for t in evolution_pokemon_data["types"]]
                formatted_id = str(evolution_pokemon_id).zfill(3)
                image_url = f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{formatted_id}.png"

                evolution_pokemon = {
                    "id": evolution_pokemon_id,
                    "name": evolution_pokemon_data["name"],
                    "types": types,
                    "image_url": image_url
                }
                evolution_details.append(evolution_pokemon)

            # Tiến hóa tiếp theo (nếu có)
            if current_evolution.get("evolves_to"):
                for next_evolution in current_evolution["evolves_to"]:
                    await traverse_evolution_chain(next_evolution)  # Gọi đệ quy

    # Lấy chuỗi tiến hóa ban đầu
    evolution_response = await client.get(evolution_chain_url)
    if evolution_response.status_code == 200:
        evolution_data = evolution_response.json()
        current_evolution = evolution_data["chain"]
        
        # Bắt đầu đệ quy từ chuỗi tiến hóa đầu tiên
        await traverse_evolution_chain(current_evolution)

    return evolution_details
