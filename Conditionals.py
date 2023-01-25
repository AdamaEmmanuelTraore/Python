# METEO 1
temp = 25
if temp < 35:
    print('\n Che bella giornata\n')
else:
    print("Meglio stare all'ombra\n")

# METEO 2
temp = 75
stato = 'soleggiato'
if temp < 80 and stato != 'pioggia':
    print('Andiamo fuori!!!\n')
else:
    print('Stiamo dentro casa!\n')