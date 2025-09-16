"""Family Matters"""

def find_the_redheads(family: dict) -> list:
    """Return a list of names of family members with red hair use filter"""
    return list(filter(lambda name: family[name] == "red", family))



dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))