# Pension
# Calculadora de Pensión por Inversión

Este programa calcula el crecimiento de una inversión a largo plazo y la pensión mensual resultante, considerando inflación y tasas de retorno reales.

## Características

- **Gestión de preferencias**: Guarda y reutiliza configuraciones de inversión
- **Cálculo con inflación**: Ajusta automáticamente las contribuciones mensuales por inflación
- **Tasa real de retorno**: Calcula usando la fórmula `((1+tasa_nominal)/(1+inflacion))-1`
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
└── README.md
```

## Uso

1. Ejecuta el programa:
```bash
python src/main.py
```

2. En la primera ejecución, se te pedirán los siguientes datos:
   - **Tasa nominal promedio anual**: Retorno esperado de la inversión (decimal)
   - **Inflación promedio anual**: Inflación esperada (decimal)
   - **Mensualidad**: Contribución mensual inicial
   - **Años hasta el retiro**: Período de inversión
   - **Inversión inicial**: Monto inicial (puede ser 0)
   - **Tasa de retiro anual**: Porcentaje a retirar anualmente en la jubilación

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

### Pensión Mensual
- Se calcula como: `pension_mensual = monto_final * tasa_retiro_anual / 12`

## Notas Importantes

- Las tasas se ingresan como decimales (ej: 0.10 para 10%)
- El archivo `preferencias.json` se crea automáticamente y está excluido del control de versiones
- Los cálculos asumen reinversión completa de ganancias durante el período de acumulación

## Requisitos

- Python 3.x
- Módulos estándar: `json`, `os`