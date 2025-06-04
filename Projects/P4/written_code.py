"""
Written code - Minglang Du 8-D14

import tkinter as tk
from tkinter import messagebox

def add_song():
    ind = song_library_listbox.curselection()
    if (len(ind) != 0):
        title = song_library_listbox.get(ind)
        playlist_listbox.insert(tk.END, title)
        
def remove_song():
    ind = playlist_listbox.curselection()
    if (len(ind) != 0):
        playlist_listbox.delete(ind)
        
root = tk.Tk()
root.title("Project: Music Playlist Creator")

song_library_listbox = tk.Listbox(root)

scrollbar = tk.Scrollbar(root)

title_label = tk.Label(root, text = "Song Library")

song_library_listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = song_library_listbox.yview)

playlist_listbox = tk.Listbox(root)

playlist_scrollbar = tk.Scrollbar(root)

playlist_name = tk.Label(root, text="Playlist")

playlist_listbox.config(yscrollcommand = playlist_scrollbar.set)
playlist_scrollbar.config(command = playlist_listbox.yview)

add = tk.Button(root, text = "Add Song", command = add_song)
rem = tk.Button(root, text = "Remove Song", command = remove_song)

title_label.grid(row = 0, column = 0)
song_library_listbox.grid(row = 1, column = 0)
scrollbar.grid(row = 1, column = 1, sticky = "NS")

playlist_listbox.grid(row = 1, column = 2)
playlist_scrollbar.grid(row = 1, column = 3, sticky = "NS")
playlist_name.grid(row = 0, column = 2)

song_details_heading_label.grid(row=0, column=4)
song_details_label.grid(row=1, column=4, rowspan=2, sticky='nsew')

add.grid(row = 2, column = 0)
rem.grid(row = 2, column = 2)

song_library_listbox.bind("<<ListboxSelect>>", update_song_details)
playlist_listbox.bind("<<ListboxSelect>>", update_song_details)

root.mainloop()

"""