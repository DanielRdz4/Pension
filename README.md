# Pension
# Calculadora de Pensión por Inversión

Este programa calcula el crecimiento de una inversión a largo plazo y la pensión mensual resultante, considerando el efecto de la inflación y los intereses por dividendos.

## Características

- **Gestión de preferencias**: Guarda y reutiliza configuraciones de inversión
- **Cálculo con inflación**: Ajusta automáticamente las contribuciones mensuales por inflación
- **Tasa real de retorno**: Calcula usando la fórmula `((1+tasa_nominal)/(1+inflacion))-1`
- **ISR sobre ganancias**: Aplica un 10% de ISR sobre las ganancias anuales por reparto de dividendos 
- **Pensión mensual**: Calcula la pensión basada en una tasa de retiro anual

## Estructura del Proyecto

```
pension/
├── src/
│   └── main.py              # Archivo principal
├── utils/
│   ├── mod_preferencias.py  # Gestión de preferencias de usuario
│   └── calc_pension.py      # Cálculos financieros
├── data/
│   └── preferencias.json    # Configuración guardada (ignorado por Git)
├── .gitignore               # Archivos ignorados por Git
└── README.md
```

## Uso

1. Ejecuta el programa:
```bash
python src/main.py
```

2. En la primera ejecución, se te pedirán los siguientes datos:
   - **Tasa nominal promedio anual**: Rendimiento neto esperado de la inversión  (%)
   - **Inflación promedio anual**: Inflación anual esperada  (%)
   - **Mensualidad**: Contribución mensual a fondo de inverisón
   - **Años hasta el retiro**: Período de inversión
   - **Inversión inicial**: Monto inicial (puede ser 0)
   - **Tasa de retiro anual**: Tasa anual para retiro de fondos de la inversíon 

3. En ejecuciones posteriores, podrás mantener o actualizar las preferencias guardadas.

## Ejemplo de Salida

```
Inverisón total: $1,234,567.89
Pensión mensual: $4,115.23
```

## Metodología de Cálculo

### Crecimiento de la Inversión
- Se aplica la tasa real mensual: `tasa_real = ((1+tasa_nominal)/(1+inflacion))-1`
- Las contribuciones mensuales se ajustan anualmente por inflación
- Se capitaliza mensualmente durante el período especificado
- **ISR sobre ganancias**: Se aplica un 10% de ISR sobre las ganancias por dividendos anuales.

### Pensión Mensual
- Se calcula como: `pension_mensual = monto_final * tasa_retiro_anual / 12`

## Notas Importantes

- La tasa de rendimiento esperado a ingresar deberá considerar el efecto de las tasas de manejo de cuenta, comisiones, etc. Ej. 10% de rendimiento - 2% por manejo de cuenta = 8% neto anual
- El archivo `preferencias.json`, así como el directorio que lo contiene son creados automáticamente al ejecutar el programa por primera vez
- Los cálculos asumen reinversión completa de ganancias durante el período de inversión
- **ISR aplicado**: Se descuenta un 10% sobre las utilidades acumuladas anuales
- El programa considera inversiones en instrumentos de renta variable con reparto de dividendos

## Requisitos

- Python 3.x
- Módulos estándar: `json`, `os`, `pathlib`