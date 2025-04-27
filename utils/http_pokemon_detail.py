import httpx
from utils.fetch_evolution_chain import fetch_evolution_chain, fetch_evolution_details

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
        species = detail_data["species"]["name"]

        # Lấy URL chuỗi tiến hóa
        evolution_chain_url = detail_data["species"]["url"]
        return {
            "pokemon_id": pokemon_id,
            "name": name,
            "types": types,
            "height": height,
            "weight": weight,
            "species": species,
            "evolution_chain_url": evolution_chain_url,
            "abilities": abilities,
            "stats": stats,
            "moves": moves,
        }
    return None

async def fetch_detail(pokemon):
    """Hàm chính để lấy chi tiết Pokémon và tiến hóa."""
    async with httpx.AsyncClient() as client:
        # Lấy chi tiết Pokémon
        pokemon_details = await fetch_pokemon_details(pokemon["url"], client)
        if pokemon_details:
            pokemon_id = pokemon_details["pokemon_id"]
            name = pokemon_details["name"]
            types = pokemon_details["types"]
            height = pokemon_details["height"]
            weight = pokemon_details["weight"]
            species = pokemon_details["species"]
            evolution_chain_url = pokemon_details["evolution_chain_url"]
            abilities = pokemon_details["abilities"]
            stats = pokemon_details["stats"]
            moves = pokemon_details["moves"]

            # Lấy chuỗi tiến hóa
            evolution_chain = await fetch_evolution_chain(evolution_chain_url, client)

            # Lấy thông tin tiến hóa chi tiết
            evolution_details = []
            if evolution_chain:
                evolution_details = await fetch_evolution_details(evolution_chain, client)

            # Định dạng ID và tạo URL ảnh
            formatted_id = str(pokemon_id).zfill(3)
            image_url = f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{formatted_id}.png"

            # Trả về dữ liệu chi tiết
            return {
                "id": pokemon_id,
                "name": name,
                "types": types,
                "image_url": image_url,
                "height": height,
                "weight": weight,
                "species": species,
                "evolution_chain": evolution_details,
                "abilities": abilities,
                "stats": stats,
                "moves": moves,
            }
    return None
