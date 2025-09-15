"""Let’s Say Hello to everyone!"""

def greetings(text=""):
    """Print Hello, <text>!"""
    if isinstance(text, str):
        text = "noble stranger" if not text else text
        print(f"Hello, {text}.")
    else:
        print("Error! It was not a name.")


greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
