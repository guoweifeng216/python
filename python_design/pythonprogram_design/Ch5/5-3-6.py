import pickle
def main():
    #Display the data for an individual country
    nations=get_dictionary("UNdict.dat")
    continent=input("Enter the name of a contient other than Antarctica:")
    continent_dict=construct_continent_nations(nations,continent)
    display_data(continent_dict)


def get_dictionary(filename):
    infile=open(filename,'rb')
    nations=pickle.load(infile)
    infile.close()
    return nations


def construct_continent_nations(nations,continent):
    # Reduce the full 193 item dictionary to a dictionary consisting
    # solely of the countried in the specified continent
    continent_dict={}
    for nation in nations:
        if nations[nation]['cont']==continent:
            continent_dict[nation]=nations[nation]
    return continent_dict



def display_data(dictionary_name):
    #Display conutries in descending order by population
    continent_list=sorted(dictionary_name.items(),key=lambda k: k[1]['popl'],reverse=True)
    for k in continent_list:
        print(" {0:s}:  {1:,.2f}".format(k[0],k[1]['popl']))


main()
