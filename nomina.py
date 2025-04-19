# ----------------------------------------------------
# Constantes de referencia (2025, período 1)
# ----------------------------------------------------
SALARIO_MINIMO_2025 = 1423500     # Salario mínimo mensual vigente
VALOR_HORA_ORDINARIA = 5197        # Valor de la hora ordinaria

# Descuentos
PORC_SALUD = 0.04
PORC_PENSION = 0.04

# Factores para los 7 tipos de hora extra/recargo (total a pagar sobre la hora base)
TIPOS_HORAS = [
    ("Hora extra diurna (25%)", 1.25),
    ("Hora extra nocturna (75%)", 1.75),
    ("Recargo nocturno (35%)", 1.35),
    ("Hora extra dominical/festiva diurna (100%)", 2.00),
    ("Recargo dominical/festivo diurno (75%)", 1.75),
    ("Hora extra nocturna dominical/festiva (110%)", 2.10),
    ("Recargo dominical/festivo nocturno (110%)", 2.10)
]

def leer_tipo_contrato() -> int:
    """
    Solicita al usuario el tipo de contrato (1 o 2) y valida la entrada:
      1 -> Tiempo completo
      2 -> Medio tiempo
    """
    while True:
        try:
            valor = int(input("Ingrese el tipo de contrato (1 - Tiempo completo, 2 - Medio tiempo): ").strip())
            if valor in [1, 2]:
                return valor
            else:
                print("Error: Debe ingresar '1' para tiempo completo o '2' para medio tiempo.")
        except ValueError:
            print("Error: Debe ingresar un número entero (1 o 2).")

def leer_entero_no_negativo(mensaje: str) -> int:
    """
    Solicita al usuario un número entero no negativo y valida que la entrada sea correcta.
    """
    while True:
        try:
            valor = int(input(mensaje).strip())
            if valor >= 0:
                return valor
            else:
                print("Error: No se permiten números negativos.")
        except ValueError:
            print("Error: Ingrese un número entero válido (>= 0).")

def nominaDocente(tipo_contrato, horas_extra_diurna, horas_extra_nocturna, recargo_nocturno, 
                  horas_extra_dominical_diurna, recargo_dominical_diurno, horas_extra_nocturna_dominical, 
                  recargo_dominical_nocturno):
    """
    Calcula el pago total de un docente incluyendo horas extras y recargos.
    
    Parámetros:
    tipo_contrato (int): 1 si es tiempo completo, 2 si es medio tiempo
    horas_extra_diurna (int): Cantidad de horas extra diurnas trabajadas
    horas_extra_nocturna (int): Cantidad de horas extra nocturnas trabajadas
    recargo_nocturno (int): Cantidad de horas con recargo nocturno
    horas_extra_dominical_diurna (int): Cantidad de horas extra dominical/festiva diurna
    recargo_dominical_diurno (int): Cantidad de horas con recargo dominical/festivo diurno
    horas_extra_nocturna_dominical (int): Cantidad de horas extra nocturna dominical/festiva
    recargo_dominical_nocturno (int): Cantidad de horas con recargo dominical/festivo nocturno
    
    Retorna:
    dict: Resultado con salario base, pago por horas extras, descuentos y pago neto.
    """
    
    # Definir la base salarial y hora base según el tipo de contrato
    if tipo_contrato == 1:
        base_salary = SALARIO_MINIMO_2025
        hora_base = VALOR_HORA_ORDINARIA
    elif tipo_contrato == 2:
        base_salary = SALARIO_MINIMO_2025 / 2
        hora_base = VALOR_HORA_ORDINARIA
    else:
        raise ValueError("Tipo de contrato inválido. Use 1 para tiempo completo o 2 para medio tiempo.")

    # Calcular el pago por cada tipo de hora extra/recargo
    pago_extras = 0.0
    pago_extras += horas_extra_diurna * hora_base * 1.25
    pago_extras += horas_extra_nocturna * hora_base * 1.75
    pago_extras += recargo_nocturno * hora_base * 1.35
    pago_extras += horas_extra_dominical_diurna * hora_base * 2.00
    pago_extras += recargo_dominical_diurno * hora_base * 1.75
    pago_extras += horas_extra_nocturna_dominical * hora_base * 2.10
    pago_extras += recargo_dominical_nocturno * hora_base * 2.10

    # Sumar el salario base con el pago de horas extras
    pago_total_bruto = base_salary + pago_extras

    # Calcular los descuentos de salud y pensión (4% cada uno)
    descuento_salud = pago_total_bruto * PORC_SALUD
    descuento_pension = pago_total_bruto * PORC_PENSION

    # Calcular el pago neto
    pago_neto = pago_total_bruto - (descuento_salud + descuento_pension)

    # Devolver los resultados en un diccionario
    return {
        "base_salario": round(base_salary, 2),
        "pago_extras": round(pago_extras, 2),
        "pago_total_bruto": round(pago_total_bruto, 2),
        "descuento_salud": round(descuento_salud, 2),
        "descuento_pension": round(descuento_pension, 2),
        "pago_neto": round(pago_neto, 2)
    }

# Ejemplo de uso de la función
if __name__ == "__main__":
    # Llamar a la función con ejemplo de valores
    tipo_contrato = leer_tipo_contrato()

    horas_extra_diurna = leer_entero_no_negativo("Ingrese la cantidad de horas extra diurnas (25%): ")
    horas_extra_nocturna = leer_entero_no_negativo("Ingrese la cantidad de horas extra nocturnas (75%): ")
    recargo_nocturno = leer_entero_no_negativo("Ingrese la cantidad de recargo nocturno (35%): ")
    horas_extra_dominical_diurna = leer_entero_no_negativo("Ingrese la cantidad de horas extra dominical diurna (100%): ")
    recargo_dominical_diurno = leer_entero_no_negativo("Ingrese la cantidad de recargo dominical diurno (75%): ")
    horas_extra_nocturna_dominical = leer_entero_no_negativo("Ingrese la cantidad de horas extra nocturna dominical (110%): ")
    recargo_dominical_nocturno = leer_entero_no_negativo("Ingrese la cantidad de recargo dominical nocturno (110%): ")

    # Llamar a la función nominaDocente
    resultado = nominaDocente(
        tipo_contrato,
        horas_extra_diurna,
        horas_extra_nocturna,
        recargo_nocturno,
        horas_extra_dominical_diurna,
        recargo_dominical_diurno,
        horas_extra_nocturna_dominical,
        recargo_dominical_nocturno
    )
    
    # Mostrar los resultados
    print("\n===== Resultados =====")
    for clave, valor in resultado.items():
        print(f"{clave}: {valor}")

