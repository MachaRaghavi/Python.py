def traverse_dict(data, level=0):
    for key, value in data.items():
        if isinstance(value, dict):
            print("  " * level + f"{key}:")
            traverse_dict(value, level + 1)
        else:
            print("  " * level + f"{key}: {value}")

data = {
    "a": 1,
    "b": {"c": 2, "d": {"e": 3}},
    "f": 4
}

traverse_dict(data)
