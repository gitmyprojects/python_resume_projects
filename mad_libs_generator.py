import time

# main function to run program will take in user input and place them in story that gets printed at the end.
def main():
    print('''
    Adjective = Description
    Verb = Action
    Noun = Person, Place, or Thing
    ''')
    adj_one = input('Adjective: ')
    adj_two = input('Adjective: ')
    bird = input('Type of bird: ')
    room = input('Room in house: ')
    verb_past = input('Past tense verb: ')
    verb_one = input('Verb: ')
    rel_name = input('Relative\'s name: ')
    noun_one = input('Noun: ')
    liquid = input('A liquid: ')
    verb_ing = input("Verb ending in \'ing': ")
    body_parts = input('Body part - plural: ')
    noun_plural = input('Plural noun: ')
    verb_ing_two = input("Verb ending in \'ing': ")
    noun_two = input('Noun: ')
    print(f"""
It was a {adj_one}, cold October day.
I woke up to the {adj_two} smell of {bird} roasting in the {room}.
I {verb_past} down the stairs to see if I could help {verb_one} the dinner.
My mom said, "See if {rel_name} needs a fresh {noun_one}."
So I carried a tray of glasses full of {liquid} into the {verb_ing} room.
When I got there I couldn't believe my {body_parts}.
There were {noun_plural} {verb_ing_two} on the {noun_two}!
""")






if __name__==('__main__'):
    main()
