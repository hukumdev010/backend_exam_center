import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import init_db
from routes import include_routers
from settings.loader import get_settings

# Load environment variables
load_dotenv()

print("Environment variables loaded", os.environ.get("GEMINI_API"))

# Database setup


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup - Initialize settings and database
    settings = await get_settings()
    print(f"Starting application in {settings.environment} mode")
    await init_db()
    yield
    # Shutdown - SQLAlchemy handles cleanup automatically


app = FastAPI(
    title="Exam Center API",
    description="FastAPI backend for exam center application",
    version="1.0.0",
    lifespan=lifespan,
)

# Get settings for CORS configuration


async def get_cors_origins():
    settings = await get_settings()
    default_origins = [
        "http://localhost:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001",
    ]
    if settings.frontend_url not in default_origins:
        default_origins.append(settings.frontend_url)
    return default_origins


# CORS middleware - will be configured properly after startup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Will be updated with proper origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
include_routers(app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
