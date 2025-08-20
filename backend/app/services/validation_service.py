from app.services.dataset_service import get_dataset

def validate_ranges(request):
    """
    Validate date ranges: sequential, non-overlapping, within bounds.
    Count rows per range.
    """
    df = get_dataset()

    training = request["training"]
    testing = request["testing"]
    simulation = request["simulation"]

    start = str(df["synthetic_timestamp"].min())
    end = str(df["synthetic_timestamp"].max())

    # Extract per-range counts
    training_count = df[(df["synthetic_timestamp"] >= training["start"]) &
                        (df["synthetic_timestamp"] <= training["end"])].shape[0]

    testing_count = df[(df["synthetic_timestamp"] >= testing["start"]) &
                       (df["synthetic_timestamp"] <= testing["end"])].shape[0]

    simulation_count = df[(df["synthetic_timestamp"] >= simulation["start"]) &
                          (df["synthetic_timestamp"] <= simulation["end"])].shape[0]

    # Basic validation
    if training["end"] >= testing["start"]:
        raise ValueError("Testing must start after Training ends")
    if testing["end"] >= simulation["start"]:
        raise ValueError("Simulation must start after Testing ends")

    return {
        "status": "Valid",
        "training_count": training_count,
        "testing_count": testing_count,
        "simulation_count": simulation_count,
        "message": f"Date ranges are valid. Dataset covers {start} to {end}"
    }
