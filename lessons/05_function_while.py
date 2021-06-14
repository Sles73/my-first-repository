def get_formatted_name(fname, lname):
    """Return a fill name, nice formate."""
    full_name = f"{fname} {lname}"
    return full_name.title()

while True:
    print("Please tell me your name")
    print("enter q at any time to quit")

    fname= input("First name: ")

    if fname == "q":
        break

    lname= input("Last name: ")

    if lname == "q":
        break

    formatted_name = get_formatted_name(fname, lname)
    print(f"Hello, {formatted_name}!")