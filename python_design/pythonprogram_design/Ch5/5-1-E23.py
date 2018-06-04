import os.path

if os.path.isfile("ABC.txt"):
    print("File already exists.")
else:
    infile = open("ABC.txt", 'w')
    infile.write("a\nb\nc\n")
    infile.close()
