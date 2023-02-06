import requests
from os import system
import threading
choice = input("[1] profile-counter.glitch.me\n[2] gpvc.arturio.dev\n> ")
system("cls")
username = input("username\n> ")
system("cls")
amount = int(input("amount\n> "))
counter = 0


def profile():
	global username
	r = requests.get(f"https://profile-counter.glitch.me/{username}/count.svg")

def gpvc():
	global username
	r = requests.get(f"https://gpvc.arturio.dev/{username}")

if choice == "1":
	for i in range(amount, 0, -1):
		thread = threading.Thread(target=profile)
		thread.start()
		counter +=1
		system("cls")
		print(f"{counter}/{amount}")
elif choice == "2":
	for i in range(amount, 0, -1):
		thread = threading.Thread(target=gpvc)
		thread.start()
		counter +=1
		system("cls")
		print(f"{counter}/{amount}")	
