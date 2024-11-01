import random

Gryffindor = 0
Slytherin = 0
Hufflepuff = 0
Ravenclaw = 0

quiz = [
    {
        "question": "Un muggle se enfrenta a ti y te dice que está seguro de que eres una bruja o un mago. Vos si:",
        "options":[
            {
                "statement": "Pregúnteles qué les hace pensar eso",
                "answer": "Ravenclaw"
            },
            {
                "statement": "Acepte y pregunte si les gustaría una muestra gratis de una maldición",
                "answer": "Gryffindor"
            },
            {
                "statement": "Acepta y aléjate, dejándolos preguntándose si estás fanfarroneando.",
                "answer": "Slytherin"
            },
            {
                "statement": "Dígales que está preocupado por su salud mental y ofrézcase a llamar a un médico.",
                "answer": "Hufflepuff"
            },
        ]
    },
    {
        "question": "Un muggle se enfrenta a ti y te dice que está seguro de que eres una bruja o un mago. Vos si:",
        "options":[
            {
                "statement": "Pregúnteles qué les hace pensar eso",
                "answer": "Ravenclaw"
            },
            {
                "statement": "Acepte y pregunte si les gustaría una muestra gratis de una maldición",
                "answer": "Gryffindor"
            },
            {
                "statement": "Acepta y aléjate, dejándolos preguntándose si estás fanfarroneando.",
                "answer": "Slytherin"
            },
            {
                "statement": "Dígales que está preocupado por su salud mental y ofrézcase a llamar a un médico.",
                "answer": "Hufflepuff"
            },
        ]
    },
    {
        "question": "Un muggle se enfrenta a ti y te dice que está seguro de que eres una bruja o un mago. Vos si:",
        "options":[
            {
                "statement": "Pregúnteles qué les hace pensar eso",
                "answer": "Ravenclaw"
            },
            {
                "statement": "Acepte y pregunte si les gustaría una muestra gratis de una maldición",
                "answer": "Gryffindor"
            },
            {
                "statement": "Acepta y aléjate, dejándolos preguntándose si estás fanfarroneando.",
                "answer": "Slytherin"
            },
            {
                "statement": "Dígales que está preocupado por su salud mental y ofrézcase a llamar a un médico.",
                "answer": "Hufflepuff"
            },
        ]
    },
    {
        "question": "Un muggle se enfrenta a ti y te dice que está seguro de que eres una bruja o un mago. Vos si:",
        "options":[
            {
                "statement": "Pregúnteles qué les hace pensar eso",
                "answer": "Ravenclaw"
            },
            {
                "statement": "Acepte y pregunte si les gustaría una muestra gratis de una maldición",
                "answer": "Gryffindor"
            },
            {
                "statement": "Acepta y aléjate, dejándolos preguntándose si estás fanfarroneando.",
                "answer": "Slytherin"
            },
            {
                "statement": "Dígales que está preocupado por su salud mental y ofrézcase a llamar a un médico.",
                "answer": "Hufflepuff"
            },
        ]
    },
    {
        "question": "Un muggle se enfrenta a ti y te dice que está seguro de que eres una bruja o un mago. Vos si:",
        "options":[
            {
                "statement": "Pregúnteles qué les hace pensar eso",
                "answer": "Ravenclaw"
            },
            {
                "statement": "Acepte y pregunte si les gustaría una muestra gratis de una maldición",
                "answer": "Gryffindor"
            },
            {
                "statement": "Acepta y aléjate, dejándolos preguntándose si estás fanfarroneando.",
                "answer": "Slytherin"
            },
            {
                "statement": "Dígales que está preocupado por su salud mental y ofrézcase a llamar a un médico.",
                "answer": "Hufflepuff"
            },
        ]
    },
    # {
    #     "question" : "Entras en un jardín encantado. ¿Qué sería lo que más le interesaría examinar primero?",
    #     "options": [
    #         "Las setas gordas rojas que parecen estar hablando entre sí",
    #         "El estanque burbujeante, en cuyas profundidades se arremolina algo luminoso",
    #         "El árbol de hojas de plata con manzanas doradas",
    #         "La estatua de un viejo mago con un extraño centelleo en los ojos."
    #     ]
    # }
]
def options(list):
    numeral = 0
    plantilla = ""
    while numeral < 4:
        plantilla += f"""\t {numeral+1}. {list[numeral].get("statement")} \n"""
        numeral += 1
    return plantilla


for value in quiz:
    print(f""" 
    {value.get("question")}

       {options(value.get("options"))}
    """)
    number = int(input("\t Ingrese su prespuesta: "))
    match value.get("options")[number-1].get("answer"):
        case "Gryffindor":
            Gryffindor += 1
        case "Hufflepuff":
            Hufflepuff += 1
        case "Slytherin":
            Slytherin += 1
        case "Ravenclaw":
            Ravenclaw += 1
        case _:
            print(":(")



maxValue = max( Gryffindor, Hufflepuff, Slytherin, Ravenclaw )

maxCount = [Gryffindor, Hufflepuff, Slytherin, Ravenclaw ].count(maxValue)



houses = {
    "Gryffindor": Gryffindor,
    "Hufflepuff": Hufflepuff,
    "Slytherin": Slytherin,
    "Ravenclaw": Ravenclaw
    }

topHouses = [house for house, score in houses.items() if score == maxValue]

selectedHouse = random.choice(topHouses)

if maxCount == 1:
    print(f"Su casa es...     ¡{topHouses}! ")


else:
    print(f"su casa es...   ¡{selectedHouse}!") 


print("Gryffindor: ", Gryffindor)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)
print("Ravenclaw: ", Ravenclaw)


 #!ravenclaw¡
