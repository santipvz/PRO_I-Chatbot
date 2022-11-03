####################################### Imports #######################################
import os
import platform
import random
import csv
import urllib.request
from PIL import Image # Para que funcione el módulo PIL hay que hacer pip install pillow en la terminal o en el IDE
urllib.request.urlretrieve(
  'https://i0.wp.com/prevencionsaludproactiv.com/wp-content/uploads/2021/09/desktop_6637c766-e294-44ce-a7d8-21cb75a04014.png?w=509&ssl=1',
   "desktop_6637c766-e294-44ce-a7d8-21cb75a04014.png")
  
img = Image.open("desktop_6637c766-e294-44ce-a7d8-21cb75a04014.png")
random.seed()

####################################### Functions #######################################

# Function to clean the console so its more comfortable to see
def clear():
    #platform.system() This returns "Linux" "Darwin" "Java" or "Windows"
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")

# Asks for specific symptoms and calculates percentages
def addSymptons():
    
    # Function to show the user which symptons he can still add 
    def addableSymptons():
        print("Puedes añadir los siguientes síntomas:")
        for i in range(len(wellRedactedSintomas)):
            if userSymptoms[i] == 0:
                print(wellRedactedSintomas[i].capitalize())

    #Calculates the percentage of each disease    
    def calculatepercentages():
        percentages = {}
        for i in newEnfermedades:
            percentage = 0
            for j in range(len(userSymptoms)):
                if newEnfermedades[i][j] == userSymptoms[j] and userSymptoms[j] == 1:
                    percentage += 85/(newEnfermedades[i]).count(1)
                elif newEnfermedades[i][j] == userSymptoms[j] and userSymptoms[j] == 0:
                    percentage += 10/(newEnfermedades[i]).count(0)
                percentages[i] = percentage
        return percentages

    randomSymptom = random.choice(wellRedactedSintomas)
    answer = input(f"Escriba los síntomas que tenga o pulse enter para salir\nComo por ejemplo: {randomSymptom}\n").lower()

    while answer != "":
        symptomsAdded = [] #Lista para avisar al usuario el sintoma que ha introducido
        for i in range(len(sintomas)):
            counter = 0
            for j in range(len(sintomas[i])):
                for k in range(len(sintomas[i][j])):
                    if sintomas[i][j][k] in answer:
                        counter += 1
                        break
            if counter == len(sintomas[i]) and userSymptoms[i] == 0:
                userSymptoms[i] = 1
                symptomsAdded.append(wellRedactedSintomas[i])

        if len(symptomsAdded) == 0:
            option = input("No sé detectó ningún síntoma no nombrado anteriormente\n¿Quiere ver todos los posibles síntomas para añadir? [Y] ")
            if option in ["y","Y"]:
                addableSymptons()

        else:
            print("Has añadido los siguientes síntomas:")
            for i in symptomsAdded:
                print(i.capitalize())
        input("Pulse enter para continuar... ")
        clear()
        answer = input(f"Escriba los síntomas que tenga o pulse enter para salir\nComo por ejemplo: {randomSymptom}\n").lower()

    #Calculates the percentage of each disease
    newpercentages = {}
    percentages = calculatepercentages()

    #Deletes percentages lower than 20%
    for k,v in percentages.items():
        if v > 20:
            newpercentages[k] = v

    # No diseases detected
    if len(newpercentages) <= 0:
        option = input("Ninguna enfermedad se corresponde con los síntomas añadidos\n\
¿Quiere añadir más síntomas? [Y]")
        if option in ["y","Y"]:
                newpercentages = addSymptons()
    return newpercentages

####################################### Variables #######################################


wellRedactedSintomas = []
with open("WellRedactedSintomas.txt","r") as f:
    for linea in f:
        wellRedactedSintomas.append(linea.strip())
        
ubications = []
newEnfermedades = {}
enfermedades = {}
userSymptoms = [0 for x in wellRedactedSintomas]

with open("enfermedades.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        enfermedades[row["Enfermedad"]] = row[None]

####################################### Main Program #######################################

# Welcome message
print("Bienvenido a la consulta especializada en dolores abdominales!")

img.show()     
# We ask where the pain is
ubi = input("""Indique la zona del dolor o pulse enter para salir\n
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |\n 
""")


# We add to the list (ubications) the zone(s) where the patient feels pain
while ubi != "" or len(ubications) == 0:
    if ubi.isnumeric() and (ubi not in ubications) and (1 <= int(ubi) <= 9):
        ubications.append(ubi)
    clear()
    ubi = input("""Si le duele en otra zona, indíquelo o pulse enter para salir\n
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |\n 
""")

#We create a new dict where we only save the diseases that are possible on the zone the patient feels pain
for i in enfermedades:
    if i[-1] in ubications:
        newEnfermedades[i] = enfermedades[i]
clear()

#We erase the dictionary because we don't need it anymore
enfermedades.clear()

# Main function
newpercentages = addSymptons()

#Shows the percentage
print("Con los síntomas que tienes puede que tengas las siguientes enfermedades:")
for i,j in newpercentages.items():
    print(f"{i[:-1]:20}{j:4.02f}%")
