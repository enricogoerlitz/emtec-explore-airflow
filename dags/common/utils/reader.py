def readfile(path: str) -> str:
    with open(path, "r") as f:
        content = f.read()

    return content
