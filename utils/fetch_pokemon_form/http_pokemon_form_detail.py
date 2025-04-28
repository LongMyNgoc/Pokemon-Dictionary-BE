from utils.fetch_pokemon_form.fetch_pokemon_form_detail import fetch_pokemon_form_details
import httpx

async def fetch_detail(pokemon):
    """Hàm chính để lấy chi tiết Pokémon và tiến hóa."""
    async with httpx.AsyncClient() as client:
        # Lấy chi tiết Pokémon
        pokemon_details = await fetch_pokemon_form_details(pokemon["url"], client)
        if pokemon_details:
            pokemon_id = pokemon_details["pokemon_id"]
            name = pokemon_details["name"]
            types = pokemon_details["types"]
            height = pokemon_details["height"]
            weight = pokemon_details["weight"]
            species = pokemon_details["species"]
            description = pokemon_details["description"]
            habitat = pokemon_details["habitat"]
            shape = pokemon_details["shape"]
            growth_rate = pokemon_details["growth_rate"]
            capture_rate = pokemon_details["capture_rate"]
            base_happiness = pokemon_details["base_happiness"]
            abilities = pokemon_details["abilities"]
            stats = pokemon_details["stats"]
            moves = pokemon_details["moves"]
            image_url = pokemon_details["image_url"]

            # Trả về dữ liệu chi tiết
            return {
                "id": pokemon_id,
                "name": name,
                "types": types,
                "image_url": image_url,
                "height": height,
                "weight": weight,
                "species": species,
                "description": description,
                "habitat": habitat,
                "shape": shape,
                "growth_rate": growth_rate,
                "capture_rate": capture_rate,
                "base_happiness": base_happiness,
                "abilities": abilities,
                "stats": stats,
                "moves": moves,
            }
    return None
