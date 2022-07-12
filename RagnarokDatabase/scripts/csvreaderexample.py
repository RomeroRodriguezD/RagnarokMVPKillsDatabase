from RagnarokDatabase.models import MVP
import csv

def run():
    fhand= open('RagnarokDatabase/scripts/Lista MVP.csv')
    reader = csv.reader(fhand)
    next(reader) # Avanza más allá de las cabeceras

    # Aquí el ejemplo borra los items con app.models.all().delete()

    for row in reader:
        print(row)
        #b, created = MVP.objects.get_or_create(name=row[1])
        c = MVP(name=row[0])
        c.save()
    print('MVP Database Update Done!')