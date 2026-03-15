def characterEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "geass": item["geass"],
        "affiliation": item["affiliation"],
        "image":item["image"],
    }

def charactersEntity(entity) -> list:
    return [characterEntity(item) for item in entity]