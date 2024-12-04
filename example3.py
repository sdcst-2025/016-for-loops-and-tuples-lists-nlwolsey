# The IN operator
# The in operator can be used to check if something matches one of the elements in a list
# Note that it can only find a match, and not if there is something with an inequality.

data = [3,4,5,1,2,3,4,5,6,7,1,2,1,0]

while True:
  print(f"The list contains {data}")
  x = input("Enter a number to look for")
  if x in data:
    print(f"{x} is in the list")
  print("\n\n")
