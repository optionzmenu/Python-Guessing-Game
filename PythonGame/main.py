from players import Player
answers = ['string','integer','float', 'complex','list','tuple','range',
'dictionary','set','frozenset','boolean','bytes','bytearray','memoryview','nonetype']

question = 'Name a built-in data type in Python\n'

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
    print(question)

    while play:
      play=player1.enterGuess(answers, play)
      play=player2.enterGuess(answers, play)
      
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
       print(question)

       while play:
              play=player1.enterGuess(answers, play)
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