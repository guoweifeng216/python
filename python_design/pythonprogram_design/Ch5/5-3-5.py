import pickle
def main():
    #Display the data for an individual country
    nations=get_dictionary("UNdict.dat")
    nation=input_name_of_nation(nations)
    display_data(nations,nation)


def get_dictionary(filename):
    infile=open(filename,'rb')
    nations=pickle.load(infile)
    print(nations)
    infile.close()
    return nations


def input_name_of_nation(nations):
    nation=input("Enter the name of a UN member nation:")
    while nation not in nations:
        print("Not member of the UN.Try again")
        nation = input("Enter the name of a UN member nation:")

    return nation


def display_data(nations,nation):
    print("Continent:",nations[nation]['cont'])
    print("Population:",nations[nation]['popl'],"million people")
    print("Area",nations[nation]['area'],"square miles")

main()
