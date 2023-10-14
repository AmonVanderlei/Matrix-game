# Jogo da Velha

Jogo da velha de matrizes com a opção de enfrentar o computador.

## Sumário

- [Regras](#regras)
- [Instalação](#instalação)
- [Uso](#uso)
- [Licença](#licença)

## Regras

* O primeiro jogador será o 1.
* O segundo jogador será o 0.
* Os dois jogam alternadamente até preencher todo o tabuleiro.
* Se o determinante da matriz 3x3 formada pelo tabuleiro for igual a 0, o segundo jogador ganha, se for diferente de 0, o primeiro jogador ganha.

## Instalação

Para instalar execute:

```bash
python setup.py install
```

## Uso

Exemplo de uso:

```python
from jogomatriz import JogoMatriz, JogadorHumano, JogadorComputador

p1 = JogadorHumano("Irineia")
p2 = JogadorComputador("Irineu", "aleatoria")
jv = JogoMatriz(p1, p2)
jv.jogar()

```

## Licença

> Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

##### Made by Amon Vanderlei
