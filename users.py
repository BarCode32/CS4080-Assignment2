from dataStructure import UserProfile


class UserManager:
    def __init__(self):
        self.users = []
        self.currentUser = None
    
    def createAccount(self):
        while True:
            name = input("Enter your name: ").strip()
            if any(account.name.lower() == name.lower() for account in self.users):
                print("This name is already used. Try again.")
            else: 
                break
        
        age = int(input("Enter your age: "))
        isPremium = input("Is the account Premium (Y/N): ").lower().strip() == 'y'
        # Preferences handled after assistant selection

        profile = UserProfile(name, age, isPremium)
        self.currentUser = profile
        self.users.append(profile)
        print(self.currentUser)


    def login(self):
        name = input("Enter your username: ").strip()
        for profile in self.users:
            if profile.name.lower() == name.lower():
                self.currentUser = profile
                return profile
        print("Could not find the user. Try again")
        return None

    def logout(self):
        if self.currentUser:
            print(f"Goodbye {self.currentUser.name}!!!")
            self.currentUser = None
        else:
            print("There is currently no user logged in.")
