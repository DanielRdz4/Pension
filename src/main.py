from utils.mod_preferencias import gestionar_preferencias, obt_preferencias
from utils.calc_pension import calc_crecimiento, calc_pens_mensual

def main():
    """
    Función princial que ejecuta el cálculo de la pensión.
    """
    gestionar_preferencias()
    preferencias = obt_preferencias()
    monto_final = calc_crecimiento(preferencias)
    pension_mensual = calc_pens_mensual(preferencias, monto_final)

    print(f"Inverisón total: ${monto_final:,.2f}")
    print(f"Pensión mensual: ${pension_mensual:,.2f}")

if __name__ =="__main__":
    main()