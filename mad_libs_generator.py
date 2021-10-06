from _datetime import datetime

# main function to run program will take in user input and place them in story that gets printed at the end.
def main():
    print('''
    Adjective = Description
    Verb = Action
    Noun = Person, Place, or Thing
    ''')
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    # While loops will check if user left input blank
    adj_one = input('Adjective: ')
    while adj_one == '':
        adj_one = input('Field cannot be left blank. Adjective: ')
    adj_two = input('Adjective: ')
    while adj_two == '':
        adj_two = input('Field cannot be left blank. Adjective: ')
    bird = input('Type of bird: ')
    while bird == '':
        bird = input('Field cannot be left blank. Bird: ')
    room = input('Room in house: ')
    while room == '':
        room = input('Field cannot be left blank. Room: ')
    verb_past = input('Past tense verb: ')
    while verb_past == '':
        verb_past = input('Field cannot be left blank. Past tense verb: ')
    verb_one = input('Verb: ')
    while verb_one == '':
        verb_one = input('Field cannot be left blank. Verb: ')
    rel_name = input('Relative\'s name: ')
    while rel_name == '':
        rel_name = input('Field cannot be left blank. Relative\'s name: ')
    noun_one = input('Noun: ')
    while noun_one == '':
        noun_one = input('Field cannot be left blank. Noun: ')
    liquid = input('A liquid: ')
    while liquid == '':
        liquid = input('Field cannot be left blank. A liquid: ')
    verb_ing = input("Verb ending in \'ing': ")
    while verb_ing == '':
        verb_ing = input('Field cannot be left blank. Verb ending in \'ing: ')
    body_parts = input('Body part - plural: ')
    while body_parts == '':
        body_parts = input('Field cannot be left blank. Body part - plural: ')
    noun_plural = input('Plural noun: ')
    while noun_plural == '':
        noun_plural = input('Field cannot be left blank. Plural Noun: ')
    verb_ing_two = input("Verb ending in \'ing': ")
    while verb_ing == '':
        verb_ing = input('Field cannot be left blank. Verb ending in \'ing: ')
    noun_two = input('Noun: ')
    while noun_two == '':
        noun_two = input('Field cannot be left blank. Noun: ')
    print(f"""
It was a {adj_one}, cold October day. It was {current_time}.
I woke up to the {adj_two} smell of {bird} roasting in the {room}.
I {verb_past} down the stairs to see if I could help {verb_one} the dinner.
My mom said, "See if {rel_name} needs a fresh {noun_one}."
So I carried a tray of glasses full of {liquid} into the {verb_ing} room.
When I got there I couldn't believe my {body_parts}.
There were {noun_plural} {verb_ing_two} on the {noun_two}!
""")






if __name__==('__main__'):
    main()
