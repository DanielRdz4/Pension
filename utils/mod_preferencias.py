import json
import os

ruta_datos = "data"
ruta_relativa =os.path.join(os.curdir,ruta_datos)
filename = "preferencias"
ruta = os.path.join(ruta_relativa,f"{filename}.json")


def obt_float(mensaje):
    while True:
        try:
            dato_usr = float(input(mensaje))
            return dato_usr
        except ValueError:
            print("Dato inválido, intente de nuevo")

def obt_interger(mensaje):
    while True:
        try:
            dato_usr = int(input(mensaje))
            return dato_usr
        except ValueError:
            print("Dato inválido, intente de nuevo")

def crear_dicc_preferencias():
    """Crea las prefrenecias del usuario"""

    preferencias = {
        "Tasa-nominal-promedio":[],
        "Inflacion-promedio":[],
        "Mensualidad":[],
        "Años-invertidos":[],
        "Inversion-inicial":[],
        "Tasa_de_retiro_anual":[],
    }

    preferencias["Tasa-nominal-promedio"]=obt_float("Tasa nominal promedio anual esperada (decimal): ")
    preferencias["Inflacion-promedio"]= obt_float("Inflación anual promedio esperada (decimal): ")
    preferencias["Mensualidad"]=obt_interger("Mensualidad: ")
    preferencias["Años-invertidos"] = obt_interger("Años hasta el retiro: ")
    preferencias["Inversion-inicial"] = obt_interger("Inversion actual: ")
    preferencias["Tasa_de_retiro_anual"]=obt_float("Tasa de retiro anual sobre inversión (decimal): ")

    return preferencias

def obt_preferencias():
    """Obtiene preferencias actuales"""

    with open(ruta, "r") as f:
        preferencias = json.load(f)
        return preferencias

def decidir_estado_preferencias(preferencias_act):
    """Permite al usuario crear o mantener preferencias actuales"""

    print("Preferencias actuales: \n")
    for k, v in preferencias_act.items():
        print(f"{k}= {v}")

    while True:
        evaluar = input("\n¿Desea mantener las preferencias actuales? (Y/N): ").rstrip().upper()
        if evaluar == "Y":
            break
        elif evaluar == "N":
            os.remove(ruta)
            crear_preferencias()
            break
        else:
            continue

def guardar_preferencias(preferencias):
    """Crea el archivo .json con las preferencias de usuario en la ruta establecida"""

    with open(ruta,"w") as f:
        json.dump(preferencias,f,indent = 4)

def crear_preferencias():
    preferencias = crear_dicc_preferencias()
    guardar_preferencias(preferencias)

#MAIN
def gestionar_preferencias():
    if os.path.exists(ruta):

        #Leer archivo de preferencias actual
        preferencias_act = obt_preferencias()
        decidir_estado_preferencias(preferencias_act)

    else:
        crear_preferencias()

