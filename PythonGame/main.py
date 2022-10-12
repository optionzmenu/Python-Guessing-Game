from players import Player
q_and_a = (
	{
		"question": "What is the capital of Texas, US? ",
		"answer": ["austin"]
	},
	{
		"question": "What is a built-in data type in Python? ",
		"answer": ['string','integer','float', 'complex','list','tuple','range', 'dictionary','set','frozenset','boolean','bytes','bytearray','memoryview','nonetype']
	},
	{
		"question": "What is a planet in our universe? ",
		"answer": ["mercury", "venus", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]
	}
)

#~~~~~~~           Two Player Game       ~~~~~~~~~~~~~
def twoplayergame():
                      #~~~~~~~~~~~ 2  Players   ~~~~~~~~~~~~~
  print("Player 1")
  player1=Player(input("Enter name: "))

  print("Player 2")
  player2=Player(input("Enter name: "))
  #==========               Play single game function     ============================

  def playGame():
    play = True
    print("\nNew Game Start! (When you're done press 3 to compare scores!)\n")

    for question in q_and_a:
      print(question["question"])
      play=player1.enterGuess(question["answer"], play)
      play=player2.enterGuess(question["answer"], play)
      continue
        
      print("\nScore: "+player1.name+" "+str(player1.score)+" | "+player2.name+" "+str(player2.score))
    
  #=====================       Game play section               ===============================

  quitgame = False
  while quitgame != True:
    try:
      playGame()
      print("Thanks for playing!")
      quitgame = True
    except ValueError:
      print("Wrong input")
      
#~~~~~~~           One Player Game       ~~~~~~~~~~~~~
def oneplayergame():
       player1=Player(input("Enter name: "))
       play = True
       print("\nNew Game Start! (Enter 3 to quit and see your score!)\n")
       
       for question in q_and_a:
              print(question["question"])
              play=player1.enterGuess(question["answer"], play)
              continue
       print("\nScore: "+player1.name+" "+str(player1.score))

#~~~~~~~           Start of the Game       ~~~~~~~~~~~~~
def startgame():
  print("Hello! Welcome to the Python Guessing Game!")

  while True:
    try:
      select = int(input("Would you like to do 1 or 2 players? (3 to quit)"))
      if select == 1:
        oneplayergame()
      elif select == 2:
        twoplayergame()
      elif select == 3:
       quit() 
      else:
        print("Enter a valid choice")
    except ValueError:
      print("Wrong input")

startgame()
