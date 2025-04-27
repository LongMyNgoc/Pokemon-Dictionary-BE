import httpx

async def fetch_page_data(url):
    """Hàm bất đồng bộ lấy dữ liệu của một trang"""
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            return {"error": "Failed to fetch Pokémon list"}
        return response.json()