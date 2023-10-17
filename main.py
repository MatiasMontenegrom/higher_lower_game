from art import logo,vs
from game_data import data
import random

a=""
b=""
winning=True
score=0
election=0

print(logo)

def random_selection(data):
     return random.choice(data)

a=random.choice(data)
a_follower=a["follower_count"]

b=random.choice(data)
b_follower=b["follower_count"]

while winning:
     print(f"Your score is {score}")
     print("------------------------------------------")
     print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
     print(vs)
     print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
     election=input("Who has more followers? Type 'A' or 'B': ").lower()

     if election=="a" and a_follower>b_follower:
          print(f"You win! {a['name']} has more followers")
          a=b
          a_follower=b_follower
          b=random.choice(data)
          b_follower=b["follower_count"]
          score+=1
     elif election=="b" and b_follower>a_follower:
          print(f"You win! {b['name']} has more followers")
          a=b
          a_follower=b_follower
          b=random.choice(data)
          b_follower=b["follower_count"]
          score+=1
     else:
          print(f"You lose! {a['name']} has more followers")
          winning=False
          print(f"Your final score is: {score}")
     
          
     
     


