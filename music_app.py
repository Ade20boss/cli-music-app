# Imports the 'music' list from the 'music_file' module.
from music_file import music
# Imports the 'music_logo' string from the 'music_ascii_art' module.
from music_ascii_art import music_logo

# Prints the ASCII art logo for the music player.
print(music_logo)


def print_music_list():
    """
    Prints a list of music tracks with details excluding the first key from each song.

    The function iterates over a list of music dictionaries, skipping the first key
    in each dictionary and printing the remaining key-value pairs.

    :raises KeyError: If an attempt is made to access a non-existent key in a dictionary.
    :raises TypeError: If the input data is not iterable or does not contain
        dictionaries with valid structures.
    """
    # Iterates through each song dictionary in the 'music' list.
    for song in music:
        # Gets the first key of the current song dictionary.
        first_key = next(iter(song))
        # Iterates through the key-value pairs of the current song dictionary.
        for index, music2 in song.items():
            # Checks if the current key is the first key.
            if index == first_key:
                # If it is, skips to the next iteration.
                continue
            # Prints the key and value of the current item.
            print(index, music2)


def get_song():
    """
    Prompts the user to select a song in the format '1:1' and returns the input.

    This function requests user input to select a song using a specific format and
    returns the provided input as a string.

    :return: The song selection entered by the user
    :rtype: str
    """
    # Prompts the user for input and stores it in the 'song' variable.
    song = input("Select a song to play using format 1:1 ")
    # Returns the user's input.
    return song


def determine_song_to_play():
    """
    Determines which song to play based on input format and playlist data.

    This function retrieves user input for a song selection, validates its format,
    and matches the input to a song within the available playlists. It ensures that
    the input adheres to the correct format (e.g., "number:number"), verifies the
    indexes, and attempts to locate the desired song within the corresponding playlist.

    :raises ValueError: If the input contains non-numeric values.
    :raises KeyError: If the song key does not exist in the playlist dictionary.

    :return: A string indicating the result of the song selection process. Possible
        outcomes include:
        - The song name followed by "playing now....." if the song is successfully found.
        - An error message providing details on why the song selection failed (e.g.,
          invalid format, song not found, etc.).
    :rtype: str
    """
    # Calls the 'get_song' function to get user input.
    song = get_song()
    # Initializes an empty dictionary 'song_dict'.
    song_dict = {}
    # Initializes a boolean variable 'check' to False.
    check = False  # Changed to False by default
    # Checks if the user's input contains a ':' and has exactly two parts after splitting.
    if ':' not in song or len(song.split(':')) != 2:
        # If the format is invalid, returns an error message.
        return "Invalid format. Use format like 1:1"

    # Splits the user's input by ':' and stores the parts in 'song_parts'.
    song_parts = song.split(':')
    # Starts a try-except block to handle potential errors.
    try:
        # Converts the first part to an integer for the playlist index.
        playlist_index = int(song_parts[0])
        # Converts the second part to an integer for the song index.
        song_index = int(song_parts[1])
    # Catches a ValueError if the conversion fails (e.g., if the input is not a number).
    except ValueError:
        # Returns an error message if the input contains non-numeric values.
        return "Invalid format. Numbers only."

    # Checks if the playlist index is out of the valid range.
    if playlist_index > len(music) or playlist_index < 1:
        # Returns an error message if the playlist is not found.
        return "Song not found in Playlist"

    # Gets the dictionary for the selected playlist (adjusting for zero-based indexing).
    song_dict = music[playlist_index - 1]

    # Check if the song key exists in the dictionary
    # Checks if the user's full input string (e.g., "1:1") exists as a key in the dictionary.
    if song in song_dict:
        # If the song is found, returns the song name with a "playing now" message.
        return song_dict[song] + " playing now....."
    else:
        # If the song key is not found, returns an error message.
        return "Song not found in Playlist"

def add_song():
    """
    Adds a song to an artist's playlist or creates a new playlist for a new artist.

    If the artist already has an existing playlist, the song is added to their playlist
    with an incremented key. If the artist does not have a playlist, a new one is created
    and the song is added with an appropriate key. The function updates and displays the
    list of all playlists after the song addition.

    :raises ValueError: If input values are invalid or music structure contains unexpected data.
    """
    artist = input("Enter artist name: ")
    song = input("Enter song name: ")
    artist_list = []
    last_key = ""
    for i in music:
        artist_list.append(next(iter(i.values())))
    if artist in artist_list:
        # Loop through all playlists
        for j in music:
            # Check if the artist name (e.g., "Green Day") is one of the values (the first value)
            if artist in j.values():
                # 1. Get the last key (e.g., '1:5')
                last_key = list(j.keys())[-1]
                last_key_parts = last_key.split(":")

                # 2. FIX: Use the split parts and INCREMENT the song number (second part)
                first = int(last_key_parts[0])  # The playlist ID (e.g., 1)
                second = int(last_key_parts[1]) + 1  # The new song ID (e.g., 5 + 1 = 6)

                # 3. Add the new song using the correctly incremented key
                j[str(first) + ":" + str(second)] = artist + " - " + song
                print("\nSong added")

                # 4. FIX: Break the loop since we found the correct playlist
                break  # Exit the 'for j in music' loop
    else:
        new_playlist = {} #Create a new dictionary for a new artist
        new_playlist[len(music) + 1] = artist #Add the title to the playlist
        new_playlist[str(len(music) + 1) + ":" + str(len(new_playlist) + 1)] = artist + " - " + song #Add the new song to the playlist
        music.append(new_playlist) #Then append the new playist to the music file

    print_music_list() #reprint the music list



def main():
    # Starts an infinite loop for continuous song playback and selection.
    while True:
        # Calls the function to display the available songs.
        print_music_list()
        print()
        # Calls the function to handle song selection and prints the result.
        print(determine_song_to_play())

        # Prompts the user for action and waits for input (this is the reliable way).
        choice = input("Press 'c' to change song, 'a' to add a song to playlist or q to quit APP: ").lower().strip()
        print()

        # Checks the choice entered by the user.
        if choice == "c":
            # If 'c' is entered, the loop continues to the next iteration.
            print("\n--- Starting a new song selection ---\n")
            # The next iteration will automatically call print_music_list() and determine_song_to_play() again.
            continue
        # If any other key is pressed, or if the input is empty.

        elif choice == "a":
            add_song()
            stuff = input("Do you want to quit(Y/N): ")
            if stuff.lower() == "y":
                print("\n--- Exiting App ---\n")
                exit()
            else:
                continue
        elif choice == "q":
            # Prints a farewell message before breaking the loop.
            print("\nExiting Music Player. Goodbye!")
            # Breaks out of the 'while True' loop, ending the application.
            exit()



# Calls the 'main' function to start the program.
main()