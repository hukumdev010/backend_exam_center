from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import init_db
from routes import include_routers
from settings.loader import get_settings

# Load environment variables initially
load_dotenv()

# Database setup


# Get CORS origins for configuration
cors_origins = []


async def get_cors_origins():
    settings = await get_settings()
    default_origins = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://eduneps.com",
        "https://www.eduneps.com",
    ]
    if settings.frontend_url not in default_origins:
        default_origins.append(settings.frontend_url)
    return default_origins


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup - Initialize settings and database
    global cors_origins
    await init_db()
    cors_origins = await get_cors_origins()
    print(f"CORS origins configured: {cors_origins}")
    yield
    # Shutdown - SQLAlchemy handles cleanup automatically


app = FastAPI(
    title="Exam Center API",
    description="FastAPI backend for exam center application",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS middleware - configured with proper origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://eduneps.com",
        "https://www.eduneps.com",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
)

# Include routers
include_routers(app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
