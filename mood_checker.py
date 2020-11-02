name = input("What's your name? ")
print(f"Hi, {name}!")
mood = input("How you doing' today? ")
mood_lower = mood.lower()
positive = ["well", "good", "super", "great", "wonderful", "superb", "excellent", "fantastic"]
negative = ["not good", "poor", "sad", "hurt", "bad", "unwell", "ill", "rotten", "awful", "lame", "horrible"]
neutral = ["so-so", "ok", "meh"]

for i in positive:
    if i == mood_lower:
        print(f"Keep up the good work, {name}")
for i in neutral:
    if i == mood_lower:
        print(f"That's ok, we all have days like these. It'll get better, {name}!")
for i in negative:
    if i == mood_lower:
        print(f"Aww, {name}, I'm so sorry! Virtual hug is loading...\nnow!")

