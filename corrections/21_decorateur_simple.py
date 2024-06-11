def deco(fonction):
    def wrapper():
        print("je décore la fonction")
        fonction()

    return wrapper

def base():
    print("Je suis la fonction de base.")

# @deco
# def base2():
#     print("Je suis la fonction de base.")


if __name__ == "__main__":
    print("Avant la décoration : ")
    base()

    print()

    print("Apres la décoration : ")
    # base2()

    # fonction décorée à l'éxécution
    fonction = deco(base)
    fonction()
    #équivalent:
    deco(base)()