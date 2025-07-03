from users import UserManager
from music import MusicAssistant
from study import StudyAssistant
from dataStructure import AssistantType, Response, Request
from datetime import datetime
    

def main():

    manager = UserManager()

    print("Welcome!!!\n")
    hasAccount = input("Do you already have an account? (Y/N): ").strip().lower() == 'y'

    if hasAccount:
        print("------Login------")
        while(manager.currentUser == None):
            manager.login()
    else:
        print("\n------Create an account------")
        manager.createAccount()
    
    user = manager.currentUser

    print("\n-----Choose Assitant-----")
    choice = input("Would you like a music or study assistant? ").strip().lower()
    
    while(True):
        match choice:
            case "music":
                genre = input("What genre of music would you like? (rock, pop, or country): ").strip().lower()
                user.preferences = {"genre" :genre}
                assistant = MusicAssistant(user)
                assistantType = AssistantType.MUSIC

                break
                
            case "study":
                #Currently will only print math sinec prototype and hard coded
                genre = input("What subject would you liek to focus on? (Math, Science, English): ").strip().lower()
                user.preferences = {"genre" :genre}
                assistant = StudyAssistant(user)
                assistantType = AssistantType.STUDY
                break

            case _:
                print("Invalid input, try again.")
                print("Please enter [music] or [study].")
                


    request = Request(choice, datetime.now(), assistantType)
    response = assistant.generateResponse(request)
    print(f"\nThe assistant says:\n{response.message}")



    



if __name__ == "__main__":
    main()