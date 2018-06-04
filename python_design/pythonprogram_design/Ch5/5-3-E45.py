pres = input("Who was the youngest U.S. president? ")
pres = pres.upper()
trResponse = "Correct. He became president at age 42\n" + \
             "when President McKinley was assassinated."
jfkResponse = "Incorrect. He became president at age 43. However,\n" + \
              "he was the youngest person elected president."
responses = {}
responses["THEODORE ROOSEVELT"] = trResponse
responses["TEDDY ROOSEVELT"] = trResponse
responses["JFK"] = jfkResponse
responses["JOHN KENNEDY"] = jfkResponse
responses["JOHN F. KENNEDY"] = jfkResponse
print(responses.get(pres, "Nope.")) 
