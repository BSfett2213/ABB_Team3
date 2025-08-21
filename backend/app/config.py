# app/config.py
import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # General App Settings
    APP_NAME: str = "IntelliInspect Backend"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Dataset Settings
    UPLOAD_DIR: str = os.getenv("UPLOAD_DIR", "uploads")
    ALLOWED_EXTENSIONS: set = {"csv"}

    # ML Service Settings
    ML_SERVICE_HOST: str = os.getenv("ML_SERVICE_HOST", "127.0.0.1")
    ML_SERVICE_PORT: int = int(os.getenv("ML_SERVICE_PORT", 8001))
    ML_SERVICE_URL: str = f"http://{ML_SERVICE_HOST}:{ML_SERVICE_PORT}"

    # Simulation Settings
    SIMULATION_DELAY: float = 1.0  # seconds between row predictions (for streaming demo)


# Singleton instance you can import anywhere
settings = Settings()
