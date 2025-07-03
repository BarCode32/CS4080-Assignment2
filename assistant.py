
class AIAssistant:
    def __init__(self, userProfile):
        self.user = userProfile
    
    def greet(self):
        return f"Hello {self.user.name}, how can I help you?"
    
    def takeRequest(self, request):
        #Currently unused
        #For future plans
        pass

    def giveRespose(self, request):
        #Implemented in subclasses
        print("No output here")
        