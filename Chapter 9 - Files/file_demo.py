# File Objects

with open("LICENSE.txt", "r") as f:

    size_to_read = 100
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end=" [END LINE] ")
        f_contents = f.read(size_to_read)
