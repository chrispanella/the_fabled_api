from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict
import os
from datetime import datetime

# Import data from separate files
from data.game_info import game_info
from data.characters import characters
from data.items import items
from data.achievements import achievements
from data.levels import levels
from data.news import news

app = FastAPI(
    title="Game API",
    description="API for accessing game information",
    version="1.0.0"
)

# Add health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

class GameInfo(BaseModel):
    name: str
    version: str
    description: str
    genres: List[str]
    release_date: str
    developer: str
    publisher: str

class Character(BaseModel):
    id: int
    name: str
    class_: str
    level: int
    abilities: List[str]
    description: str

class Item(BaseModel):
    id: int
    name: str
    type: str
    rarity: str
    stats: Dict
    description: str

class Achievement(BaseModel):
    id: int
    name: str
    description: str
    reward: str
    difficulty: str

class Level(BaseModel):
    id: int
    name: str
    description: str
    recommended_level: int
    boss: str
    rewards: List[str]

class News(BaseModel):
    id: int
    title: str
    content: str
    date: str
    type: str

@app.get("/")
async def root():
    return {"message": "Welcome to the Game API! Use /docs to see all available endpoints."}

@app.get("/game-info", response_model=GameInfo)
async def get_game_info():
    return game_info

@app.get("/game-info/{field}")
async def get_specific_info(field: str):
    if field not in game_info:
        raise HTTPException(status_code=404, detail=f"Field '{field}' not found")
    return {field: game_info[field]}

@app.get("/characters", response_model=List[Character])
async def get_characters():
    return characters

@app.get("/characters/{character_id}", response_model=Character)
async def get_character(character_id: int):
    character = next((c for c in characters if c["id"] == character_id), None)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@app.get("/items", response_model=List[Item])
async def get_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = next((i for i in items if i["id"] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.get("/achievements", response_model=List[Achievement])
async def get_achievements():
    return achievements

@app.get("/achievements/{achievement_id}", response_model=Achievement)
async def get_achievement(achievement_id: int):
    achievement = next((a for a in achievements if a["id"] == achievement_id), None)
    if not achievement:
        raise HTTPException(status_code=404, detail="Achievement not found")
    return achievement

@app.get("/levels", response_model=List[Level])
async def get_levels():
    return levels

@app.get("/levels/{level_id}", response_model=Level)
async def get_level(level_id: int):
    level = next((l for l in levels if l["id"] == level_id), None)
    if not level:
        raise HTTPException(status_code=404, detail="Level not found")
    return level

@app.get("/news", response_model=List[News])
async def get_news():
    return news

@app.get("/news/{news_id}", response_model=News)
async def get_news_item(news_id: int):
    news_item = next((n for n in news if n["id"] == news_id), None)
    if not news_item:
        raise HTTPException(status_code=404, detail="News item not found")
    return news_item

@app.get("/news/latest")
async def get_latest_news():
    return sorted(news, key=lambda x: x["date"], reverse=True)[:5]

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 