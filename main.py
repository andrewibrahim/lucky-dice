#!/usr/bin/env python3

import random

class Dice:

  def __init__(self, sides):
    self.sides = sides
    self.value = 0
    self.keep = False
    return

  def roll(self):
    if self.keep == False:
      self.value = random.randint(1,self.sides)
      return

  def toggle(self):
    if self.keep == True:
      self.keep = False
    else:
      self.keep = True
  
  def toString(self):
    s = str(self.value)
    if self.keep:
      s = s + "*"
    return s

  def toValue(self):
    return self.value

class Hand:
  def __init__ (self):
    self.dice_count = 2
    self.dice_total = 0
    self.max_rolls = 3
    self.rolls_count = 0
    self.dice = []
    for x in range(self.dice_count):
      self.dice.append(Dice(30))
    return
  
  def roll(self):
    self.dice_total = 0
        
    #self.dice[0].value = 2
    #self.dice[1].value = 1
    #self.dice[2].value = 4
    #self.dice[3].value = 5
    #self.dice[4].value = 3
    
    for x in range(self.dice_count):
      self.dice[x].roll()
      self.dice_total = self.dice_total + self.dice[x].toValue()

    self.dice.sort(key = lambda x: x.value)
    
    self.toString()
    return

  
  def toString(self):
    print("\n")
    for x in range(self.dice_count):
      print('Your Dice ' + str(x + 1) + ' is: ' + self.dice[x].toString() )
    return

  def reset(self):
    for x in range(self.dice_count):
      self.dice[x].keep = False

  def calcTotal(self):
    calcVal = 0
    for x in range(self.dice_count):
      calcVal = calcVal + self.dice[x].toValue()
    return calcVal

  def countValue(self,val):
    countVal = 0
    for x in range(self.dice_count):
      if self.dice[x].toValue() == val:
        countVal = countVal + 1
    return countVal

  
  
  def calcRow(self, row):
    if row == "k":
      return self.calcTotal()
    else:
      return 10000000000


class Player:

  def __init__(self, namePassed):
    #self.total = 100
    self.name = namePassed
    self.hand = Hand()
    self.score = Score()
    self.guess = -1
    
    return

  def addScore(self, s):
    self.total = self.total + s
    return

  def score(self):
    return self.total

  def turn(self):
    print("\nPlayer " + self.name + " turn starting!")
    self.hand.roll_count = 0
    self.hand.reset()
    self.guess = int(input("What is your guess? : "))
    command = "R"
    while (self.hand.roll_count <= self.hand.max_rolls):
      if command == "R" or command == "r":
        if self.hand.roll_count < self.hand.max_rolls:
          self.hand.roll()
          self.hand.roll_count = self.hand.roll_count + 1
        else:
          print("No rolls left.")
      elif command == "1":
        self.hand.dice[0].toggle()
        self.hand.toString()
      elif command == "2":
        self.hand.dice[1].toggle()
        self.hand.toString()
      elif command == "3":
        self.hand.dice[2].toggle()
        self.hand.toString()
      elif command == "4":
        self.hand.dice[3].toggle()
        self.hand.toString()
      elif command == "5":
        self.hand.dice[4].toggle()
        self.hand.toString()
      elif (command in "kK") and len(command) == 1:
        if self.score.setScore(command,abs(self.hand.calcTotal() - self.guess)):
          break
      else:
        print("Please enter a valid input.")
        
      if self.hand.roll_count <= self.hand.max_rolls:
        self.score.toString(self)
        print("You have " + str(self.hand.max_rolls - self.hand.roll_count) + " rolls remaining.")
        command = input('(R)oll or (K)eep: ')

    #self.score.toString(self)
    
class Score:
  def __init__(self):
    self.total_points = 100

  def setScore(self, command, val):
    if command == "k" and self.total_points > 0:
      self.total_points = self.total_points - val
      return True
    else:
      return False

  def calcScore(self, val):
    if val < 0:
      return 0
    else:
      return val
  
  def toString(self, player):
    print("-------------------------------------")
    print("Name      : " + player.name)
    print("Total     : " + str(self.total_points))
    print("Guess     : " + str(player.guess))
    print("Roll      : " + str(player.hand.calcTotal()))
    print("Diffrence : " + str(abs(player.hand.calcTotal() - player.guess)))
    print("New Total : " + str(self.total_points - abs(player.hand.calcTotal() - player.guess)))
    print("-------------------------------------")

def player_scores(players):
  print("\n\nScore")
  print("==================")  
  for player in players:
    print(player.name + " " + str(player.score.total_points))
  print("==================")

def main():
  print("Welcome to the Lucky Dice Game!")

  player_count = int(input("How many people are playing?: "))
  players = []
  for x in range(player_count):
    name_entered = input("Enter player " + str(x + 1) + " name: ")
    players.append(Player(name_entered))

  while True:
    command = input('Enter your command (R)ound or e(X)it: ' )
    if command == "X" or command == "x":
      print("Thanks for playing!")
      break   
    elif command == "R" or command == "r":  
      for z in range(player_count):
        players[z].turn()
        player_scores(players)
    else:
      print("Please enter a valid input.")

if __name__ == "__main__":
  main()