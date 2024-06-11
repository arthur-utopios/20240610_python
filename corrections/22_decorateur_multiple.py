def decorateur_base(function):
    def fonc_decoree():
        print("Je décore la fonction !")
        function()

    return fonc_decoree


def decorateur_param(parametre):
    def decorator(function):
        def wrapper():
            print("J'écris un message personnalisé : ", parametre)
            result = function()
            return result
        return wrapper
    return decorator


# @decorateur_base
# @decorateur_param("Message perso")
def fonc_base():
    print("Je suis la fonction de base")
    pass


f_1 = fonc_base
f_2 = decorateur_param("Message perso")(f_1)
f_3 = decorateur_base(f_2)

print("Avant décoration :")
f_1()
print("\nAprès décoration personnalisable :")
f_2()
print("\nAprès décoration multiple :")
f_3()

