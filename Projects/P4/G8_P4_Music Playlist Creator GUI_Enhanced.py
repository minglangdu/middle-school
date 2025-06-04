## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK
## ENHANCEMENTS NOT FINISHED RECHECK


"""
Project: Music Playlist Creator (GUI)
Student Code
Python Level 3

Student Name: Minglang Du
Class Section: 8-D14

Student Instructions:

Fill in the missing code in this program to complete this GUI version of the
Music Playlist Creator (the console version of which you wrote earlier in the
school year).

Some notes on the GUI vs the console versions:
----------------------------------------------
1. The base GUI version only uses one playlist. (Adding more than one playlist
   is an optional enhancement that requires creating additional widgets.)
2. The GUI version reuses the song library from the console version but
   implements everything else differently.

More details are provided as embedded comments, but in summary, 
you need to fill in most of the code yourself. This includes:
---------------------------------------------------------------
1. Functions to handle events, specifically:
     a. adding a song to the playlist
     b. removing a song from the playlist
     c. (The function to update the song details label is provided.)
2. Creating and placing widgets:
     a. a song library listbox with a scrollbar
     b. a playlist listbox with a scrollbar
     c. heading labels above each of these widgets to identify them
     d. two buttons, one to add a song and another to remove a song
     e. (The code to create and place the song details label is provided.)
3. Binding events
     a. Clicking the "Add Song" button (using its command attribute)
     b. Clicking the "Remove Song" button (using its command attribute)
     c. Selecting a song in the song library listbox (using bind())
     d. Selecting a song in the playlist listbox (using bind())
4. Do basic tests for valid selections to prevent errors. For example, in the
   update_song_details() function, two such conditional checks are done:
     ...
     # If a valid song selection was made, get its index in the listbox:
     if selected_index:
         ...
         # If song title is in library, retrieve and display song details:
         if song_title in song_library:
     ...
   Even though the checks might be redundant if you control how songs are added
   to the listboxes, this kind of "defensive programming" is still a good idea
   to help keep your program robust as it gets larger and more complex. It can
   help protect against crashes due to unexpected behavior as other features
   are added. It also makes it easier for you to debug your program, since you
   are already checking for specific conditions where things could go wrong.
     
GUI Layout
----------
See the screenshot in the project sheet for the GUI layout for both the base
project and a sample enhanced version.

Suggested Enhancements
----------------------
1. Shuffle playlist feature.
     a. Create a "Shuffle Playlist" button.
     b. Create a function to randomize the order of the songs displayed in the
        playlist listbox. Use random.shuffle(<some_list>), which will shuffle
        the order of items in its list argument.
     c. Bind the button to the function.
2. Extend the functionality to multiple playlists.
     a. Create a playlists dictionary to hold all the playlists
           i. Keys = playlist titles
          ii. Values = lists of songs in each playlist
     b. Create a separate listbox to display the playlist titles
           i. Starts off empty; user will create or delete playlists
          ii. Must be synced with the playlists dictionary so that both hold 
              the same playlist titles.
     c. Add an entry field and two buttons:
           i. Entry field to type in a new playlist title.
          ii. "Create Playlist" button - when clicked, should add that playlist
              title to the listbox and the dictionary (with an empty song list,
              since it is a newly created playlist).
         iii. "Delete Playlist" button - when clicked, should delete the
              selected playlist, removing it from the listbox and dictionary.
     d. All other features must be updated to deal with multiple playlists:
           i. The "Add Song" button must now only work when a playlist is
              selected. The button will add the selected song to that playlist.
          ii. The "Remove Song" button must now only work when a playlist is
              selected and a song is selected in that playlist. The button will
              remove the selected song from the selected playlist.
         iii. If you have already implemented the "Shuffle Songs" feature, it
              should only work when a playlist is selected. It should shuffle
              the songs in that playlist only.
3. As before, do basic conditional checks for valid selections before taking
   actions based on those selections.
4. In case the user failed to select a playlist and/or a song for an action,
   display an error message box informing the user of the missing selection.
5. If the user tries to delete a playlist, provide a message box prompting him
   on whether he wishes to proceed (yes/no) even if the playlist may not be
   empty.

Printing and Submission
-----------------------
1. If you have any unresolved errors and debugging print messages at the time 
   of submission, copy-paste them into a string at the end of your code. 
   Otherwise, you should not have any console output to print.
2. Populate your playlist with songs and select a song so that the song details
   label displays the details. Then, using Ctrl+PrtScn (Control + Print Screen),
   take and print a screenshot of your interface.
3. If your GUI does not work or only works partly but still appears on screen,
   take a screenshot of it anyway.
4. Print out your Python script and submit it with the screenshot (if any).
5. In case your teacher needs to test your code, name your script as directed:
   MS3_P5_Music Playlist Creator GUI_[Your User Name].py
   
Grading
-------
1. A line-by-line point breakdown is provided in the comments. You can earn a
   total of 90 points from correct code.
2. The remaining 10 points is earned by a working program, as evidenced by
   your GUI screenshot and verified by teacher testing, as needed.
3. Partial credit on both categories above may be earned by partially working
   code. Earning full credit on code should ensure your program works
   as intended and thus earns the full 10-point working-program credit.
4. All provided point values apply to the base project requirements only.
   Enhancements earn credit at teachers' discretion and can only make up for up
   to 50% of any lost points.
"""

