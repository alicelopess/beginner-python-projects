import time

def main():
  countdown_time = int(input("Enter the time in seconds: "))
  countdown(countdown_time)

def countdown(t):
  print('-=' * 15)
  print(f"{t} seconds".upper())
  print('-=' * 15)
  
  while t:
    mins, secs = divmod(t, 60)
    timer = f'{mins:02d}:{secs:02d}'
    print(timer, end='\r')
    t -= 1
    time.sleep(1)
    if not t:
      print('00:00')
  print("Countodown Completed!")
  print('-=' * 15)

def simple_countdown():
  print('-=' * 15)
  countdown_time = int(input("Enter the time in seconds: "))
  print(f"{countdown_time} seconds".upper())
  print('-=' * 15)

  while countdown_time != 0:
    print(f'{countdown_time} seconds left...', end='\r')
    countdown_time -= 1
    time.sleep(1)
  print("Countodown Finalizado!")
  print('-=' * 15)

main()