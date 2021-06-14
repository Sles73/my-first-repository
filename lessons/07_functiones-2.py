def get_formatted_name(fname, lname):
    """Return a fill name, nice formate."""
    full_name = f"{fname} {lname}"
    return full_name.title()

#print(get_formatted_name("ales", "usagi"))

def build_person(fname, lname):
    """Return a dictionary of  information about a person."""
    person = {"first":fname.title(), "second":lname.title()}
    return person

print(build_person("ales", "usagi"))

