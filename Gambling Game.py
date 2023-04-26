#Imports tkinter and random modules
import tkinter as tk, random

#Initiates Window and defines its dimensions, title, and its ability to be resized
root = tk.Tk()
root.geometry("300x200")
root.title("Slot Machine")
root.resizable(False, False)

#Control Variables
is_odd = list(range(1,10,2))
is_even = list(range(0,10,2))
balance_dict = {0: 100}
wager_dict = {"0": 0}
slots = {0: "A", 1: "B", 2: "C"}

def randint(a):
    #Generates a random number
    r = random.randint(0, a)
    return r

def lose_prompt():
    #Pop up window that displays when user goes bankrupt
    pop = tk.Toplevel(root)
    pop.resizable(False, False)
    pop.geometry("180x30")
    tk.Label(pop, text="Bankrupt!", font=("Arial", 13, "bold")).pack()
    
def slot_game():
    #Main slot game
    number = randint(10)
    if number in is_even:
        status_label.config(text=f"Status: Won!")
        balance_dict[0] += wager_dict["0"]
        balance_label.config(text=f"Balance: {balance_dict[0]}$")
        x = randint(2)
        if balance_dict[0] <= 0:
            lose_prompt()
            reset()
        if x == 1:
            game_label.config(text=f"""
|+[{slots[randint(2)]}]+[{slots[randint(2)]}]+[{slots[randint(2)]}]+|
|>[{slots[0]}]+[{slots[0]}]+[{slots[0]}]<|
|+[{slots[randint(2)]}]+[{slots[randint(2)]}]+[{slots[randint(2)]}]+|
   """)
        elif x == 0:
            game_label.config(text=f"""
|+[{slots[randint(2)]}]+[{slots[randint(2)]}]+[{slots[randint(2)]}]+|
|>[{slots[1]}]+[{slots[1]}]+[{slots[1]}]<|
|+[{slots[randint(2)]}]+[{slots[randint(2)]}]+[{slots[randint(2)]}]+|
   """)
        elif x == 2:
            game_label.config(text=f"""
|+[{slots[randint(2)]}]+[{slots[randint(2)]}]+[{slots[randint(2)]}]+|
|>[{slots[2]}]+[{slots[2]}]+[{slots[2]}]<|
|+[{slots[randint(2)]}]+[{slots[randint(2)]}]+[{slots[randint(2)]}]+|
   """)
    elif number in is_odd:
            balance_dict[0] -= wager_dict["0"]
            balance_label.config(text=f"Balance: {balance_dict[0]}$")
            status_label.config(text=f"Status: Lost")
            game_label.config(text=f"""
|+[{slots[randint(2)]}]+[{slots[randint(1)]}]+[{slots[0]}]+|
|>[{slots[1]}]+[{slots[randint(0)]}]+[{slots[randint(2)]}]<|
|+[{slots[randint(2)]}]+[{slots[1]}]+[{slots[2]}]+|
   """)
            if balance_dict[0] <= 0:
                lose_prompt()
                reset()

def wager():
    #updates wager to current
    wager_dict["0"] = int(wager_entry.get())
    if wager_dict["0"] > balance_dict[0]:
        wager_dict["0"] = 0
    else:
        current_wager_label.config(text=f"Current Bet: {wager_dict['0']}$")

def reset():
    #Resets the game
    balance_dict[0] = 100
    wager_dict["0"] = 0
    current_wager_label.config(text=f"Current Bet: {wager_dict['0']}$")
    balance_label.config(text=f"Balance: {balance_dict[0]}$")
    status_label.config(text="Status: Idle")

game_label = tk.Label(root, text=f"""
|+[{slots[0]}]+[{slots[1]}]+[{slots[2]}]+|
|>[{slots[0]}]+[{slots[1]}]+[{slots[2]}]<|
|+[{slots[0]}]+[{slots[1]}]+[{slots[2]}]+|
   """, font=("Ariel", 15, "bold"))
game_label.place(x=75, y=45)

balance_label = tk.Label(root, text=f"Balance: {balance_dict[0]}$", font=("Ariel", 13, "bold"))
balance_label.place(x=0, y=0)

wager_entry = tk.Entry(root, width=11, font=("Ariel", 11, "bold"), state="normal")
wager_entry.place(x=51, y=26)

wager_label = tk.Label(root, text="Bet: $", font=("Ariel", 13, "bold"))
wager_label.place(x=0, y=24)

wager_button = tk.Button(root, text="Bet", command=wager)
wager_button.place(x=143, y=0)

play_button = tk.Button(root, text="Play", command=slot_game)
play_button.place(x=262, y=170)

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.place(x=220, y=170)

current_wager_label = tk.Label(root, text="Current Bet: $", font=("Ariel", 13, "bold"))
current_wager_label.place(x=140, y=39, anchor="w")

status_label = tk.Label(root, text="Status: Idle", font=("Ariel", 13, "bold"))
status_label.place(x=192, y=10, anchor="w")

root.mainloop()