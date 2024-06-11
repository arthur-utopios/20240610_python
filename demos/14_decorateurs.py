# Un décorateur simple se présente de la sorte
# Il s'agit d'une fonction qui accepte en paramètre une fonction
def mon_decorateur(fonction):
    def wrapper():
        print("je fais des choses avant")
        # instructions effectuées avant

        fonction()

        #instruction effectuées après
        print("je fais des choses après")

    return wrapper

@mon_decorateur
def hello_world():
    print("Hello world!")

@mon_decorateur
def hello_world2():
    print("Hello world 2!")

hello_world()  # Ici on appelle la fonction qui se verra décorée

hello_world2()



# Apparté sur les *args et les **kwargs

# Le paramètre étoile * se transformera en tuple qui pourra avoir autant de paramètres en son sein,
# il sera possible d'y accéder par leur index []
def ma_fonction_avec_args(*args): #args est une convention, mais le caractère * est obligatoire
    for arg in args:
        print(arg)

ma_fonction_avec_args(1, "5", True, "Salut", "\na\nb\nc")
ma_fonction_avec_args()
ma_fonction_avec_args("aaa")

def ma_fonction_avec_args2(bonjour, *args): 
    print(bonjour)
    print(args)
    print(bonjour)

ma_fonction_avec_args2("bonjour!", 1, 2, "Salut", True)


# Le paramètre double étoile ** se transformera en un dictionnaire qui contiendra un ensemble clé-valeur
# qui aura tous les paramètres ayant un nom associé à une valeur via la syntaxe nom = valeur
# kwargs est une convention ==> "keword arguments"
def ma_fonction_avec_kwargs(**kwargs):
    print(kwargs)
    for kwarg_key, kwarg_value in kwargs.items():
        print(kwarg_key, kwarg_value)

ma_fonction_avec_kwargs(agument1="test", argument2=True, arg3=300)


#si on veux utiliser les 2 en plus des arguments classiques, cela reste possible:
def ma_fonction(argument_classique, argument_par_défaut="valeur par défaut", *args, **kwargs):
    print(argument_classique)
    print(argument_par_défaut)
    print(args)
    print(kwargs)

ma_fonction(1, None, 1, 2 ,3, 4, key1="value1", key2="value2", key3="value3")
ma_fonction(1, None, 1, 2 ,3, 4)
ma_fonction(1, None)
ma_fonction(1)
ma_fonction(argument_classique=1, argument_par_défaut="test")

# Il n'est pas possible de mettre des arguments étoiles après un argument double étoile,
# ni des arguments positionnels classiques


# Il est cependant possible de mettre :
# - Arguments positionnels puis arguments étoile
# - Argument étoile puis positionnel (à condition de les injecter dans la fonction via la syntaxe nom = valeur
def ma_fonction(*args, argument_classique,  **kwargs):
    print(argument_classique, args, kwargs)

ma_fonction(1, 2, 3, 3, aaa=1, argument_classique="a33EA", bbb="333")




#RETOUR AUX DECORATEURS
# Pour décorer une fonction ayant des paramètres,
# il va nous falloir altérer le wrapper pour prendre en compte *args et **kwargs
def my_dec_bis(func):
    def wrapper(*args, **kwargs):
        print("args", args)
        print("kwargs", kwargs)
        #avant
        func(*args, **kwargs)
        #après

    return wrapper

@my_dec_bis
def say_name(name):
    print("Bonjour", name)
say_name("Guillaume")

@my_dec_bis
def say_something(**kwargs):
    for kwarg_key, kwarg_value in kwargs.items():
        print(kwarg_key, kwarg_value)

say_something(salut="bonjour", ciao="aurevoir")



# Décorateur de fonction ayant des paramètres et un retour
def my_decorator_3(func):
    def wrapper(*args, **kwargs):
        print("args", args)
        print("kwargs", kwargs)
        result = func(*args, **kwargs)
        print("Quelque chose après")

        return result

    return wrapper

    
@my_decorator_3
def addition(a, b):
    return a + b

print(addition(1, 2))


# Pour créer un décorateur avec paramètres, il va falloir créer une fonction qui défini un décorateur
def my_decorator_param(message, *args_b, **kwargs_b):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("args", args)
            print("kwargs", kwargs)
            print("args_b", args_b)
            print("kwargs_b", kwargs_b)
            print("message :", message)
            result = func(*args, **kwargs)
            print("Quelque chose après")

            return result
        return wrapper
    return decorator


@my_decorator_param('Bonjour')
def soustraction(a, b):
    return a - b

print(soustraction(10, 2))


#pour aller (encore) plus loin, il est possible de décorer des décorateurs