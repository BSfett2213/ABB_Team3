from pydantic import BaseModel
from datetime import date

class SimulationRequest(BaseModel):
    simulationStart: date
    simulationEnd: date

#row by row pred results
class SimulationRecord(BaseModel):
    timestamp: str
    sample_id: str
    prediction: str   # "Pass" / "Fail"
    confidence: float
    temperature: float | None = None
    pressure: float | None = None
    humidity: float | None = None
