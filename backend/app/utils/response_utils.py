from fastapi.responses import JSONResponse

def success_response(data: dict, status_code: int = 200) -> JSONResponse:
    """
    Standard success response wrapper.
    """
    return JSONResponse(
        status_code=status_code,
        content={"status": "success", "data": data}
    )

def error_response(message: str, status_code: int = 400) -> JSONResponse:
    """
    Standard error response wrapper.
    """
    return JSONResponse(
        status_code=status_code,
        content={"status": "error", "message": message}
    )
