"""
DESCRIPTION:
Search for a song by entering the title. The program returns the song title and
artist name and also gives the user an option of would they like to see the lyrics
to the song as well.
AUTHORS: Aidan Pearce

LAST UPDATE:

Class Variables: 
1. genius_access_token -> str(allows access to genius API)
2. genius_object -> instantiation of genius object which allows access
to methods of the genius API.

Functions: 
1. search()
2. getTitle()
3. showLyrics()
3. __str__()

"""
# imported libraries
import lyricsgenius as lg
from searchBox import SearchBox


class TitleSearchBox(SearchBox):

    genius_access_token = "_rDAy259SoA7baRL1ouy2MWdOADsdevMvTvMxo83XXtJJ-ejmfSNvtZSrbqJZrvZ"
    genius_object = lg.Genius(genius_access_token)

    def __init__(self, title: str) -> None:
        self.title = title
        self.songObj = None

    def search(self):
        """Description: This function creates a song object from the title entered by the user."""
        try:
            self.songObj = self.genius_object.search_song(self.title)
        except:
            print("Something went wrong. Try again or try searching for a different song.")
        

    def getTitle(self):
        """Description: Prints out the title and artist name for the title entered by the user"""
        print(f"The song title you searched for is " + self.title +
                " \nThe artist is " + self.songObj.artist)
    
    def showLyrics(self):
        """Description: Prints out the lyrics of the song object"""
        print(" \nThe lyrics are:\n " + self.songObj.lyrics)
    

    # override
    def __str__(self):
        print(f"This is the title search box and the song you are searching for is " + self.title)
