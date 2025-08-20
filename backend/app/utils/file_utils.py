import os

def allowed_file(filename: str, extensions={"csv"}) -> bool:
    """
    Check if uploaded file has an allowed extension.
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in extensions

def save_file(file, path: str) -> str:
    """
    Save uploaded file to given path.
    """
    with open(path, "wb") as f:
        f.write(file.file.read())
    return os.path.abspath(path)
