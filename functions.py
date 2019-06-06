def hello_world():
	message = "Hello World"
	print(message)

hello_world()

def hello_user(first_name, last_name):
	print("Hello " + first_name + " " + last_name + "!")


hello_user("Dara", "Aguilar")

def favorite_thing(favorite = "robotics"):
	print("My favorite thing in the world is "+ favorite)

favorite_thing("pie")	
favorite_thing()


robots = ["nomad", "Ponginator", "Alfred"]

def how_many(list_of_things):
	count = len(list_of_things)
	return count

how_many(robots)

def how_many(list_of_things):
	count = len(list_of_things)
	return count, 1

(x, y) = how_many(robots)

print(x)
print(y)


