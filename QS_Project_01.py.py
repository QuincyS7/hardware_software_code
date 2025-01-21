def conversation(name):
	print("Hello!{}".format(name.capitalize()) "Welcome to my conversation program that is designed to collect data about your academic background!")))
	print("First things first, what college do you currently attend?")
	answer = input()
	print("Great! Where did you graduate high school from?")
	answer = input()
	print("Did you perfer one over the other? Answer Highschool or College")
	answer = input().lower().strip()
	if answer == "Highschool":
		print("Woah, I knew it!")
		answer = input
	elif answer == "College":
		print("A rigorous student you are!")
	else:
		print("I dont have anything to say to that.")
	print("\nSo lets recap what I've learned about you, {}".format(name.capitalize()))
	print("You went to high school at {}.")
	Print("Post graduation, you decided to attend {}.")
	Print("You prefer {} over {}"input().lower().strip())


def main():
	name = input("Hello! What is your name?")
	conversation()
	print("It was a pleasure getting to know you! Until next time!")

if __name__ == "__main__":
	main()
