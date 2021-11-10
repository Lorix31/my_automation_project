from EXTRA.OOP.g_clase_cont import Cont

# cream obiecte de tip cont
cont1 = Cont('Lore R', 2881231, 'RO001', 200)
cont2 = Cont('Irinel R', 1870107, 'RO002', 500)

cont1.interogare_sold() #=>Soldul titularului Lore R este de 200 euro
cont2.interogare_sold() #=>Soldul titularului Irinel R este de 500 euro

cont1.alimentare_cont(100)
cont1.interogare_sold() #=> Soldul titularului Lore R este de 300 euro

cont2.alimentare_cont(300)
cont2.interogare_sold() #=>Soldul titularului Irinel R este de 800 euro

cont1.retragere_numerar(100) #=>Soldul titularului Lore R este de 200 euro
cont1.interogare_sold()

cont2.retragere_numerar(2000) #=>Fonduri insuficiente / Ai vrut sa retragi 2000 dar mai ai in cont 500
