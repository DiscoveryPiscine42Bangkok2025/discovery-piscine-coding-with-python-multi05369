"""Organize this list of names for me!"""

def array_of_names(persons: dict) -> list:
    """Convert a dictionary of persons to a list of "First Last" strings first be capitalizing the first and last names."""
    return [f"{first_name.capitalize()} {last_name.capitalize()}" for first_name, last_name in persons.items()]


persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))
