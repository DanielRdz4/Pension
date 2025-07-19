
def calc_crecimiento(preferencias):
    # inicializar monto
    monto = preferencias["Inversion-inicial"]
    mensualidad = preferencias["Mensualidad"]
    inflacion = preferencias["Inflacion-promedio"]
    tasa_nominal = preferencias["Tasa-nominal-promedio"]
    tasa_r = ((1+tasa_nominal)/(1+inflacion))-1
    tasa_r_m = tasa_r/12
    años_invertidos = preferencias["Años-invertidos"]

    for _ in range(años_invertidos):
        monto_inicio_año = monto

        for _ in range(12):
            monto = monto*(1+tasa_r_m) + mensualidad
        
        utilidad_anual = monto - monto_inicio_año - (mensualidad*12)

        # ISR simple sobre ganancias de capital: 10% fijo
        if utilidad_anual > 0:
            isr_ganancias = utilidad_anual * 0.10
            monto -= isr_ganancias

        mensualidad *= (1+inflacion)
        
    return monto

def calc_pens_mensual(preferencias, monto):
    tasa_retiro = preferencias["Tasa_de_retiro_anual"]
    mensualidad = monto*tasa_retiro/12
    return mensualidad