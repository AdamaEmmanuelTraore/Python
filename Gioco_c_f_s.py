# [ita] GIOCO: CARTA, FORBICE E SASSO / [fr] JEUX: PIERRE, FEUILLE, CISEAUX
## [ita] Ps: POTEVO USARE L'ISTRUZIONE WHILE INVECE DELLA CONDIZIONE IF/ELSE PER RENDERLO PIU SMART / [fr] Ps: JE POUVAIS UTILISER L'INSTRUCTIONS WHILE AU LIEU DE LA CONDITION IF/ELSE POUR RENDRE LE JEUX PLUS INTELLIGENT
import random


user = input('Inserisci il tuo nome\n')
print('\n Iniziamo!\n')
print('Ora è il turno della macchina\n')
scelte = ['carta', 'forbice', 'sasso']
scelta_macchina = random.choice(scelte)
print('La macchina ha scelto\n')
x = input('Ora tocca a te ' + str(user) + ' cosa scegli fra carta, forbice, sasso?\n')
if x == scelta_macchina and x != scelte[1] and x != scelte[2]:
    print('\n Pareggio, la macchina ha scelto ' + str(scelta_macchina) + ' e tu hai scelto ' + str(x) + ' continuate a giocare\n')
elif x == scelta_macchina and x != scelte[0] and x != scelte[2]:
    print('\n Pareggio, la macchina ha scelto ' + str(scelta_macchina) + ' e tu hai scelto ' + str(x) + ' continuate a giocare\n')
elif x == scelta_macchina and x != scelte[0] and x != scelte[1]:
    print('\n Pareggio, la macchina ha scelto ' + str(scelta_macchina) + ' e tu hai scelto ' + str(x) + ' continuate a giocare\n')
elif x == scelte[0] and scelta_macchina == scelte[1]:
    print('\n la macchina ha scelto ' + scelta_macchina + ' e tu hai scelto ' + str(x) + ' GAME OVER, ' + str(user) + 'hai perso contro la macchina!\n')
elif x == scelte[0] and scelta_macchina == scelte[2]:
    print('\n la macchina ha scelto ' + scelta_macchina + ' e tu hai scelto ' + str(x) + ' Complimenti ' + str(user) + ', hai battuto la macchina!\n')
elif x == scelte[1] and scelta_macchina == scelte[0]:
    print('\n la macchina ha scelto ' + scelta_macchina + ' e tu hai scelto ' + str(x) + ' Complimenti ' + str(user) + ', hai battuto la macchina!\n')
elif x == scelte[1] and scelta_macchina == scelte[2]:
    print('\n la macchina ha scelto ' + scelta_macchina + ' e tu hai scelto ' + str(x) + ' GAME OVER, ' + str(user) + 'hai perso contro la macchina!\n')
elif x == scelte[2] and scelta_macchina == scelte[0]:
    print('\n la macchina ha scelto ' + scelta_macchina + ' e tu hai scelto ' + str(x) + ' GAME OVER, ' + str(user) + 'hai perso contro la macchina!\n')
elif x == scelte[2] and scelta_macchina == scelte[1]:
    print('\n la macchina ha scelto ' + scelta_macchina + ' e tu hai scelto ' + str(x) + ' Complimenti ' + str(user) + ', hai battuto la macchina!\n')