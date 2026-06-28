from itertools import zip_longest

# Open both input files and the output file
with open("fileA.txt", "r") as fileA, \
     open("fileB.txt", "r") as fileB, \
     open("combined.txt", "w") as output:

    linesA = fileA.readlines()
    linesB = fileB.readlines()

    # Merge lines alternately
    for lineA, lineB in zip_longest(linesA, linesB, fillvalue=""):
        if lineA:
            output.write(lineA)
        if lineB:
            output.write(lineB)

print("Files merged successfully into combined.txt")