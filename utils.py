def get_input(daynum):
    filename = f"inputs/{str(daynum).zfill(2)}.txt"
    
    with open(filename, "r") as f:
        return f.read()
    
def get_input_lines(daynum):
    return get_input(daynum).split("\n")