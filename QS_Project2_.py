def questions():
    answer1 = input("Type start to begin")
    if answer1 == 'EXIT':
        return 'EXIT'
    answer2 = input("How are you doing?")
    if answer2 == 'EXIT':
        return 'EXIT'
    name = input("What is your name?")
    if name == 'EXIT':
        return 'EXIT'
    answer3 = input("Where are you from {}".format(name))
    if answer3 == 'EXIT':
        return 'EXIT'
    answer4 = input("What is your favorite song?")
    if answer4 == 'EXIT':
        return 'EXIT'
    answer5 = input("Where did you grow up?")
    if answer5 == 'EXIT':
        return 'EXIT'
    answer6 = input("Who is your favorite celebrity?")
    if answer6 == 'EXIT':
        return 'EXIT'
    return input("How old are you?").lower().strip()

def main():
    print("I am a conversation based program that will ask you question until you type 'EXIT'")
    count = 0
    run_loop = questions()

    while run_loop != 'EXIT':
        questions()
        run_loop = input()

if __name__ == "__main__":
    main()
