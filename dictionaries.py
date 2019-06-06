Nomad = {'type': 'rover', 'color':'black', 'processor':'Jetson TX1'}
print(Nomad['type'])

BARB = {'type':'test-bed', 'color':'black', 'type':'wheeled'}
print(BARB)

myRobots = {'BARB':'WIP','Nomad':Nomad,'Llamabot':'WIP'}
print(myRobots)

myRobots['Llamabot'] = 'Getting to it'
print(myRobots)

del myRobots['Llamabot']
print(myRobots)

workingRobots = myRobots.copy()
print(workingRobots)

otherRobots = {'Rasbot-pi': 'Pi-bot from book', 'spiderbot':'broken'}
myRobots.update(otherRobots)
print(myRobots)

robots = ["nomad", "Ponginator", "Alfred"]
print(robots)

myRobot = robots[0]
print(myRobot)

myRobot = myRobot.capitalize()
print(myRobot)


for robot in robots:
	if robot == "nomad":
		print("This is Nomad")
	else:
		print(robot + " is not Nomad")


myRobot = "Nomad"
a=(myRobot == "Ponginator")
b=(myRobot == "Nomad")

print(a)
print(b)


for robot in robots:
	if robot == "Ponginator" or robot == "Alfred":
		print("These aren't the droids I'm looking for.")



for robot in robots:
	print(robot)		

for name, data in Nomad.items():
	print(name + ': ' + data)


for num, robot in enumerate(robots):
	print(num, robot)

count = 1
while count < 5:
	print(count)
	count = count+1


