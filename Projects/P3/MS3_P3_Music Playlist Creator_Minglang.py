"""
Project 3: Music Playlist Creator
Student Code: Base Project and Enhancements
Python Level 3
"""

import random

# Song library is a dictionary of dictionaries.
# Keys are song titles and values are dictionaries with each song's details.
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

# Playlists dictionary will hold all playlists.
# Each playlist will be a list of strings (song titles).
#playlists = {'aaa':['Moon Cheese', 'The Mysterious Sock', 'Under the Bed']}
playlists = {}

def print_song_library():
    """ Display the entire song library as a table. """
    
    print("\nSong Library:")
    print("=" * 101)  # Line separator
    
    # Print column headings with field widths (left-justified by default):
    print(f"   {'Title':27} {'Artist':18} {'Album':20} {'Year':6}",
          f"{'Genre':13} Duration")
    print("=" * 101)  # Line separator
    
    # Loop over the songs to print them. First enumerate the songs so that
    # we can display song numbers for easy user selection:
    for i, song_title in enumerate(song_library.keys(), 1):
        # First get the dictionary containing that song's details:
        song_details = song_library[song_title]
        
        # Now, get the song's details from that dictionary:
        artist, album = song_details["Artist"], song_details["Album"]
        year, genre = song_details["Year"], song_details["Genre"]
        duration = song_details["Duration"]  # whole number of seconds
        
        # Calculate minutes and seconds using integer division and remainder:
        minutes, seconds = duration // 60, duration % 60
        
        # Output that song's details using their columns' field widths:
        print(f"{i:<2} {song_title:27} {artist:18} {album:20}",
              f"{year:6} {genre:13} {minutes:2}:{seconds:02}")


def print_playlists():
    """ Display all playlists with song titles, artists, and durations. """
    
    print("\nPlaylists:")
    
    # Loop over the playlists to print them. First enumerate the playlists
    # so that we can display playlist numbers for easy user selection:
    for i, playlist_name in enumerate(playlists, 1):
        print(f"\n{i}. {playlist_name}:")
        print("-"*60)  # Line separator
        
        # Print column headings for the playlist with field widths:
        print(f"   {'Title':27} {'Artist':18} Duration")
        print("-"*60)
        
        # Call print_playlist() to print the current playlist:
        print_playlist(playlist_name)


def print_playlist(playlist_name):
    """ STUDENT CODE REQUIREMENT:
        Print the given playlist with song titles, artists, and durations.

        > Display this as a 2-D table with columns for each of those fields.
          The song details should line up with the column headings printed by
          the print_playlists() function.
          
        > Number each song, starting with 1. Use enumerate() on the playlist, 
          or manually increment a variable for the song number as you iterate
          over the playlist's songs.
          
        > Output the duration of each song in mm:ss format.
          
        > Add up the duration of all the songs and output the total duration
          in mm:ss format, algined with the individual song durations.

        > The print_song_library() and print_playlists() functions should
          give you some clues on how to approach this function.
    """
    import math
    number = 1 # the number of the song
    total = 0# total duration
    for s in playlists[playlist_name]:
        song = song_library[s]
        minute = math.floor(song['Duration'] / 60)
        second = song['Duration'] - int(minute) * 60
        # 'ljust' adjusts the values to fit the headers
        print(str(number) + '. ' + s.ljust(27) + song['Artist'].ljust(18 )
              + f"{minute:2}:{second:02}")
        total += song['Duration']
        number += 1
    print('-' * 60)
    minute = math.floor(total / 60)
    second = total - int(minute) * 60
    print("Total Duration" + " " * 34
          + f"{minute:2}:{second:02}")

def create_playlist():
    """ STUDENT CODE REQUIREMENT:
        Create a new playlist with a user-inputted name.
        
        > Display all the current playlists before prompting the user for
          the name of the new playlist.
        
        > If the user-inputted playlist name already exists, let the user
          know and do nothing.
          
        > Otherwise, create the new playlist as an empty list in the playlists
          dictionary.
    """
    print_playlists()
    name = input("Select your playlist name: ") # input function
    if (name in playlists):
        print("Name taken. Try again next time.")
        return
    playlists[name] = [] # initialize as empty list


