import csv

with open("lotes.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    lotes = list(lector)

total_pellet = 0
menor_rendimiento = None
peor_lote = None

for lote in lotes:
    kg_pellet = float(lote["kg_pellet"])
    kg_entrada = float(lote["kg_entrada"])
    rendimiento = kg_pellet / kg_entrada * 100

    total_pellet += kg_pellet
    print(f"Lote {lote['lote']}: rendimiento {rendimiento:.1f} %")

    if menor_rendimiento is None or rendimiento < menor_rendimiento:
        menor_rendimiento = rendimiento
        peor_lote = lote["lote"]

print(f"Total de pellet producido: {total_pellet} kg")
print(f"Peor lote: {peor_lote} ({menor_rendimiento:.1f} %)")