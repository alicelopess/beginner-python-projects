import csv
import sys

def main():

  # TODO: Check for command-line usage
  if len(sys.argv) != 3:
    sys.exit("Usage: python dna.py FILENAME.csv FILENAME.txt")
  if '.csv' not in sys.argv[1] and '.txt' not in sys.argv[2]:
    sys.exit("Usage: python dna.py FILENAME.csv FILENAME.txt")

  # TODO: Read database file into a variable
  database = list()
  with open("smalldb.csv", "r") as arquivo:
    db = csv.DictReader(arquivo)
    for line in db:
      database.append(line)

  print(database)
  
  # TODO: Read DNA sequence file into a variable
  with open("sequence.txt", "r") as arquivo:
    sequence = arquivo.read()
  
  # TODO: Find longest match of each STR in DNA sequence
  subsequence = list()
  for key in database[0].keys():
    if key != 'name':
      subsequence.append(key)

  str_count = dict()
  for item in subsequence:
    str_count[item] = longest_match(sequence, item)
  print(str_count)

  # TODO: Check database for matching profiles
  
  name = ''
  for i in range(len(database)):
    print(i, end=' ')
    count = 0
    match = len(subsequence)
    while count < len(subsequence):
      print(database[i][f'{subsequence[count]}'], end = ' ')
      
      if int(database[i][f'{subsequence[count]}']) == int(str_count[subsequence[count]]):
        match -= 1

      count += 1
    
    print()
    if match == 0:
      name = database[i]["name"]
      print(f'Match! {database[i]["name"]}')
      break
  
  print(name)
  if name == '':
    print('No match')

def longest_match(sequence, subsequence):
  """Returns length of longest run of subsequence in sequence."""

  # Initialize variables
  longest_run = 0
  subsequence_length = len(subsequence)
  sequence_length = len(sequence)

  # Check each character in sequence for most consecutive runs of subsequence
  for i in range(sequence_length):

    # Initialize count of consecutive runs
    count = 0

    # Check for a subsequence match in a "substring" (a subset of characters) within sequence
    # If a match, move substring to next potential match in sequence
    # Continue moving substring and checking for matches until out of consecutive matches
    while True:

      # Adjust substring start and end
      start = i + count * subsequence_length
      end = start + subsequence_length

      # If there is a match in the substring
      if sequence[start:end] == subsequence:
        count += 1
      
      # If there is no match in the substring
      else:
        break
  
    # Update most consecutive matches found
    longest_run = max(longest_run, count)

  # After checking for runs at each character in seqeuence, return longest run found
  return longest_run

main()
