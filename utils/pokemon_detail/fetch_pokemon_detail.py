#from utils.fetch_pokemon_form.get_pokemon_by_name_from_list import get_pokemon_by_name_from_list

async def fetch_pokemon_details(pokemon_url, client):
    """Lấy chi tiết thông tin về Pokémon."""
    detail_response = await client.get(pokemon_url)
    if detail_response.status_code == 200:
        detail_data = detail_response.json()
        
        # Lấy các thông tin cơ bản
        pokemon_id = detail_data["id"]
        name = detail_data["name"]
        types = [t["type"]["name"] for t in detail_data["types"]]
        abilities = [a["ability"]["name"] for a in detail_data["abilities"]]
        stats = {stat["stat"]["name"]: stat["base_stat"] for stat in detail_data["stats"]}
        moves = [m["move"]["name"] for m in detail_data["moves"]]
        
        # Lấy thông tin bổ sung
        height = detail_data["height"]
        weight = detail_data["weight"]

        # Lấy URL species
        species_url = detail_data["species"]["url"]

        # Gọi API species để lấy thêm thông tin
        species_response = await client.get(species_url)
        description = None

        if species_response.status_code == 200:
            species_data = species_response.json()

            # Description tiếng Anh
            flavor_text_entries = species_data.get("flavor_text_entries", [])
            flavor_text_entry = next(
                (entry for entry in flavor_text_entries if entry["language"]["name"] == "en"),
                None
            )
            description = flavor_text_entry["flavor_text"].replace('\n', ' ').replace('\f', ' ') if flavor_text_entry else None

        # Trả về dữ liệu chi tiết của Pokémon
        return {
            "pokemon_id": pokemon_id,
            "name": name,
            "types": types,
            "height": height,
            "weight": weight,
            "species_url": species_url,
            "description": description,
            "abilities": abilities,
            "stats": stats,
            "moves": moves,
        }
    return None