def main():
    text_dict=create_dictionary("Textese.txt")
    print("Enter a simple sentence in lowercase lettter without:")
    sentence=input("any punction:")
    print()
    translate(sentence,text_dict)


def create_dictionary(filename):
    infile=open(filename,'r')
    testlist=[line.rstrip() for line in infile]
    infile.close()
    return dict([x.split(',') for x in testlist])


def translate(sentence,tests_dict):
    words=sentence.split()
    for word in words:
        print(tests_dict.get(word,word))

