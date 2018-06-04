def main():
    ## Sort three names.
    pres = [("Lyndon", "Johnson"),("John", "Kennedy"),("Andrew", "Johnson")]
    pres.sort(key=lambda person: person[0])  # sort by first name
    pres.sort(key=lambda person: person[1])  # sort by last name
    for person in pres:
        print(person[1] + ',', person[0])

main()
