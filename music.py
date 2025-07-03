from assistant import AIAssistant
from dataStructure import Response

class MusicAssistant(AIAssistant):

    def __init__(self, userProfile):
        super().__init__(userProfile)
        self.playlists = {
            "pop": ["Blinding Lights -The Weeknd", "As It Was -Harry Styles"],
            "rock": ["Hotel California -Eagles", "Smells Like Teen Spirit -Nirvana"],
            "country": ["This Is How We Roll -Florida Georgia Line", "All My Ex's Live in Texas -George Strait"] 
        }

    def handleRequest(self, request):
        return self.recommendPlaylist(self.user.preferences.get("genre", "pop"))

    def recommendPlaylist(self, genre):
        return f"playing {genre.capitalize()} Genre"
    
    def generateResponse(self, request):
        genre = self.user.preferences.get("genre", "pop")
        playlist = self.playlists.get(genre)
        return Response(f"Here is a playist for your Genre:\n{playlist}")