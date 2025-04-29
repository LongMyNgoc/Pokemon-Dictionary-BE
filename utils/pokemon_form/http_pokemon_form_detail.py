from utils.pokemon_form.fetch_pokemon_form_detail import fetch_pokemon_form_details
from utils.pokemon_detail.fetch_evolution_chain import fetch_evolution_chain, fetch_evolution_details
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
            description = pokemon_details["description"]
            abilities = pokemon_details["abilities"]
            stats = pokemon_details["stats"]
            moves = pokemon_details["moves"]
            image_url = pokemon_details["image_url"]
            
            evolution_chain = await fetch_evolution_chain(pokemon_details["species_url"], client)

            # Lấy thông tin tiến hóa chi tiết
            evolution_details = []
            if evolution_chain:
                evolution_details = await fetch_evolution_details(evolution_chain, client)


            # Trả về dữ liệu chi tiết
            return {
                "id": pokemon_id,
                "name": name,
                "types": types,
                "image_url": image_url,
                "height": height,
                "weight": weight,
                "description": description,
                "evolution_chain": evolution_details,
                "abilities": abilities,
                "stats": stats,
                "moves": moves,
            }
    return None
