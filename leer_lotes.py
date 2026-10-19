import csv


def leer_lotes(ruta):
    with open(ruta, newline="", encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))


def calcular_rendimiento(kg_pellet, kg_entrada):
    return kg_pellet / kg_entrada * 100


def encontrar_peor_lote(lotes):
    peor_lote = None
    menor_rendimiento = None
    for lote in lotes:
        rendimiento = calcular_rendimiento(
            float(lote["kg_pellet"]), float(lote["kg_entrada"])
        )
        if menor_rendimiento is None or rendimiento < menor_rendimiento:
            menor_rendimiento = rendimiento
            peor_lote = lote["lote"]
    return peor_lote, menor_rendimiento


def total_turno(lotes):
    totales = {}
    for lote in lotes:
        turno = lote["turno"]
        totales[turno] = totales.get(turno, 0) + float(lote["kg_pellet"])
    return totales


def validar_lote(lote):
    try:
        kg_entrada = float(lote["kg_entrada"])
        kg_pellet = float(lote["kg_pellet"])
    except ValueError:
        raise ValueError(f"Lote {lote['lote']}: los kilos no son números")

    if kg_entrada <= 0:
        raise ValueError(f"Lote {lote['lote']}: kg_entrada debe ser mayor que 0")
    if kg_pellet < 0:
        raise ValueError(f"Lote {lote['lote']}: kg_pellet no puede ser negativo")


def main():
    lotes = leer_lotes("lotes_con_errores.csv")

    lotes_validos = []
    errores = []
    for lote in lotes:
        try:
            validar_lote(lote)
            lotes_validos.append(lote)
        except ValueError as error:
            errores.append(str(error))

    total_pellet = 0
    for lote in lotes_validos:
        total_pellet += float(lote["kg_pellet"])

    totales = total_turno(lotes_validos)
    for turno, kg in totales.items():
        print(f"{turno}: {kg} kg")

    peor_lote, menor_rendimiento = encontrar_peor_lote(lotes_validos)
    print(f"Total de pellet producido: {total_pellet} kg")
    print(f"Peor lote: {peor_lote} ({menor_rendimiento:.1f} %)")

    if errores:
        print(f"Se descartaron {len(errores)} lotes:")
        for error in errores:
            print(f"- {error}")


if __name__ == "__main__":
    main()