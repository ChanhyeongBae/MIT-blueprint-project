def main():
    op1 = int(input("Hello! How would you describe your skill level? \n"
                    "1: Novice \n"
                    "2: Experienced \n"
                    "3: Advanced \n"
                    ">>>"))

    op2 = int(input("What are you looking learn more about? \n"
                    "1: Mobile Application Development \n"
                    "2: Website Development \n"
                    "3: Video Game Creation \n"
                    "4: Cyber-security \n"
                    "5: Data Science \n"
                    ">>>"))

    op3 = int(input("What sounds most exciting? \n"
                    "1: Creating an appealing yet simple interface users interact with \n"
                    "2: Designing the backbones of application \n"
                    "3: Both! \n"
                    ">>>"))

    print("You should learn: ")
    if op1 == 1 and op2 == 2 and op3 == 2 or 3:
        print("HTML! HTML is a language for the structure of a website.")
    if op1 == 1 or 2 and op2 == 2 and op3 == 1 or 3: # may need to add op1 and op3 in front of 2 and 3 respectivley
        print("CSS! CSS is used in the visual design of websites.")
    if op1 == 1 or 2 and op2 == 1 or 2 or 5:
        print("JavaScript! JavaScript is used to promote interactivity of websites.")
    if op2 == 4 and op3 == 2 or 3:
        print("C! C is used by many operating systems.")
    if op1 == 3 and op2 == 3 or 4 or 5:
        print("C++! C++ is considered by many to be a difficult language."
              "However, it's used in a variety of fields, including game development, data structures, and operating systems!")
    if op1 == 1 or 2 and op2 == 1:
        print("C#! C# is used in a variety of fields including video games, applications, and websites!")
    if op2 == 1 or 2 or 3 or 5 and op3 == 2 or 3:
        print("Java! Java is commonly used in back-end development.")
    if op == 2 or 3 and op2 == 1:
        print("Swift! Swift was developed by Apple and is commonly used in IOS Development.")
    if op1 == 1 or 2 and op2 == 3:
        print("Lua! Lua is commonly used to develop video games, notably Roblox, which uses its own version of Lua.")
    if op1 == 2 or 3 and op2 == 5:
        print("R! R is often used in data science, analytics, and scientific research.")
    if op1 == 1 or op2 == 2 or 3 or 4 or 5 and op3 == 2 or 3:
        print("Python! Python is a versatile language used in a variety of settings, such as"
              "web development, AI, financial applications, and much more!")
main()