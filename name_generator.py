#Init
#Functions


#challenge 1
print("Welcome to Which Inside Out Character are You?")
print("Answer the questions to find out...")


ans=input("winter or summer?")
if ans=="winter":
    ans=input("sleeping or watch movies?")
    if ans== "watch movies":
        ans=input("red or green?")
        if ans=="red":
            print("your inside out chracter is anger")
        else:
            print("your inside out chracter is disgust")

    if ans== "sleeping":
        ans=input("purple or teal?")
        if ans=="purple":
            print("your inside out chracter is fear")
        else:
            print("your inside out chracter is envy")

if ans=="summer":
    ans=input("draw or homework?")
    if ans== "draw":
        ans=input("yellow or blue?")
        if ans=="yellow":
            print("your inside out chracter is joy")
        else:
            print("your inside out chracter is sadness")

    if ans== "homework":
        ans=input("pink or orange?")
        if ans=="pink":
            print("your inside out chracter is embarrassment")
        else:
            print("your inside out chracter is anxiety")


