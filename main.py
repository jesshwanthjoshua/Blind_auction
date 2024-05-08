from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to Secret Auction Program.")
bid_dic = {}
game = True

def high_bid_fun(bid_dic):
  high_bid_name = ""
  high_bid_amount = 0
  for k,v in bid_dic.items():
    v = bid_dic[k]
    if high_bid_amount < v:
      high_bid_name = k
      high_bid_amount = v
  
  print(f"The highest bidder is {high_bid_name}, with an amount of ${high_bid_amount}.")
  print("The other bidders are as follows.")
  print(bid_dic)
  
while game:
  name = input ("What is your name?\n")
  bid_amount = int(input("Enter your bid amount\n$"))
  bid_dic[name] = bid_amount
  
  choice = input("Type 'Y' if there are any more bidders or 'N' if not: ").lower()
  clear()
  
  if choice == 'n':
    game = False
    high_bid_fun(bid_dic)
