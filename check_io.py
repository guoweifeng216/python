import os


def say_hi(name, age):
    print ("Hi. My name is %s and I'm %s years old" %(name, age))


def correct_sentence(text):
    tmp = text[-1:]
    print text
    print text.capitalize()
    if text.isupper():
        text = text
    else:
        text = text[0].upper()+text[1:]
    if tmp.endswith('.'):
        text = text
    elif tmp.isalpha():
        text = text + '.'
    else:
        text = text[:-1]
        text = text + '.'
    print text
# say_hi('Alice', 32)

def first_word(text):
    text = text.replace('.', ' ').replace(',', ' ').strip()
    list = text.split()
    print list[0]

def find_string(strings,s):

    for i in range(len(strings)):
        if strings[i] == s:
            print i
# correct_sentence("ddd,abcddef,")
# correct_sentence("ddd,abcdef.")
find_string("welcome to New York",'o')