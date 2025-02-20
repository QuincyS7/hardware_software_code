def greeting(name):
	print("Hello {}!".format(name), "Welcome to my conversation program that is designed to collect data about your academic background!")
	age = input("First things first, how old are you currently?")
	hs = input("Great! Now, what highschool did you graduate from?")
	cc = input("Great! What college do you currently attend?")
	print("Did you perfer one over the other? Answer Highschool or College")
	decision = input()
	if decision == "Highschool":
		print("Woah, I knew it!")
	elif decision == "College":
		print("A rigorous student you are!")
	else:
		print("I dont have anything to say to that.")
	print("So lets recap what I've learned about you")
	print("You are {} years old".format(age))
	print("You graduated high school from {}".format(hs))
	print("Post graduation, you decided to attend {}".format(cc))
	print("You prefer {}".format(decision), "over any other school")




def main():
	name = input("ENTER STUDENT NAME HERE :")
	greeting(name)
	print("It was a pleasure getting to know you! Until next time!")

if __name__ == "__main__":
	main()
