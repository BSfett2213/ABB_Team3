import os

def allowed_file(filename: str, extensions={"csv"}) -> bool:
    # check if file is having valid type
    return "." in filename and filename.rsplit(".", 1)[1].lower() in extensions

def save_file(file, path: str) -> str:
    with open(path, "wb") as f:
        f.write(file.file.read())
    return os.path.abspath(path)
