import json
from pathlib import Path
import os

DIR_BASE= Path(__file__).parent.parent
DIR_DATOS = DIR_BASE / "data"
ARCHIVO_PREFERENCIAS = "preferencias.json"
RUTA_PREFERENCIAS = DIR_DATOS / ARCHIVO_PREFERENCIAS

def obt_años(mensaje):
    """Obtiene de manera segura los años totales de inversión"""

    while True:
        try:
            dato_usr = float(input(mensaje))
            
            #Asegurar que el dato sea válido        
            if dato_usr < 0:
                print("El valor debe ser mayor o igual a 0")
                continue

            #Asegurar que el valor sea un entero
            if dato_usr % 1 != 0:
                print("Los años invertidos tienen que ser un número entero")
                continue

            return int(dato_usr)

        except ValueError:
            print("Dato inválido, intente de nuevo")

def obt_float(mensaje):
    while True:
        try:
            dato_usr = float(input(mensaje))

            #Asegurar que el dato sea válido
            if dato_usr >= 0:
                return dato_usr
            else:
                print("El valor debe ser mayor o igual a 0")

        except ValueError:
            print("Dato inválido, intente de nuevo")

def crear_dicc_preferencias():
    """Crea las prefrenecias del usuario"""

    preferencias = {
        "Tasa-nominal-promedio":obt_float("Tasa nominal promedio anual esperada (%): "),
        "Inflacion-promedio":obt_float("Inflación anual promedio esperada (%): "),
        "Mensualidad":obt_float("Mensualidad: "),
        "Años-invertidos":obt_años("Años hasta el retiro: "),
        "Inversion-inicial":obt_float("Inversion actual: "),
        "Tasa_de_retiro_anual":obt_float("Tasa de retiro anual sobre inversión (%): ")
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

    # Asegurar que el directorio data existe
    DIR_DATOS.mkdir(parents=True, exist_ok=True)

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

