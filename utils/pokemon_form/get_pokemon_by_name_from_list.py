from services.pokemon_form import get_all_pokemons_form

class TrieNode:
    def __init__(self):
        self.children = {}
        self.pokemons = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, pokemon_name, pokemon_data):
        node = self.root
        for char in pokemon_name:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.pokemons.append(pokemon_data)  # Lưu Pokémon vào các nút có từ khóa trùng

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []  # Không tìm thấy prefix
            node = node.children[char]
        return self._collect_pokemons(node)

    def _collect_pokemons(self, node):
        pokemons = node.pokemons.copy()
        for child in node.children.values():
            pokemons.extend(self._collect_pokemons(child))
        return pokemons

async def get_pokemon_by_name_from_list(pokemon_name):
    # Lấy danh sách tất cả Pokémon
    pokemons = await get_all_pokemons_form()

    # Khởi tạo Trie
    trie = Trie()

    # Tiền xử lý: Thêm tất cả Pokémon vào Trie
    for pokemon in pokemons:
        if pokemon:
            trie.insert(pokemon['name'].lower(), pokemon)

    # Tìm kiếm Pokémon theo từ khóa (chữ thường)
    matching_pokemons = trie.search(pokemon_name.lower())

    return matching_pokemons
