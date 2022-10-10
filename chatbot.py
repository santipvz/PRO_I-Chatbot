import os
import platform

#platform.system() This returns "Linux" "Darwin" "Java" or "Windows"
if platform.system() == "Linux":
    os.system("clear")
elif platform.system() == "Windows":
    os.system("cls")
 

sintomas = [["dolor","leve"], ["dolor","moderadamente","intenso"], ["dolor","intenso"],
            ["dolor","insoportable"],["retortijones"],["dolor","intermitente","colico"],
            ["dolor","punzante"],["quemazón"],["dolor","vago"],["dolor","comer"],["hambre"],
            ["distensión"],["náuseas"],["vómitos"],["malestar","estomacal"],["sudoración"],
            ["taquicardia"],["sangre","orina"],["ardor","orina"],["dolor","orina"],
            ["sensación","imperiosa","orinar"],["sagre","heces"],["dolor","evacuación"],
            ["evacuación","incompleta"],["diarrea"],["diarrea","sangre"],
            ["protuberancia","indolora","ingle","escroto"],["fiebre"],["ictericia"],
            ["estreñimiento"],["pérdida","peso"],["cansancio"],["saciedad"]]

wellRedactedSintomas = ["Dolor leve", "Dolor moderadamente intenso", "Dolor intenso",
            "Dolor insoportable","Retortijones","Dolor intermitente/colico",
            "Dolor punzante","Quemazón","Dolor vago","Dolor _Comer","Hambre",
            "Distensión","Náuseas","Vómitos","Malestar estomacal","Sudoración",
            "Taquicardia","Sangre-Orina","Ardor-Orina","Dolor-Orinar",
            "Sensación imperiosa de orinar","Sagre-Heces","Dolor-Evacuación",
            "Evacuación incompleta","Diarrea","Diarrea-Sangre",
            "Protuberancia-Indolora-Ingle-Escroto","Fiebre,Ictericia",
            "Estreñimiento","Pérdida de peso","Cansancio","Saciedad"]


userSymptoms = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
percentages = {}

enfermedades = {"Cálculos biliares1":[0,0,1,1,0,1,1,0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                 "Hepatitis1":[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0],
                 "Pancreatitis1":[0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 "Úlcera duodenal1":[1,1,0,0,0,0,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  "Cálculos biliares2":[0,0,1,1,0,1,1,0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 "Gastritis2":[0,0,1,0,0,1,1,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 "Gastrointeritis2":[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0],
                 "Hepatitis2":[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,1,0],
                 "Pancreatitis2":[0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                 "Úcera estomacal2":[1,1,0,0,0,0,0,1,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
                 "Pancreatitis3":[0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  "Úcera duodenal3":[1,1,0,0,0,0,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  "Cálculos biliares4":[0,0,1,1,0,1,1,0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 "Cálculos renales4":[0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
                 "Estreñimiento4":[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0],
                 "Gastrointeritis4":[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0],
                 "Hepatitis4":[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,1,0],
                 "Apendicitis5":[1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  "Gastroenteritis5":[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0],
                  "Hernia umblical5":[0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  "Pancreatitis5":[0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                  "Úlcera estomacal5":[1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
                  "Cálculos renales6":[0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
                 "Colitis6":[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0],
                 "Diverticulitis6":[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
                 "Fecaloma6":[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0],
                 "Gastroenteritis6":[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0],
                 "Apendicitis7":[0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                 "Enfermedad Pelvica7":[0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],
                 "Estreñimiento7":[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0],
                 "Hernia inguinal7":[0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                 "Apendicitis8":[0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 "Cálculos renales8":[1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                 "Diverticulitis8":[1,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0],
                 "Enfermedad Pelvica8":[0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],
                 "Infección de orina8":[0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
                 "Colitis9":[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
                 "Diverticulitis9":[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
                 "Enfermedad Pelvica9":[0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],
                 "Fecaloma9":[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0],
                 "Gastroenteritis9":[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0],
                 "Hernia inguinal9":[0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]}

# Wwlcome message
print("Bienvenido a la consulta especializada en dolores abdominales!")
      
# Preguntamos ubicación del dolor

ubi = input("""Indique la zona del dolor\n
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |\n 
""")

ubications = []

while ubi != "" or len(ubications) == 0:
    if ubi.isnumeric() and (ubi not in ubications) and (1 <= int(ubi) <= 9):
        ubications.append(ubi)
    os.system("cls")
    ubi = input("""Si le duele en otra zona, indíquelo\n
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |\n 
""")

newEnfermedades = {}
for i in enfermedades:
    if i[-1] in ubications:
        newEnfermedades[i] = enfermedades[i]
os.system("cls")


#We ask for specific symptoms
answer = input("Escriba los síntomas que tenga: ").lower()
while answer != "":
    for i in range(len(sintomas)):
        counter = 0
        for j in range(len(sintomas[i])):
            if sintomas[i][j] in answer:
                counter += 1
        if counter == len(sintomas[i]):
            userSymptoms[i] = 1
    print(userSymptoms)
    answer = input("Escriba los síntomas que tenga: ")
    

#Calculates the percentage of each disease
for i in newEnfermedades:
    percentage = 0
    for j in range(len(userSymptoms)):
        if newEnfermedades[i][j] == userSymptoms[j]:
            percentage += 100/len(userSymptoms)
        percentages[i] = percentage
