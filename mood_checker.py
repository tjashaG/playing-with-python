name = input("What's your name? ")
print(f"Hi, {name}!")
mood = input("How you doing' today? (fantastic, happy, meh or sad)")

if mood == "happy":
    print(f"Keep up the good work, {name}")
elif mood == "fantastic":
    print(f"Great to hear {name}, you're doing something right!")
elif mood == "meh":
    print(f"That's ok, we all have days like these. It'll get better, {name}!")
else:
    print(f"Aww, {name}, I'm so sorry! Virtual hug is loading...\nnow!")
