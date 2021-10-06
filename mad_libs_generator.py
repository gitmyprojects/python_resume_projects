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
    while adj_one == '' or adj_one.isdigit():
        adj_one = input('Field cannot be left blank or a number. Adjective: ')
    adj_two = input('Adjective: ')
    while adj_two == '' or adj_two.isdigit():
        adj_two = input('Field cannot be left blank or a number. Adjective: ')
    bird = input('Type of bird: ')
    while bird == '' or bird.isdigit():
        bird = input('Field cannot be left blank or a number. Bird: ')
    room = input('Room in house: ')
    while room == '' or room.isdigit():
        room = input('Field cannot be left blank or a number. Room: ')
    verb_past = input('Past tense verb: ')
    while verb_past == '' or verb_past.isdigit():
        verb_past = input('Field cannot be left blank or a number. Past tense verb: ')
    verb_one = input('Verb: ')
    while verb_one == '' or verb_one.isdigit():
        verb_one = input('Field cannot be left blank or a number. Verb: ')
    rel_name = input('Relative\'s name: ')
    while rel_name == '' or rel_name.isdigit():
        rel_name = input('Field cannot be left blank or a number. Relative\'s name: ')
    noun_one = input('Noun: ')
    while noun_one == '' or noun_one.isdigit():
        noun_one = input('Field cannot be left blank or a number. Noun: ')
    liquid = input('A liquid: ')
    while liquid == '' or liquid.isdigit():
        liquid = input('Field cannot be left blank or a number. A liquid: ')
    verb_ing = input("Verb ending in \'ing': ")
    while verb_ing == '' or verb_ing.isdigit():
        verb_ing = input('Field cannot be left blank or a number. Verb ending in \'ing: ')
    body_parts = input('Body part - plural: ')
    while body_parts == '' or body_parts.isdigit():
        body_parts = input('Field cannot be left blank or a number. Body part - plural: ')
    noun_plural = input('Plural noun: ')
    while noun_plural == '' or noun_plural.isdigit():
        noun_plural = input('Field cannot be left blank or a number. Plural Noun: ')
    verb_ing_two = input("Verb ending in \'ing': ")
    while verb_ing == '' or verb_ing.isdigit():
        verb_ing = input('Field cannot be left blank or a number. Verb ending in \'ing: ')
    noun_two = input('Noun: ')
    while noun_two == '' or noun_two.isdigit():
        noun_two = input('Field cannot be left blank or a number. Noun: ')
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
