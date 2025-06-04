import tkinter as tk
import sys

root = tk.Tk()

root.title('Fish Temple')
root.geometry("400x800")
root.resizable(False, True)
label = tk.Label(root, text = "\n\nFISH FISH FISH FISH FISH\n\n")
label.pack() # resizes window ?

def add_fish():
#    if (check2.cget()):
#        ltext = "FRESHWATER " + ltext
#    if (check.cget()):
#        ltext = "SPICY " + ltext
    ll = tk.Label(root, text = ltext)
    ll.pack()

button = tk.Button(root, text = "ADD FISH", command = add_fish)
button.pack()

tk.Label(root, text = "\n").pack()

anger = 0

def get_fish():
    data = entry.get()
    global anger
    if 'FISH' in data:
        print("You have made a sufficient offering to the FISH.")
        anger -= 5
    else:
        print("WRONG. FISH demands 'FISH'")
        anger += 1
    if (anger >= 3):
        print("YOU HAVE ANGERED THE FISH. BEGONE")
        root.quit()
        sys.exit()

entry = tk.Entry(root)
entry.pack()

offer = tk.Button(root, text = "OFFER FISH", command = get_fish)
offer.pack()

label = tk.Label(root, text = "\n\nOPTIONS\n")
label.pack()

check = tk.Checkbutton(root, text = "SPICY FISH")
check2 = tk.Checkbutton(root, text = "FRESHWATER FISH")
check.pack()
check2.pack()

radio = tk.Radiobutton(root, text = "SMALL FISH", value = 1)
radio2 = tk.Radiobutton(root, text = "LARGE FISH", value = 2)
radio.pack()
radio2.pack()

listb = tk.Listbox(root)
listb.insert(1, "SALMON")
listb.insert(2, "KOI")
listb.pack()

root.mainloop() # needed for it