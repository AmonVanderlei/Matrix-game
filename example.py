from jogomatriz import JogoMatriz, JogadorHumano, JogadorComputador

p1 = JogadorHumano("Irineia")
p2 = JogadorComputador("Irineu", "aleatoria")
jv = JogoMatriz(p1, p2)
jv.jogar()
