import random

def play():
  print('-=' * 25)
  while True:
    player = str(input("Make your choice: 'r' for rock, 'p' for paper, 's' for scissors: ".center(50)))
    if 'r' in player or 's' in player or 'p' in player:
      break
  
  computer = random.choice(['r', 'p', 's'])

  winner(player, computer)
  print('-=' * 25)

def winner(computer, player):

  dict = {
    'r': 'Rock',
    's': 'Scissors',
    'p': 'Paper'
  }

  for i in dict:
    if i == computer:
      print(f'Computer: {dict[i]}')
    if i == player:
      print(f'Player: {dict[i]}')

  if player == computer:
    print('>> Tie! <<')
  elif player == 'p' and computer == 'r' or player == 'r' and computer == 's' or player == 's' and computer == 'p':
    print('>> Player won! <<')
  else:
    print('>> Computer won! <<')