@outputSchema("(profession:chararray, even_odd:chararray)")
def even_odd(id, description):
    id = int(id)
    if (id % 2):
        return description, "even"
    else:
        return description[::-1], "odd"
