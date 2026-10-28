import ollama
requerimiento="""El profesor ingresa a la evaluación del alumno 
a el sistema de calificaciones"""
response=ollama.systemone(
    model="d1-omni:600m",
    state=requerimiento,
    questions={
        'condicion':{
            'type':'noul',
            'instructions':'¿Incluye una situacion que detone el evento?',
            'criterio':{
                'true':'Especifica claramente el evento o situacion claramente',
                'false':'no menciona que situacion dispara la accion'
            }
        },
        'objeto':{
            'type':'noul',
            'instructions':'¿Incluye un objeto?',
            'criterio':{
                'true':'Especifica que objeto es el que realizara la acción',
                'false':'No menciona nigun objeto'
            }
        },
        'verbo':{
            'type':'noul',
            'instructions':'¿Incluye el verbo "debe"?',
            'criterio':{
                'true':'existe la palabra "debe" dentro del texto',
                'false':'No existe'
            }
        },
        'accion':{
            'type':'noul',
            'instructions':'¿hay una accion que se realizara despues de haber tenido una condicion y el sujeto que la realizara?',
            'criterio':{
                'true':'hay una accion que se realizara',
                'false':'no hay ninguna accion que se relice'
            }
        },
        'objeto':{
            'type':'noul',
            'instructions':'¿hay un objeto con el cual se realizara la acción?',
            'criterio':{
                'true':'existe on objeto que se vea afectado por la accion',
                'false':'no existe dicho objeto'
            }
        },
        'criter':{
            'type':'noul',
            'instructions':'¿el criterio ayuda a que la accion tenga un sentido dentro de la oracion?',
            'criterio':{
                'true':'aporta a delimitar el alcance de la accion',
                'false':'no aporta nada'
            }
        }
    }
)
condicion=response.answers['condicion'].noul
if condicion >= 0.5:
    print(f"1. Cumple con la condicion: {condicion}")
else:
    print(f"2. No cumple la condicion {condicion}")