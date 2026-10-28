async function evaluacionn(){
    try{
        const uri="https://ominous-disco-wv7pwj747v54c54wp-11434.app.github.dev/v1/systemone";
        const requerimientos="ell usuarios ingresa su email y su contraseña, el sistema evalua si es valido o no";
        const data={
            model: "d1-omni:600m",
            state: requerimientos,
            questions: {
                condicion: {
                    type: "noul",
                    instructions: "¿Incluye una situacion que detone el evento?",
                    criterio: {
                        true: "Especifica claramente el evento o situacion claramente",
                        false: "no menciona que situacion dispara la accion"
                    }
                }
            }
        }
        const response = await fetch(
            uri,
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body: JSON.stringify(data)
            }
        );
        if (!response.ok) {
            throw new Error(`Error HTTP ${response.status}: ${response.statusText}`);
        }
        const resultado=await response.json();
        console.log("Conexion con la API exitosa: ",resultado);
    } catch(error){
        console.log("ups algo fallo",error.message);
    }
}