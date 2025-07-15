import sys
from pathlib import Path

# Añadir el directorio padre al path para poder importar utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.mod_preferencias import gestionar_preferencias, obt_preferencias
from utils.calc_pension import calc_crecimiento, calc_pens_mensual

gestionar_preferencias()
preferencias = obt_preferencias()
monto_final = calc_crecimiento(preferencias)
pension_mensual = calc_pens_mensual(preferencias, monto_final)

print(f"Inversión total: ${monto_final:,.2f}")
print(f"Pensión mensual: ${pension_mensual:,.2f}")

