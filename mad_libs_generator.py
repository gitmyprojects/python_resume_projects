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

    adj_one = input('Adjective: ')
    # This will test user input for any numbers
    adj_one_int_test = any(map(str.isdigit, adj_one))

    # While loops will check user input for blanks for numbers
    while adj_one == '' or adj_one_int_test == True:
        adj_one = input('Field cannot be left blank or contain/be a number. Adjective: ')
        adj_one_int_test = any(map(str.isdigit, adj_one))

    adj_two = input('Adjective: ')
    adj_two_int_test = any(map(str.isdigit, adj_two))
    while adj_two == '' or adj_two_int_test == True:
        adj_two = input('Field cannot be left blank or contain/be a number. Adjective: ')
        adj_two_int_test = any(map(str.isdigit, adj_two))

    bird = input('Type of bird: ')
    bird_int_test = any(map(str.isdigit, bird))
    while bird == '' or bird_int_test == True:
        bird = input('Field cannot be left blank or contain/be a number. Bird: ')
        bird_int_test = any(map(str.isdigit, bird))

    room = input('Room in house: ')
    room_int_test = any(map(str.isdigit, room))
    while room == '' or room_int_test == True:
        room = input('Field cannot be left blank or contain/be a number. Room: ')
        room_int_test = any(map(str.isdigit, room))

    verb_past = input('Past tense verb: ')
    verb_past_int_test = any(map(str.isdigit, verb_past))
    while verb_past == '' or verb_past_int_test == True:
        verb_past = input('Field cannot be left blank or contain/be a number. Past tense verb: ')
        verb_past_int_test = any(map(str.isdigit, verb_past))

    verb_one = input('Verb: ')
    verb_one_int_test = any(map(str.isdigit, verb_one))
    while verb_one == '' or verb_one_int_test == True:
        verb_one = input('Field cannot be left blank or be/contain a number. Verb: ')
        verb_one_int_test = any(map(str.isdigit, verb_one))

    rel_name = input('Relative\'s name: ')
    rel_name_int_test = any(map(str.isdigit, rel_name))
    while rel_name == '' or rel_name_int_test == True:
        rel_name = input('Field cannot be left blank or be/contain a number. Relative\'s name: ')
        rel_name_int_test = any(map(str.isdigit, rel_name))

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
