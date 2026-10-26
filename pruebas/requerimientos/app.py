import ollama
requerimiento=input("ingresa tu redaccion: ")
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
        }
    }
)
condicion=response.answers['condicion'].noul
if condicion >= 0.05:
    print(f"1. CUmple con la condicion: {condicion}")
else:
    print(f"2. No cumple la condicion {condicion}")