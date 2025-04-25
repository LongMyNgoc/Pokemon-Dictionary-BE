# app/main.py

from fastapi import FastAPI
from routes.pokemon import pokemon_router
from core.config import setup_cors

app = FastAPI()
setup_cors(app)

# Đăng ký các route
app.include_router(pokemon_router)

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI PokeAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4000)
