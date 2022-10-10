class Player():


  # Create a player
  def __init__(self, player_name):
    self.name = player_name
    self.score = 0
    self.guess = 0
    
  def enterGuess(self,answers,play):
    
    if play == True:
      self.guess = input(self.name + " enter a guess: ").lower()
        
      if self.guess in answers:
        print("Correct Guess!")
        self.score = self.score + 1
        return play
            
      elif self.guess not in answers:
        print("Wrong Guess!")

      elif self.guess == "3":
        play = False