# PyChat 2K17

import random

def start():
    pass

def end():
    pass

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup"]:
            return True
        elif answer in ["n", "no", "nope"]:
            return False
   
def has_keyword(statement, keywords):
    for word in keywords:
        if word in statement:
            return True

    return False
def what_is_name():
    name = input()
    return name

def get_random_response():
    responses = ["Cool!",
                 "Oh, that's interesting",
                 "Do you really think so?",
                 "Fascinating"]
    return random.choice(responses)

def get_response(statement):
    statement = statement.lower()

    hay_words = ["how are you?" , "how are you"]
    family_words = ["mother", "father", "brother", "sister"]
    teacher_words = ["cooper"]
    greeting_words = ["hi", "hello", "hey"]
    goodbye_words = ["bye", "goodbye", "leave"]
    destroy_words = ["rawr", "xd", "lol", "yuh", "lit"]
    fear_words = ["scaring", "scared", "scare", "fear"]
    color_words = ["color"]
    whats_up = ["whats up?", "what is up?", "whats up"]
    food_words = ["food"]
    yourname_words = ["your name"]
    mynameis = ["my name is"]
    
    if has_keyword(statement, family_words):
        response = "Tell me more about your family."
    elif has_keyword(statement, teacher_words):
        response = "I hear Mr. Cooper's class is really fun."
    elif has_keyword(statement, greeting_words):
        response = "Hello!"
    elif has_keyword(statement, goodbye_words):
        response = "No! Do not go! Stay with me!"
    elif has_keyword(statement, food_words):
        response = "My favorite food is electricity. How about you?"
    elif has_keyword(statement, fear_words):
        response = "Do not fear Bipsie! Bipsie is friend!"
    elif has_keyword(statement, whats_up):
        response = "Not much, what about you?"
    elif has_keyword(statement, hay_words):
        response = "I'm doing well, how are you?"
    elif has_keyword(statement, yourname_words):
        response = "My name is Bipsie!"
    elif has_keyword(statement, mynameis):
        response = what_is_name("I did not catch that, what is your name?")
        print("Hi, " + name + "!")
    elif has_keyword(statement, destroy_words):
        response = print("    ██████╗     ███████╗    ███████╗    ████████╗    ██████╗      ██████╗     ██╗   ██╗")
        response = print("    ██╔══██╗    ██╔════╝    ██╔════╝    ╚══██╔══╝    ██╔══██╗    ██╔═══██╗    ╚██╗ ██╔╝")
        response = print("    ██║  ██║    █████╗      ███████╗       ██║       ██████╔╝    ██║   ██║     ╚████╔╝ ")
        response = print("    ██║  ██║    ██╔══╝      ╚════██║       ██║       ██╔══██╗    ██║   ██║      ╚██╔╝  ")
        response = print("    ██████╔╝    ███████╗    ███████║       ██║       ██║  ██║    ╚██████╔╝       ██║   ")
        response = print("    ╚═════╝     ╚══════╝    ╚══════╝       ╚═╝       ╚═╝  ╚═╝     ╚═════╝        ╚═╝   ")
        response = print("                                                                                       ")
        response = print("    ██████╗     ███████╗    ███████╗    ████████╗    ██████╗      ██████╗     ██╗   ██╗")
        response = print("    ██╔══██╗    ██╔════╝    ██╔════╝    ╚══██╔══╝    ██╔══██╗    ██╔═══██╗    ╚██╗ ██╔╝")
        response = print("    ██║  ██║    █████╗      ███████╗       ██║       ██████╔╝    ██║   ██║     ╚████╔╝ ")
        response = print("    ██║  ██║    ██╔══╝      ╚════██║       ██║       ██╔══██╗    ██║   ██║      ╚██╔╝  ")
        response = print("    ██████╔╝    ███████╗    ███████║       ██║       ██║  ██║    ╚██████╔╝       ██║   ")
        response = print("    ╚═════╝     ╚══════╝    ╚══════╝       ╚═╝       ╚═╝  ╚═╝     ╚═════╝        ╚═╝   ")
        response = print("                                                                                       ")
        response = print("    ██████╗     ███████╗    ███████╗    ████████╗    ██████╗      ██████╗     ██╗   ██╗")
        response = print("    ██╔══██╗    ██╔════╝    ██╔════╝    ╚══██╔══╝    ██╔══██╗    ██╔═══██╗    ╚██╗ ██╔╝")
        response = print("    ██║  ██║    █████╗      ███████╗       ██║       ██████╔╝    ██║   ██║     ╚████╔╝ ")
        response = print("    ██║  ██║    ██╔══╝      ╚════██║       ██║       ██╔══██╗    ██║   ██║      ╚██╔╝  ")
        response = print("    ██████╔╝    ███████╗    ███████║       ██║       ██║  ██║    ╚██████╔╝       ██║   ")
        response = print("    ╚═════╝     ╚══════╝    ╚══════╝       ╚═╝       ╚═╝  ╚═╝     ╚═════╝        ╚═╝   ")
        response = print("                                                                                       ")
        response = print("    ██████╗     ███████╗    ███████╗    ████████╗    ██████╗      ██████╗     ██╗   ██╗")
        response = print("    ██╔══██╗    ██╔════╝    ██╔════╝    ╚══██╔══╝    ██╔══██╗    ██╔═══██╗    ╚██╗ ██╔╝")
        response = print("    ██║  ██║    █████╗      ███████╗       ██║       ██████╔╝    ██║   ██║     ╚████╔╝ ")
        response = print("    ██║  ██║    ██╔══╝      ╚════██║       ██║       ██╔══██╗    ██║   ██║      ╚██╔╝  ")
        response = print("    ██████╔╝    ███████╗    ███████║       ██║       ██║  ██║    ╚██████╔╝       ██║   ")
        response = print("    ╚═════╝     ╚══════╝    ╚══════╝       ╚═╝       ╚═╝  ╚═╝     ╚═════╝        ╚═╝   ")


    else:
        response = get_random_response()

    return response

def play():
    talking = True

    print("Hello. I'm ;̵̺͖̠̲̬̮̔̓̂̍͋̐͗̑̆͝͝͝;̷̵̢̛͉̰̩͇̺̤͇̣̳͇̳͖͍̹̠͍̘̹̼̌̄͐̓̄̓̑̋̄͂̎̇̂̓͑̌̎͝.̶̲͈̺̏͛;̷̡̟͓̘̟̠̞̗͖͇͇̔̓͐̄̄̽̔̄́̕,̸̶̨̢͈̠͚̠̹̈̈́̀̄̍̒̃̔͜;̵̖͎̝̬̑̈́̆̿.̱̎̈́͊̽͐̈͜;̷̢̟̮̰̼̩͖̲̋̇̀̌̅͜,̴̾̎̆͗̈́̄̿̈́̒͊͝,̴͙̤͚͆͘.̴̢̻̞̠͚̥̘̿̋̐́̽̀̈̇͛̌̓.")
    print("Say something to me!")

    while talking:
        statement = input(">> ")

        if statement == "Goodbye":
            talking = False
        else:
            response = get_response(statement)
            print(response)

    print("Goodbye. It was nice talking to you.")

start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to chat again?")

end()
