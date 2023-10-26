import random
from constants import const_list

def pwd_info():
  pwd_dict = {}


  pwd_dict['number'] = int(input('Please, enter the number of passwords: '))
  pwd_dict['lenght'] = int(input('Please, enter the lenght of the password: '))
  pwd_dict['special characters'] = int(input('Please, enter the number of special characters: '))
  pwd_dict['uppercase'] = int(input('Please, enter the number of uppercase characters: '))
  pwd_dict['numbers'] = int(input('Please, enter the number of integers: '))


  return pwd_dict

def generate_pwd(pwd_dict):
  pwds = []

  for i in range(pwd_dict['number']):
    counter = pwd_dict['lenght']
    pwd = []
    for i in range(pwd_dict['special characters']):
      pwd.append(random.choice(const_list[2]))
      counter -= 1
    for i in range(pwd_dict['uppercase']):
      pwd.append(random.choice(const_list[1]))
      counter -= 1
    for i in range(pwd_dict['numbers']):
      pwd.append(random.choice(const_list[3]))
      counter -= 1
    for i in range(counter):
      pwd.append(random.choice(const_list[0]))
      counter -= 1
    random.shuffle(pwd)
    pwd = ''.join(pwd)
    pwds.append(pwd)

  return pwds

def usage(item, subitem=None):
  if item == 0:
  #Tamanho de senha invalido
    print('Usage: Not a valid number!')
    while True:
      q = str(input('Do you want to end the program [Y/N]? '))
      if 'Y' in q or 'y' in q:
        return 'break'
  else:
    pass
  
  if subitem > item:
  #Senha menor do que o número de caracteres
    print('Usage: Not a valid lenght!')
    q = str(input('Do you want to end the program [Y/N]? '))
    if 'Y' in q or 'y' in q:
      print('Ending program...')
      return 'break'
  else:
    pass