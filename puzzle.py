import random as rd
username = ""
level = 0
blank_space = 0
win = False
# shuffled_list = [4,5,6,7,1,3,8,0,2]
winnning_list = [1,2,3,4,5,6,7,8,0]
shuffled_list = winnning_list.copy()
rd.shuffle(shuffled_list)
def calculate_cost(shuffle_list, winnning_list):
	heuristic_cost = 0
	heuristic_cost_index = 0
	for x in shuffle_list:
			if x != blank_space:
				index_x = shuffle_list.index(x) + 1 
				index_y = winnning_list.index(x) + 1
				diff = abs(index_x - index_y)
				heuristic_cost += diff
	return heuristic_cost
	
                       



def play():
	global shuffled_list
	global level
	global win
	print("-------- Level {} --------".format(level))
	show(shuffled_list)
	ways = find_dir(blank_space, shuffled_list)
	print("You can move to: ")
	for x in ways:
		print(" " + x)
	user_choice = input("Enter your choice: ")
	while user_choice not in ways:
		print("This is wrong choice !")
		user_choice = input("Enter your choice: ")
	shuffled_list = move(user_choice, shuffled_list)
	cost = calculate_cost(shuffled_list, winnning_list)
	if cost == 0:
		win = True
	print("Heuristic cost: " + str(cost))
	level += 1

def move(user_choice, lst):
	blank = lst.index(blank_space)
	if user_choice == "up":
		for x in range(3,9):
			if blank == x:
				element = lst[x - 3]
				lst[x - 3] = lst[blank]
				lst[blank] = element
				return lst
	elif user_choice == "right":
		for x in 0,1,3,4,6,7:
			if blank == x:
				element = lst[x + 1]
				lst[x + 1] = lst[blank]
				lst[blank] = element
				return lst
	elif user_choice == "down":
		for x in range(0,6):
			if blank == x:
				element = lst[x + 3]
				lst[x + 3] = lst[blank]
				lst[blank] = element
				return lst
	elif user_choice == "left":
		for x in 1,2,4,5,7,8:
			if blank == x:
				element = lst[x - 1]
				lst[x - 1] = lst[blank]
				lst[blank] = element
				return lst
	else:
		print("Error !")
		pass




def find_dir(blank_space, lst):
	index = lst.index(blank_space)
	dir_list = []
	if index == 0:
		dir_list = ['right', 'down']
	elif index == 1:
		dir_list = ['right','left','down']
	elif index == 2:
		dir_list = ['left','down']
	elif index == 3:
		dir_list = ['right','up','down']
	elif index == 4:
		dir_list = ['right','left','up','down']
	elif index == 5:
		dir_list = ['left','up', 'down']
	elif index == 6:
		dir_list = ['right','up']
	elif index == 7:
		dir_list = ['right', 'left', 'up']
	elif index == 8:
		dir_list = ['left', 'up']
	else:
		print("Error !")
	return dir_list



	



def show(lst):
	print("""
  {}  {}  {}
  {}  {}  {}
  {}  {}  {}

		""".format(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7], lst[8]))


print("Welcome !")
print("This is 8 Puzzle game !")
print("""
Rules
   
   You should move the blocks accordingly in order
   to make it properly organized

   The empty block is shown with {} 
   and you can move {} to up, down, right or left

	 """.format(blank_space, blank_space))
username = input("Enter your username: ")
print("Hello {}, Let's play now !".format(username))
print("This is shuffled blocks !")
show (shuffled_list)
print("This is your goal ")
show(winnning_list)

while win != True:
	play()
else:
	print("Level: " + str(level))
	print("Excellent, {} !".format(username))
	show(shuffled_list)
	print("You won in this game !")