# Fill in the required import statements (2 points):

import tkinter as tk
from tkinter import messagebox

"""
Data Structures
"""

#

pll = {}
displaylist = ""

# Song library is a dictionary of dictionaries.
# Keys are song titles and values are dictionaries with each song's details.
# This code is provided (reused from the non-GUI Music Playlist Creator).
song_library = {
    "Moon Cheese": {
        "Artist": "Galactic Mice",
        "Album": "Space Rats",
        "Year": "2023",
        "Genre": "Electronic",
        "Duration": 300
    },
    "Dance of the Marshmallows": {
        "Artist": "Sugar Symphony",
        "Album": "Candy Orchestra",
        "Year": "2022",
        "Genre": "Classical",
        "Duration": 270
    },
    "The Lonely Broccoli": {
        "Artist": "Veggie Vibes",
        "Album": "Kitchen Jams",
        "Year": "2021",
        "Genre": "Pop",
        "Duration": 210
    },
    "The Mysterious Sock": {
        "Artist": "Laundry Legends",
        "Album": "Washing Tunes",
        "Year": "2024",
        "Genre": "Rock",
        "Duration": 240
    },
    "Under the Bed": {
        "Artist": "Monster Melodies",
        "Album": "Nightmare Notes",
        "Year": "2023",
        "Genre": "Alternative",
        "Duration": 180
    },
    "Pajama Party on Pluto": {
        "Artist": "Starry Siblings",
        "Album": "Planetary Playtime",
        "Year": "2024",
        "Genre": "Dance",
        "Duration": 330
    }
}


"""
Functions for GUI events/interactions
"""

# Function add_song() will add a song from the song library to the playlist.
# (12 points - line-by-line point values in parentheses below)
#
# Triggering event:
#   The user clicks the "Add Song" button. For this to work properly, he must
#   have selected a song in the song library listbox.
#
# Function implementation:
# 1. Use curselection() to get the index of the selected song in the song
#    library. (3)
# 2. Check whether there is a song selection, i.e. whether curselection() 
#    returned a non-zero value. (3)
# 3. Retrieve the song title from the song library listbox using get(). (3)
# 4. Add the selected song title to the playlist listbox. (3)
def add_song():
    ps = ""
    pl = pll_listbox.curselection()
    if (len(pl) != 0):
        ps = pll_listbox.get(pl)
    else:
        return
    ind = song_library_listbox.curselection()
    if (len(ind) != 0):
        title = song_library_listbox.get(ind)
        playlist_listbox.insert(tk.END, title)
        pll[ps].append(title)

