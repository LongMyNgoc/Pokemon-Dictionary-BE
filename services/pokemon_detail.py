from utils.http_pokemon_detail import fetch_detail

async def get_pokemon_by_id(pokemon_id: int):
    """
    Lấy thông tin 1 Pokémon theo ID từ PokeAPI.
    """
    # URL cơ bản để lấy thông tin chi tiết về Pokémon theo ID
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"

    # Fetch chi tiết từ hàm fetch_detail
    pokemon = await fetch_detail({"url": url})
    
    return pokemon
