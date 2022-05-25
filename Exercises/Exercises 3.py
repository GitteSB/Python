def print_lyrics():
    print("I'm a lumberjack and I'm okay.")
    print("I sleep all night and I work all day")


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

#print(print_lyrics())
#Exercise 3-2

def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)