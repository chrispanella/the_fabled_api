# Game API

This is a simple API that provides information about a game. It's built using FastAPI and provides endpoints to access various game-related information.

## Local Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the API server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## Deployment

This API is configured for deployment on Render.com. Here's how to deploy it:

1. Create a GitHub repository and push your code to it
2. Sign up for a free account at [Render.com](https://render.com)
3. Click "New +" and select "Web Service"
4. Connect your GitHub repository
5. Configure the service:
   - Name: Choose a name for your service
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Plan: Free

Your API will be automatically deployed and available at `https://your-service-name.onrender.com`

## API Endpoints

### 1. Root Endpoint
- **URL**: `/`
- **Method**: GET
- **Description**: Welcome message and basic information about the API

### 2. Get All Game Information
- **URL**: `/game-info`
- **Method**: GET
- **Description**: Returns all available information about the game
- **Response**: Complete game information including name, version, description, genres, release date, developer, and publisher

### 3. Get Specific Game Information
- **URL**: `/game-info/{field}`
- **Method**: GET
- **Description**: Returns specific information about the game
- **Parameters**: 
  - `field`: The specific information you want to retrieve (e.g., name, version, description, genres, release_date, developer, publisher)
- **Response**: The requested specific information

## Example Usage

```bash
# Get all game information
curl http://localhost:8000/game-info

# Get specific information (e.g., game name)
curl http://localhost:8000/game-info/name
```

## API Documentation

Once the server is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc` 