import nltk
from nltk.chat.util import Chat, reflections

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name ?",
        ["I am a bot created by ZCOER. You can call me crazy!"]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about You?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind"]
    ],
    [
        r"I am fine",
        ["Great to hear that. How can I help you?"]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "How can I help you? :)"]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude. Seriously, you are asking me this?"]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse"]
    ],
    [
        r"(.*) created ?",
        ["Raghav created me using Python's NLTK library", "Top secret ;)"]
    ],
    [
        r"(.*) (location|city) ?",
        ['Pune, Maharashtra']
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an amazing company. I have heard about it. But they are in huge loss these"]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2", "Damn it's raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy"]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football"]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messi", "Ronaldo", "Rooney"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Ashok Saraf"]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest",
        ["Crazy_Tech has many great articles with each step explanation along with code, yo"]
    ],
    [
        r"quit",
        ["Bye take care. See you soon :)", "It was nice talking to you. See you soon :)"]
    ],
]

def chat():
    print("Hi! I am a chatbot created by ZCOER for your service")
    chat = Chat(pairs, reflections)
    chat.converse()

# initiate the conversation
if __name__ == "__main__":
    chat()
