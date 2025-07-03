from enum import Enum
from datetime import datetime

class AssistantType(Enum):
    MUSIC = 1
    STUDY = 2

class UserProfile:
    def __init__(self, name, age, premium, preferences={}):
        self.name = name
        self.age = age
        self.premium = premium
        self.preferences = preferences

    def __repr__(self):
        return f"Name: {self.name}\nAge: {self.age}\nPremium: {self.premium}\nPreferences: {self.preferences}"

class Request:
    def __init__(self, input, dateTime, commandType):
        self.input = input
        self.dateTime = dateTime
        self.commandType = commandType
        

class Response:
    def __init__(self, message, confidence=1.0, actionPerformed=True):
        self.message = message
        self.confidence = confidence
        self.actionPerformed = actionPerformed