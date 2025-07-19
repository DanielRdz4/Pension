import json
from pathlib import Path
import os

DIR_BASE= Path(__file__).parent.parent
DIR_DATOS = DIR_BASE / "data"
ARCHIVO_PREFERENCIAS = "preferencias.json"
RUTA_PREFERENCIAS = DIR_DATOS / ARCHIVO_PREFERENCIAS


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
        "Tasa-nominal-promedio":obt_float("Tasa nominal promedio anual esperada (decimal): "),
        "Inflacion-promedio":obt_float("Inflación anual promedio esperada (decimal): "),
        "Mensualidad":obt_interger("Mensualidad: "),
        "Años-invertidos":obt_interger("Años hasta el retiro: "),
        "Inversion-inicial":obt_interger("Inversion actual: "),
        "Tasa_de_retiro_anual":obt_float("Tasa de retiro anual sobre inversión (decimal): ")
    }

    return preferencias

def obt_preferencias():
    """Obtiene preferencias actuales"""

    with open(RUTA_PREFERENCIAS, "r") as f:
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
        else:
            os.remove(RUTA_PREFERENCIAS)
            crear_preferencias()
            break

def guardar_preferencias(preferencias):
    """Crea el archivo .json con las preferencias de usuario en la ruta establecida"""

    with open(RUTA_PREFERENCIAS,"w") as f:
        json.dump(preferencias,f,indent = 4)

def crear_preferencias():
    preferencias = crear_dicc_preferencias()
    guardar_preferencias(preferencias)

#MAIN
def gestionar_preferencias():
    if Path.exists(RUTA_PREFERENCIAS):

        #Leer archivo de preferencias actual
        preferencias_act = obt_preferencias()
        decidir_estado_preferencias(preferencias_act)

    else:
        crear_preferencias()

