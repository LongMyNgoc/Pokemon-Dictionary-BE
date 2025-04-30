# /utils/http_utils.py
import aiohttp

async def fetch_data(url: str) -> dict:
    """Hàm fetch dữ liệu từ một URL với aiohttp."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return {"error": f"Failed to fetch data from {url}"}
            return await response.json()

async def get_move_details(move_name: str) -> dict:
    """Lấy thông tin chi tiết về move từ PokeAPI."""
    move_url = f"https://pokeapi.co/api/v2/move/{move_name}"
    return await fetch_data(move_url)

async def get_pokemon_data(pokemon_id: int) -> dict:
    """Lấy thông tin về Pokémon từ PokeAPI."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    return await fetch_data(url)
