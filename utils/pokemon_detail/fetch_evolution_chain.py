import httpx

async def fetch_evolution_chain(evolution_chain_url, client):
    """Lấy chuỗi tiến hóa của Pokémon."""
    try:
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
    """Lấy chi tiết tiến hóa của Pokémon, bao gồm id, name, types, image_url và evolution_conditions."""
    evolution_details = []
    
    async def traverse_evolution_chain(current_evolution, from_pokemon_id=None):
        if current_evolution:
            evolution_pokemon_url = current_evolution["species"]["url"]
            evolution_pokemon_id = evolution_pokemon_url.split("/")[-2]

            # Lấy thông tin chi tiết về Pokémon từ URL
            evolution_pokemon_response = await client.get(f"https://pokeapi.co/api/v2/pokemon/{evolution_pokemon_id}/")

            if evolution_pokemon_response.status_code == 200:
                evolution_pokemon_data = evolution_pokemon_response.json()
                types = [t["type"]["name"] for t in evolution_pokemon_data["types"]]
                formatted_id = str(evolution_pokemon_id).zfill(3)
                image_url = f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{formatted_id}.png"

                # Xử lý cách tiến hóa (nếu có)
                evolution_conditions = []
                if current_evolution.get("evolution_details"):
                    for condition in current_evolution["evolution_details"]:
                        evolution_conditions.append({
                            "trigger": condition.get("trigger", {}).get("name"),
                            "min_level": condition.get("min_level"),
                            "item": condition.get("item", {}).get("name") if condition.get("item") else None,
                            "time_of_day": condition.get("time_of_day"),
                            "location": condition.get("location", {}).get("name") if condition.get("location") else None,
                            "happiness": condition.get("min_happiness"),
                            "beauty": condition.get("min_beauty"),
                            "held_item": condition.get("held_item", {}).get("name") if condition.get("held_item") else None,
                            "known_move": condition.get("known_move", {}).get("name") if condition.get("known_move") else None,
                            "known_move_type": condition.get("known_move_type", {}).get("name") if condition.get("known_move_type") else None,
                        })

                evolution_pokemon = {
                    "id": evolution_pokemon_id,
                    "name": evolution_pokemon_data["name"],
                    "types": types,
                    "image_url": image_url,
                    "evolution_conditions": evolution_conditions,
                    "from_pokemon_id": from_pokemon_id  # Thêm trường để biết tiến hóa từ ai
                }
                evolution_details.append(evolution_pokemon)

            # Đệ quy cho tiến hóa tiếp theo
            if current_evolution.get("evolves_to"):
                for next_evolution in current_evolution["evolves_to"]:
                    await traverse_evolution_chain(next_evolution, from_pokemon_id=evolution_pokemon_id)

    # Bắt đầu lấy chuỗi tiến hóa
    evolution_response = await client.get(evolution_chain_url)
    if evolution_response.status_code == 200:
        evolution_data = evolution_response.json()
        current_evolution = evolution_data["chain"]
        
        await traverse_evolution_chain(current_evolution)

    return evolution_details
