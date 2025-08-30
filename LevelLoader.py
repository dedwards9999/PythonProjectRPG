def load_level(filename):
    with open(filename, "r") as f:
        level = f.read()
    return level