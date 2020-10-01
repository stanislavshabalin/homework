name = input('Hello, what is your name? ')
age = int(input('And how old are you? '))
gender = input("Are u male or female? ")
if gender == "male" and age >= 18:
    print('I like your name, bro' + name + " - sounds good. You are an adult already =)")
elif gender == "male" and age < 18:
    print("Hey," + name + ", You are pretty young =)")
elif gender == "female" and age >= 18:
    print("Hello, young lady - " + name + " I am glad to see you there <3")
else:
    print("Hello, little girl :3. " + name + ", if you need any help, you can always ask me to")
