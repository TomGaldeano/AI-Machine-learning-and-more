def read_file():
    filename="test.txt"
    file = open(filename, "r")
    # Here we have the half a loop to get things started. Reading our first
    # graphics command here lets us determine if the file is empty or not.
    command = file.readline().strip()

    # If the command is empty, then there are no more commands left in the file.
    while command != "":
        #parse lines
        comand = file.readline.strip()