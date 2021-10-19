import sys
import json

# balance

possible_commands = [
  "init", "debit", "credit", "balance"
]

if len(sys.argv) < 2:
  print("not enough arguments. command required. possible commands = init | debit | credit")
  sys.exit(1)

command = sys.argv[1]

if not (command in possible_commands):
  print("incorrect command")
  sys.exit(1)


if command == "init":
  input_name = input("enter name: ")
  data = {
    "name": input_name,
    "bal": 0,
  }
  
  book = open("./book.json", "w")
  json.dump(data, book)
  book.close()
  print("book initialized")



if command == "debit":
  if len(sys.argv) < 3:
    print("not enough argument to debit. amount required")
    sys.exit(1)

  input_amount = int(sys.argv[2])

  data = None
  with open("./book.json") as input:
    data = json.load(input)

  data['bal'] += input_amount

  with open("./book.json", "w") as output:
   json.dump(data, output)

  print("debit done")
  
if command == "balance":
  with open("./book.json", "r") as input:
    data = json.load(input)
    print(data['bal'])  
  