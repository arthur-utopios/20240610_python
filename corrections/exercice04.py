temp = int(input("Saisir une température: "))

if(temp <= 0):
    print("Solide")
elif(temp <= 100):
    print("Liquide")
else:
    print("Gazeux")