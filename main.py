#Bonjour
""" cela est mon premier projet Python le but de ce projet et c'est que l'utilisateur trouve un nombre aleatoir entre 
0 et 10 plus il le trouve vite mieux est son scoore  """

""" 
Pour cela il faut importer la biblioteque random 
"""
import random


""" on cree une fonction qui genere un nombre aleatoir entre 0 et 10 """



def aleatoir():
    nombreAleatoir = random.randint(0,10)
    return nombreAleatoir

"""

teste de la fonction aleatoir

print("le nombre aleatoir entre 0 et 10 est :{}".format(aleatoir()))


"""
""" 

maintenat on cree une fonction qui permet de guider l'utilisateur en fontion 
du saisi au clavier et le nombde aleatoir (les arguments de la fonction)

j'ai essayer entre temps de faire de la gestion d'erreur car on a un intput

"""

def guider(nombreAleatoir,nombreUtilisateur):
    if nombreAleatoir < nombreUtilisateur:
        print("le nombre juste est plus bas")
    elif nombreAleatoir > nombreUtilisateur:
        print("le nombre juste est plus haut")

                                            #le code globale

nombreUtilisateur=input("deviner le nombre juste :")
Aleatoir = aleatoir()
tentative = 0
""""""
#si on trouve pas le nombre juste
while Aleatoir != nombreUtilisateur:
    tentative += 1
    #print(Aleatoir) regarder si tout se passe comme il faut
    #il faut pas faire confiance a l'utilisateur

    try:

        nombreUtilisateur == int(nombreUtilisateur)
        guider(Aleatoir,nombreUtilisateur)

    except:

        print("ce que vous avais saisi n'est pas compris entre 0 et 10 ou ce n'est pas un nombre " )
    
    #demander de resseiller
    nombreUtilisateur=input("saisir a nouveau :")

""""""

#si on trouve le nombre juste
print("felicitation vous avais trouver le nombre !")
print("Votre score est de : {}".format(100/tentative))

print("partie terminer")