# Function remove_song() will remove a song from the playlist.
# (12 points - line-by-line point values in parentheses below)
#
# Triggering event:
#   The user clicks the "Remove Song" button. For this to work properly, he must
#   have selected a song in the playlist songs listbox.
#
# Function implementation:
# 1. Use curselection() to get the index of the selected song in the playlist
#    listbox. (3)
# 2. Check whether there is a song selection, i.e. curselection() returned a
#    non-zero value. (3)
# 3. Remove the selected song from the playlist listbox. (3)
def remove_song():
    ps = ""
    pl = pll_listbox.curselection()
    if (len(pl) != 0):
        ps = pll_listbox.get(pl)
    else:
        return
    if (len(playlist_listbox.curselection()) == 0):
        return
    ind = playlist_listbox.curselection()
    if (len(ind) != 0):
        title = playlist_listbox.get(ind)
        playlist_listbox.delete(ind)
        pll[ps].remove(title)

#

def create_playlist():
    nm = pll_entry.get()
    if (nm == ""):
        return
    try:
        a = pll[nm]
        return
    except:
        pass
    pll[nm] = []
    pll_listbox.insert(tk.END, nm)
    
def remove_playlist():
    pl = pll_listbox.curselection()
    if (len(pl) != 0):
        del pll[pll_listbox.get(pl)]
        pll_listbox.delete(pl)

#

import random
import copy

def shuffle_song():
    ps = ""
    pl = pll_listbox.curselection()
    if (len(pl) != 0):
        ps = pll_listbox.get(pl)
    else:
        return
    songs = []
    while (playlist_listbox.get(0)):
        songs.append(playlist_listbox.get(0))
        playlist_listbox.delete(0)
    random.shuffle(songs)
    pll[ps] = copy.deepcopy(songs)
    p1 = 0
    p2 = len(pll[ps]) - 1
    while (p1 <= p2):
        pll[ps][p1], pll[ps][p2] = pll[ps][p2], pll[ps][p1]
        p1 += 1
        p2 -= 1
    while (len(songs)):
        playlist_listbox.insert(tk.END, songs[len(songs) - 1])
        songs.pop()
        
#

def updisplaylist(event):
    ps = ""
    pl = pll_listbox.curselection()
    if (len(pl) != 0):
        ps = pll_listbox.get(pl)
    else:
        return
    data = ps
    while (playlist_listbox.get(0)):
            playlist_listbox.delete(0)
    if (data in pll.keys()):
        for song in pll[data]:
            playlist_listbox.insert(tk.END, song)
        

#

# Function update_song_details(event) will update the song details listbox to
# display the details of the currently selected song. This function is provided.
#
# Triggering events:
#   The user selects a song in the song library listbox or he selects a song in 
#   the playlist songs listbox.
def update_song_details(event):
    widget = event.widget  # Determine the widget that triggered this event
    # Get the index of the selected song, if any, in that widget:
    selected_song_index = widget.curselection()  
    # If a song selection was made, get its index in the listbox:
    if selected_song_index:
        song_title = widget.get(selected_song_index[0]) 
        # If the song title is in the song library dictionary:
        if song_title in song_library:
            # Retrieve the song details from that dictionary:
            song_details = song_library[song_title]
            # Prepare the text to be displayed, with the song title and each
            # song detail on a separate line:
            details_text = f"{song_title}\n"
            for key, value in song_details.items():
                details_text += f"{key}: {value}\n"
        else:
            details_text = f"{song_title}\nSong details not available."
        # Update the song details label with the prepared text for the song:
        song_details_label.config(text=details_text)


"""
Widget Setup
"""

# Set up the root window (6 points - 3 per item below)
#   1. Initialize the root window
#   2. Title it "Project: Music Playlist Creator"

root = tk.Tk()
root.title("Project: Music Playlist Creator")

