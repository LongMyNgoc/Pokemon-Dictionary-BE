async def fetch_pokemon_form_details(pokemon_url, client):
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
        image_url = detail_data["sprites"].get("front_default")
        
        # Lấy thông tin bổ sung
        height = detail_data["height"]
        weight = detail_data["weight"]
        species_name = detail_data["species"]["name"]

        # Lấy URL species
        species_url = detail_data["species"]["url"]

        # Gọi API species để lấy thêm thông tin
        species_response = await client.get(species_url)
        description = habitat = shape = growth_rate = None
        capture_rate = base_happiness = None

        if species_response.status_code == 200:
            species_data = species_response.json()

            # Description tiếng Anh
            flavor_text_entries = species_data.get("flavor_text_entries", [])
            flavor_text_entry = next(
                (entry for entry in flavor_text_entries if entry["language"]["name"] == "en"),
                None
            )
            description = flavor_text_entry["flavor_text"].replace('\n', ' ').replace('\f', ' ') if flavor_text_entry else None

            # Habitat
            habitat = species_data["habitat"]["name"] if species_data["habitat"] else None

            # Shape
            shape = species_data["shape"]["name"] if species_data["shape"] else None

            # Growth Rate
            growth_rate = species_data["growth_rate"]["name"] if species_data["growth_rate"] else None

            # Capture Rate
            capture_rate = species_data.get("capture_rate")

            # Base Happiness
            base_happiness = species_data.get("base_happiness")

        # Trả về dữ liệu chi tiết của Pokémon
        return {
            "pokemon_id": pokemon_id,
            "name": name,
            "types": types,
            "image_url": image_url,
            "height": height,
            "weight": weight,
            "species": species_name,
            "species_url": species_url,
            "description": description,
            "habitat": habitat,
            "shape": shape,
            "growth_rate": growth_rate,
            "capture_rate": capture_rate,
            "base_happiness": base_happiness,
            "abilities": abilities,
            "stats": stats,
            "moves": moves,
        }
    return None