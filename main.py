from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import init_db
from routes import include_routers
# Load environment variables initially
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup - Initialize settings and database
    await init_db()
    yield
    # Shutdown - SQLAlchemy handles cleanup automatically



app = FastAPI(
    title="Exam Center API",
    description="FastAPI backend for exam center application",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS middleware - allow all origins for development with ngrok
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,  # Must be False when allow_origins=["*"]
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
)

# Include routers
include_routers(app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
