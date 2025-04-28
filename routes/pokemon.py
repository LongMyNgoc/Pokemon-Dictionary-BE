# app/routes/pokemon.py

from fastapi import APIRouter, HTTPException
from services.pokemon_list import get_all_pokemons
from services.pokemon_detail import get_pokemon_by_id
from services.pokemon_form import get_all_pokemons_form
from services.get_pokemon_form import get_pokemon_form_by_id

pokemon_router = APIRouter()

# Route lấy tất cả Pokémon
@pokemon_router.get("/pokemons")
async def get_pokemons():
    return await get_all_pokemons()

@pokemon_router.get("/form_pokemons")
async def get_pokemons():
    return await get_all_pokemons_form()

@pokemon_router.get("/pokemon/{pokemon_id}")
async def get_pokemon(pokemon_id: int):
    pokemon = await get_pokemon_by_id(pokemon_id)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

@pokemon_router.get("/pokemon_form/{pokemon_id}")
async def get_pokemon(pokemon_id: int):
    pokemon = await get_pokemon_form_by_id(pokemon_id)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon