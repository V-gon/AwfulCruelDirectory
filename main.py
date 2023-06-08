import requests

go = True
going = True


def trace(*args):
  pass


print("Learn about a random activity!")


def call():
  URL = "http://www.boredapi.com/api/activity/"
  trace("calling", URL)
  response = requests.get(URL)
  response.raise_for_status()
  data = response.json()
  print("\t-", data["activity"])
  print()
  return data


def choose():
  print(
    "Would you like to choose another activity or learn more about this one?\n"
  )
  choice = input("Enter N for a new activity and M to learn more: ").upper()
  while choice != "N" and choice != "M":
    choice = input("Enter N for a new activity and M to learn more: ").upper()
  return choice


def more(data):
  more = input(
    "Enter T for type, A for accessibility, and P for price: ").upper()
  while more != "A" and more != "T" and more != "P":
    more = input(
      "Enter T for type, A for accessibility, and P for price: ").upper()

  if more == "A":
    print("\tAcessibility -", data["accessibility"])
  elif more == "T":
    print("\tType -", data["type"])
  elif more == "P":
    print("\tPrice -", data["price"])
  print()


while go:
  while going:
    data = call()
    going = False
  choice = choose()
  if choice == "N":
    going = True
  if choice == "M":
    more(data)
