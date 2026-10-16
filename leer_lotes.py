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

def main():
    lotes = leer_lotes("lotes.csv")
    totales = total_turno(lotes)
    for turno, kg in totales.items():
        print(f"{turno}: {kg} kg")
    total_pellet = 0
    for lote in lotes:
        total_pellet += float(lote["kg_pellet"])

    peor_lote, menor_rendimiento = encontrar_peor_lote(lotes)
    print(f"Total de pellet producido: {total_pellet} kg")
    print(f"Peor lote: {peor_lote} ({menor_rendimiento:.1f} %)")


if __name__ == "__main__":
    main()