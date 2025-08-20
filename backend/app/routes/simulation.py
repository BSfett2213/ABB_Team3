from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.schemas.simulation_schema import SimulationRequest
from app.services import simulation_service

router = APIRouter()

@router.post("/")
async def start_simulation(request: SimulationRequest):
    """
    Start real-time prediction simulation.
    Streams row-by-row predictions.
    """
    try:
        generator = simulation_service.run_simulation(request.dict())
        return StreamingResponse(generator, media_type="application/json")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
