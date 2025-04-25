# app/routes/pokemon.py

from fastapi import APIRouter
from services.pokemon_service import get_all_pokemons

pokemon_router = APIRouter()

# Route lấy tất cả Pokémon
@pokemon_router.get("/pokemons")
async def get_pokemons():
    return await get_all_pokemons()

