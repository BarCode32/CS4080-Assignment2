from assistant import AIAssistant
from dataStructure import Response


class StudyAssistant(AIAssistant):
    def __init__(self, userProfile):
        super().__init__(userProfile)
        self.subjects = {
            
        }
    
    def generateResponse(self, request):
        subject = self.user.preferences.get("subject", "Math")
        return Response(f"Lets study start studying {subject}.")