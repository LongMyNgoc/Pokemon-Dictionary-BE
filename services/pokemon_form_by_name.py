from utils.fetch_pokemon_form.get_pokemon_by_name_from_list import get_pokemon_by_name_from_list

async def get_pokemon_form_by_name(pokemon_name: str):
    pokemons = await get_pokemon_by_name_from_list(pokemon_name)
    return pokemons