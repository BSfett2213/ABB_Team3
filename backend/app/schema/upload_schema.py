from pydantic import BaseModel

class DatasetMetadata(BaseModel):
    total_records: int
    total_columns: int
    pass_rate: float
    start_timestamp: str
    end_timestamp: str

class UploadResponse(BaseModel):
    status: str
    metadata: DatasetMetadata
