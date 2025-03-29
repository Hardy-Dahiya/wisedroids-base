import logging
from fastapi import FastAPI
from app.config.settings import Settings
from app.api.routes import router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="WiseDroidAI Agent",
    description="Custom AI Agent API",
    version="1.0.0"
)

# Load settings
settings = Settings()

# Include routes
app.include_router(router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    logger.info("Starting WiseDroidAI Agent...")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down WiseDroidAI Agent...")