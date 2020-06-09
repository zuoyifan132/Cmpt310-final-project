#a5
import random



def graph(l):
	for i in range(3):
		print (l[i], end = " ")
	print ()
	for i in range(3,6):
		print (l[i], end = " ")
	print ()
	for i in range(6,9):
		print (l[i], end = " ") 
	print ()

def computer_win(l):
	if (l[0]=="x") & (l[1]=="x") & (l[2]=="x"):
		return True
	elif (l[3]=="x") & (l[4]=="x") & (l[5]=="x"):
		return True
	elif (l[6]=="x") & (l[7]=="x") & (l[8]=="x"):
		return True
	elif (l[0]=="x") & (l[3]=="x") & (l[6]=="x"):
		return True
	elif (l[1]=="x") & (l[4]=="x") & (l[7]=="x"):
		return True
	elif (l[2]=="x") & (l[5]=="x") & (l[8]=="x"):
		return True
	elif (l[0]=="x") & (l[4]=="x") & (l[8]=="x"):
		return True
	elif (l[2]=="x") & (l[4]=="x") & (l[6]=="x"):
		return True
	else:
		return False

def player_win(l):
	if (l[0]=="o") & (l[1]=="o") & (l[2]=="o"):
		return True
	elif (l[3]=="o") & (l[4]=="o") & (l[5]=="o"):
		return True
	elif (l[6]=="o") & (l[7]=="o") & (l[8]=="o"):
		return True
	elif (l[0]=="o") & (l[3]=="o") & (l[6]=="o"):
		return True
	elif (l[1]=="o") & (l[4]=="o") & (l[7]=="o"):
		return True
	elif (l[2]=="o") & (l[5]=="o") & (l[8]=="o"):
		return True
	elif (l[0]=="o") & (l[4]=="o") & (l[8]=="o"):
		return True
	elif (l[2]=="o") & (l[4]=="o") & (l[6]=="o"):
		return True
	else:
		return False

def draw(l):
	if (player_win(l) == False) & (computer_win(l) == False):
		count = 0
		for i in range(9):
			if (l[i] == "x") or (l[i] == "o"):
				count += 1
		if count == 9:
			return True
		
	else:
		return False

def end_game(l):
	if player_win(l) == True:
		return True
	elif computer_win(l) == True:
		return True
	elif draw(l):
		return True
	else:
		return False

def player_end_game(l):
	if player_win(l) == True:
		print ("Win")
		return True
	elif computer_win(l) == True:
		print ("Lose")
		return True
	elif draw(l):
		print ("Draw")
		return True
	else:
		return False

def player_enter(l,n):
	n = int(n)
	if (n > 8) or (n < 0):
		print ("input not valid please try again")
		return False
	elif (l[n] == "x") or (l[n] == "o"):
		print ("input not valid please try again")
		return False
	else:
		return True

def rand_playout(l, computer_choice, choice):
	l_2 = []
	computer_choice_2 = []

	for i in range(9):
		l_2.append(l[i])

	l_2[choice] = "x"

	for i in range(len(computer_choice)):
		computer_choice_2.append(computer_choice[i])

	computer_choice_2.remove(choice)

	if computer_win(l_2) == True:
		return 2

	if draw(l_2) == True:
		return 1

	if player_win(l_2) == True:
		return -1

	count_win = 0
	while(end_game(l_2) == False):
		#choose random to "o"
		fill = computer_choice_2[random.randint(0,len(computer_choice_2)-1)]
		l_2[fill] = "o"
		computer_choice_2.remove(fill)

		#check if after fill in "o" the game end
		if end_game(l_2) == True:
			if player_win(l_2) == True:
				count_win = -1
			elif draw(l_2) == True:
				count_win = 1
			break

		#choose random to "x"
		fill = computer_choice_2[random.randint(0,len(computer_choice_2)-1)]
		l_2[fill] = "x"
		computer_choice_2.remove(fill)

		#check if after fill in "x" the game end
		if end_game(l_2) == True:
			if computer_win(l_2) == True:
				count_win = 2
			elif draw(l_2) == True:
				count_win = 1
			break
	return count_win

def pMCTS(l):
	computer_choice = []
	# list all computer choice
	for i in range(9):
		if (l[i] != "x") and (l[i] != "o"):
			computer_choice.append(int(l[i]))

	#make a dictionary to store the number of win of randon playout
	dic = {}
	for i in range(len(computer_choice)):
		dic[computer_choice[i]] = 0

	count_win = 0
	number_random_playout = 200
	for i in range(len(computer_choice)):
		for j in range(number_random_playout):
			count_win += rand_playout(l, computer_choice, computer_choice[i])
		dic[computer_choice[i]] = count_win
		count_win = 0

	print (dic)
	#find max in the dictionary value
	value = []
	for i in range(len(dic)):
		value.append(dic[computer_choice[i]])
	maximum_value = max(value)
	for i in range(len(computer_choice)):
		if maximum_value == dic[computer_choice[i]]:
			return computer_choice[i]

def play_a_new_game():
	# computer "x" player "o"
	#player first 
	print ()
	print ("Player first: (computer: x player: o)")
	print ()
	l = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
	graph(l)
	while(True):
	
		#player enter
		player_value = 0
		while(True):
			n = input("Enter integer from the graph:")
			if player_enter(l,n) == True:
				player_value = int(n)
				break

		#change chessboard
		l[player_value] = "o"

		graph(l)

		if player_end_game(l) == True:
			break
	

		#computer enter
		computer_value = pMCTS(l)
		l[computer_value] = "x"

		graph(l)

		if player_end_game(l) == True:
			break


	#computer first
	print ()
	print ("Computer first: (computer: x player: o)")
	print ()
	l = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

	while(True):

		#computer enter
		computer_value = pMCTS(l)
		l[computer_value] = "x"

		graph(l)

		if player_end_game(l) == True:
			break
	
		#player enter
			player_value = 0
		while(True):
			n = input("Enter:")
			if player_enter(l,n) == True:
				player_value = int(n)
				break

		#change chessboard
		l[player_value] = "o"

		graph(l)

		if player_end_game(l) == True:
			break


#main
if __name__ == '__main__':
  play_a_new_game()


	





