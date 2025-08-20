from pydantic import BaseModel
from datetime import date

class DateRange(BaseModel):
    start: date
    end: date

class DateRangeRequest(BaseModel):
    training: DateRange
    testing: DateRange
    simulation: DateRange

class DateRangeValidationResponse(BaseModel):
    status: str
    training_count: int
    testing_count: int
    simulation_count: int
    message: str
