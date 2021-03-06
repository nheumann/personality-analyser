emotion_to_emoji = {
    "admiration" : '๐คฉ',
    "amusement" : '๐',
    "anger": '๐ค',
    "annoyance": '๐', 
    "approval": '๐',    
    "caring": '๐ค',
    "confusion":'๐คจ',
    "curiosity": '๐',
    "desire": '๐ค',
    "disappointment": '๐',
    "disapproval": '๐',
    "disgust": '๐คข',
    "embarrassment":'๐ฃ',
    "excitement": '๐',
    "fear": '๐ฑ',
    "gratitude": "๐",
    "grief": "๐ญ",    
    "joy": "๐",    
    "love": "๐ฅฐ",    
    "nervousness": "๐ณ",    
    "optimism": "๐",    
    "pride": "๐",    
    "realization": "๐ค",    
    "relief": "๐",    
    "remorse": "๐",    
    "sadness" : "๐",    
    "surprise" : "๐ฒ",    
    "neutral" : "๐",
}

all_emotions = [
    "admiration",
    "amusement",
    "anger",    
    "annoyance",    
    "approval",    
    "caring",    
    "confusion",    
    "curiosity",    
    "desire",    
    "disappointment",    
    "disapproval",    
    "disgust",    
    "embarrassment",    
    "excitement",
    "fear",    
    "gratitude",    
    "grief",    
    "joy",    
    "love",    
    "nervousness",    
    "optimism",    
    "pride",    
    "realization",    
    "relief",    
    "remorse",    
    "sadness",    
    "surprise",    
    "neutral"
    ]

positive_emotions =  [
            "admiration",
            "amusement", 
            "approval", 
            "caring", 
            "curiosity",
            "desire", 
            "excitement", 
            "gratitude",
            "joy", 
            "love", 
            "optimism", 
            "pride", 
            "realization", 
            "relief", 
            "surprise"]

negative_emotions =  [   
            "anger",    
            "annoyance",       
            "confusion",    
            "disappointment",  
            "disapproval",    
            "disgust",    
            "embarrassment",
            "fear",    
            "grief",   
            "nervousness",   
            "remorse",    
            "sadness"
        ]


def is_positive_emotion(emotion: str) -> bool:
    return emotion in positive_emotions