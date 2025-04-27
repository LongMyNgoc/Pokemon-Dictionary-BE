from services.pokemon_form import get_all_pokemons_form

async def get_pokemon_by_name_from_list(pokemon_name):
    # Lấy tất cả Pokémon từ get_all_pokemons_form
    pokemons = await get_all_pokemons_form()
    
    # Tạo danh sách chứa các Pokémon thỏa mãn điều kiện
    matching_pokemons = []
    
    # Duyệt qua danh sách Pokémon và kiểm tra tên
    for pokemon in pokemons:
        if pokemon and pokemon_name.lower() in pokemon['name'].lower():  # Kiểm tra nếu tên chứa tên cần tìm
            matching_pokemons.append(pokemon)  # Thêm Pokémon vào danh sách kết quả

    return matching_pokemons  # Trả về danh sách tất cả Pokémon thỏa mãn điều kiện
