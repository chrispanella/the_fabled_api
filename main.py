from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os

app = FastAPI(
    title="Game API",
    description="API for accessing game information",
    version="1.0.0"
)

# Sample game data - you can replace this with your actual game data
game_info = {
    "name": "Your Game Name",
    "version": "1.0.0",
    "description": "A brief description of your game",
    "genres": ["Action", "Adventure"],
    "release_date": "2024-01-01",
    "developer": "Your Name",
    "publisher": "Your Publisher"
}

class GameInfo(BaseModel):
    name: str
    version: str
    description: str
    genres: List[str]
    release_date: str
    developer: str
    publisher: str

@app.get("/")
async def root():
    return {"message": "Welcome to the Game API! Use /game-info to get information about the game."}

@app.get("/game-info", response_model=GameInfo)
async def get_game_info():
    return game_info

@app.get("/game-info/{field}")
async def get_specific_info(field: str):
    if field not in game_info:
        raise HTTPException(status_code=404, detail=f"Field '{field}' not found")
    return {field: game_info[field]}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 