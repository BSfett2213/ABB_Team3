from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
import backend.app
# Import routes
from backend.app.routes import upload, daterange, training, simulation
app = FastAPI(
    title="IntelliInspect Backend",
    description="Backend service for dataset handling, training orchestration, and simulation",
    version="1.0.0"
)
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(daterange.router, prefix="/daterange", tags=["Date Range"])
app.include_router(training.router, prefix="/train", tags=["Training"])
app.include_router(simulation.router, prefix="/simulate", tags=["Simulation"])

@app.get("/")
def root():
    return {"message": "IntelliInspect Backend is running"}
