# /services/pokemon_service.py
from utils.pokemon_move.http_pokemon_move import get_pokemon_data, get_move_details

async def get_pokemon_move_by_id(pokemon_id: int):
    """
    Lấy thông tin chi tiết các move có thể học được cho Pokémon theo ID.
    """
    # Lấy dữ liệu của Pokémon
    pokemon_data = await get_pokemon_data(pokemon_id)
    if "error" in pokemon_data:
        return pokemon_data  # Trả về lỗi nếu không tìm thấy Pokémon

    # Lấy danh sách các move có thể học được
    moves = [move['move']['name'] for move in pokemon_data['moves']]

    # Lấy thông tin chi tiết về mỗi move, bao gồm accuracy, power, và type
    move_details = []
    for move in moves:
        move_data = await get_move_details(move)
        if "error" not in move_data:
            move_details.append({
                "move": move,
                "accuracy": move_data.get('accuracy'),
                "power": move_data.get('power'),
                "type": move_data.get('type')  # Fetch thêm type move
            })
        else:
            move_details.append({"move": move, "error": "Move details not found"})

    return move_details  # Trả về chỉ thông tin chi tiết của các move