# Set up the song library widgets: (12 points - 3 per item below)
#   1. Song library listbox (name this "song_library_listbox" so 
#      that it works with the provided loop to populate it below)
#   2. Song library scrollbar
#   3. Song library title label
#   4. Synchronize listbox and scrollbar scrolling

song_library_listbox = tk.Listbox(root, exportselection = False)

scrollbar = tk.Scrollbar(root)

title_label = tk.Label(root, text = "Song Library")

song_library_listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = song_library_listbox.yview) 



# Initialize the song library in the listbox (provided):
for song in song_library.keys():
    song_library_listbox.insert(tk.END, song)

# The song details widgets are already set up:
#   1. Song details label (with the attribute assignment justify=tk.LEFT to
#      left-justify song details)
#   2. Song details heading label
song_details_label = tk.Label(root, text="", width=25, justify=tk.LEFT)
song_details_heading_label = tk.Label(root, text="Song Details", width=25)

# Set up the playlist widgets (12 points - 3 per item below):
#   1. Playlist songs listbox
#   2. Playlist songs scrollbar
#   3. Playlist name label
#   4. Synchronize listbox and scrollbar scrolling

playlist_listbox = tk.Listbox(root, exportselection = False)

playlist_scrollbar = tk.Scrollbar(root)

playlist_name = tk.Label(root, text="Playlist")

playlist_listbox.config(yscrollcommand = playlist_scrollbar.set)
playlist_scrollbar.config(command = playlist_listbox.yview)

# 

pll_listbox = tk.Listbox(root, exportselection = False)

pll_scrollbar = tk.Scrollbar(root)

pll_name = tk.Label(root, text = "Playlists")

pll_listbox.config(yscrollcommand = pll_scrollbar.set)
pll_scrollbar.config(command = pll_listbox.yview)

pll_entry = tk.Entry(root)

# Set up the "Add Song" and "Remove Song" buttons (6 points - 3 each):

add = tk.Button(root, text = "Add Song", command = add_song)
rem = tk.Button(root, text = "Remove Song", command = remove_song)

#

shf = tk.Button(root, text = "Shuffle Playlist", command = shuffle_song)

#

cre = tk.Button(root, text = "Create Playlist", command = create_playlist)
dte = tk.Button(root, text = "Delete Playlist", command = remove_playlist)

#

"""
Widget Placement on Grid
"""

# Place the song library heading, listbox, and scrollbar (9 points - 3 each):

title_label.grid(row = 0, column = 0)
song_library_listbox.grid(row = 1, column = 0)
scrollbar.grid(row = 1, column = 1, sticky = "NS")

# Place the playlist heading, listbox, and scrollbar (9 points - 3 each):

playlist_listbox.grid(row = 1, column = 5)
playlist_scrollbar.grid(row = 1, column = 6, sticky = "NS")
playlist_name.grid(row = 0, column = 5)

#

pll_listbox.grid(row = 1, column = 2)
pll_scrollbar.grid(row = 1, column = 3, sticky = "NS")
pll_name.grid(row = 0, column = 2)
pll_entry.grid(row = 2, column = 2)

# The song details label and heading placements are provided:
song_details_heading_label.grid(row=0, column=7)
song_details_label.grid(row=1, column=7, rowspan=2, sticky='nsew')

# Place "Add Song" and "Remove Song" buttons (6 points - 3 each)

add.grid(row = 2, column = 0)
rem.grid(row = 2, column = 5)
shf.grid(row = 3, column = 5)
cre.grid(row = 3, column = 2)
dte.grid(row = 4, column = 2)

"""
Event Bindings and Main Loop
"""

# Bind selection event in both listboxes to update details (6 pts - 3 each):

song_library_listbox.bind("<<ListboxSelect>>", update_song_details)
playlist_listbox.bind("<<ListboxSelect>>", update_song_details)
pll_listbox.bind("<<ListboxSelect>>", updisplaylist)

# Start the GUI main event loop (1 point):

root.mainloop()