def add_song_to_playlist():
    """Prompt user to add a song to a chosen playlist"""
    
    print_playlists()
    playlist_num = int(input("\nChoose a playlist number: "))
    
    # Convert the playlist keys view object to a list and then retrieve the
    # playlist name in the list using the user-selected playlist number:
    playlist_names = list(playlists.keys())
    playlist_name = playlist_names[playlist_num - 1]
    
    print_song_library()
    song_num = int(input("\nChoose a song number to add: "))
    
    # Get the song title by converting the song library keys view object to a
    # list and then finding the string at the chosen song number:
    song_titles = list(song_library.keys())
    song_title = song_titles[song_num - 1]
    
    # Get the playlist from the dictionary of playlists and add the song to it:
    playlist = playlists[playlist_name]
    playlist.append(song_title)
    
    print(f"Song '{song_title}' added to playlist '{playlist_name}'!")


def remove_song_from_playlist():
    """ STUDENT CODE REQUIREMENT:
        Prompt user to remove a song from a chosen playlist.
        
        > Display all the current playlists using print_playlists() before 
          prompting the user for the playlist to remove a song from.
          
        > After the user selects that playlist, prompt the user for the song
          to remove.
          
        > Since playlists and songs are numbered, prompts should be for those
          numbers so that the user doesn't have to type out names/titles.
          
        > If the chosen playlist is empty, inform the user and exit the
          function since there are no songs to remove from it.
    
        > Inform the user once a song is removed. State the playlist name
          and the title of the removed song.

        > The add_song_to_playlist() function should give you some clues on
          how to approach this function.
    """
    print_playlists()
    while 1: # stops users from picking an error
        try:
            num = int(input("Choose the playlist number: "))
            key = list(playlists.keys())[num - 1] # the name of the playlist
            if (len(playlists[key]) == 0):
                print("No songs to remove: empty playlist.")
                break
            song = int(input("Choose the song number: "))
            print(f"Song '{playlists[key][song - 1]}' from playlist '{key}' was removed.")
            del playlists[key][song - 1] # deletes
            break
        except:
            print("Invalid.")


def shuffle_playlist():
    """ OPTIONAL ENHANCEMENT:
        Shuffle the songs in a chosen playlist
        
        > Display all the playlists and prompt the user for the number of
          the playlist to shuffle.
          
        > Shuffle the given playlist using random.shuffle(), which accepts
          a single list (or any mutable sequence) as an argument.

    """
    print("\n *** OPTIONAL ENHANCEMENT: Playlist Shuffle ***\n")
    print("This is currently just a stub.")


def search_songs():
    """ OPTIONAL ENHANCEMENT:
        Search for songs by any of their details.
        
        > Prompt the user for a search term and search each song detail
          (including the song title) to see if it contains the search term
          as a substring (e.g., 'dance' is found as part of a song title
          and as a genre).
          
        > Display every matched song along with all its song details.  
    """
    print("\n *** OPTIONAL ENHANCEMENT: Song Search ***\n")
    print("This is currently just a stub.")
    

def main():
    """ Present the main menu of choices in a loop, prompting the user to
        select the next playlist operation. """
    
    print("\nWelcome to the Music Playlist Creator!")
    print("Please choose one of the following options at a time.")
    
    while True:
        print("\nMain Menu:")
        print("----------------------------")
        print("1. Display Song Library")
        print("2. Display Playlists")
        print("3. Create Playlist")
        print("4. Add Song to Playlist")
        print("5. Remove Song from Playlist")
        print("6. Shuffle Playlist")
        print("7. Search Songs")
        print("8. Quit")
        print("----------------------------")
        choice = input("Choose an option (1-8): ")
        if choice == "1":
            print_song_library()
        elif choice == "2":
            print_playlists()
        elif choice == "3":
            create_playlist()
        elif choice == "4":
            add_song_to_playlist()
        elif choice == "5":
            remove_song_from_playlist()
        elif choice == "6":
            shuffle_playlist()
        elif choice == "7":
            search_songs()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()