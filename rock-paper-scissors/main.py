from uteis import play

def main():
  print('-=' * 25)
  print("Let's play Rock, Paper, Scissors!".center(50))
  
  while True:
    play()
    q = str(input('[Q] to quit | [C] to continue: '))
    if 'Q' in q or 'q' in q:
      print('Thanks for playing! See you next time!')
      break

main()