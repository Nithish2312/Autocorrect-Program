from textblob import TextBlob
def speak():
    while True:
        text=input("Enter your sentence")
        correct_text=TextBlob(text).correct()
        print(str(correct_text))

speak()
