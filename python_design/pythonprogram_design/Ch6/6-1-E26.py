try:
   infile = open("Ages.txt", 'r')  # FileNotFound if fails
   age = int(infile.readline())    # ValueError if fails
   print("Age:", age)
except FileNotFoundError:
   print("File Ages.txt not found.")
except ValueError:
   print("File Ages.txt contains an invalid age.")
   infile.close()
else:
    infile.close()
      







          
