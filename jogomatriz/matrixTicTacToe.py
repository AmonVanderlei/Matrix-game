import numpy as np
from typing import List, Optional, Tuple, Union


class Tabuleiro:
    def __init__(self) -> None:
        """Inicializes an empty board.
        """
        self.casas = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        self.matrix = np.zeros((3, 3), dtype=int)
        
    def pegar_tabuleiro(self) -> List[List[int]]:
        """Return the board in a list of lists format.

        Returns:
            List[List[int]]: Each sublist is a line of the board.
        """
        return self.casas

    def marcar_casa(self, pos: Tuple[int, int], valor: int) -> None:
        """Mark an empty cell with the symbol of a player.

        Args:
            pos (Tuple[int, int]): The position of the cell.
            valor (str): The value to mark the cell.
        """
        linha = pos[0]
        coluna = pos[1]
        
        self.matrix[linha][coluna] = valor
        self.casas[linha][coluna] = valor

    def imprimir_tabuleiro(self) -> None:
        """Print the board with separators.
        """
        print(f"| {self.casas[0][0]}  {self.casas[0][1]}  {self.casas[0][2]} |")
        print(f"| {self.casas[1][0]}  {self.casas[1][1]}  {self.casas[1][2]} |")
        print(f"| {self.casas[2][0]}  {self.casas[2][1]}  {self.casas[2][2]} |")


class JogadorHumano():
    def __init__(self, nome: str) -> None:
        """Inicializes a human player.

        Args:
            nome (str): How the player will be called.
        """
        self.nome = nome

    def fazer_jogada(self, tabuleiro: Tabuleiro) -> Tuple[int, int]:
        """Asks which cell will be marked.

        Args:
            tabuleiro (Tabuleiro): Board where the cell will be marked.

        Returns:
            Tuple[int, int]: The position of the mark.
        """
        print()
        print(f"É sua vez, {self.nome}!")
        valores = list(input(
            "Digite a jogada (separada por espaço): ").strip().split())
        
        #It must have only to values
        while len(valores) != 2:
            valores = list(input(
                "Digite uma jogada válida: ").strip().split())
        
        if len(valores) == 2:
            linha, coluna = valores
        
        #Verify if the values given are valid numbers
        linha, coluna = movimento_valido(linha, coluna)
        
        tabuleiro_lista = tabuleiro.pegar_tabuleiro() 
    
        #Verify if the cell is empty
        while tabuleiro_lista[linha - 1][coluna - 1] != "-":
            linha, coluna = input(
                "Essa casa já está preenchida: ").strip().split()
            linha, coluna = movimento_valido(linha, coluna)
        
        #Takes 1 from line and column, so first cell can be (1,1) and not (0,0)
        #Makes it to be easier to the player writing the cell position
            
        return (linha - 1, coluna - 1)
    
    
class JogadorComputador():
    estrategias = ["aleatoria"]
    
    def __init__(self, nome: str, estrategia: str) -> None:
        """Verify if the strategy is valid and inicialize a computer player.

        Args:
            nome (str): How the player will be called.
            estrategia (str): Strategy that will be used.

        Raises:
            ValueError: Raises if the strategy doesn't exist.
        """        
        self.nome = nome
        
        if estrategia in JogadorComputador.estrategias:
            self.estrategia = estrategia
        else:
            raise ValueError("Estratégia inválida.")
        
    def fazer_jogada(self, tabuleiro: Tabuleiro) -> Tuple[int, int]:
        """Determine the cell according to the strategy.

        Args:
            tabuleiro (Tabuleiro): The board the game is being played.

        Returns:
            Tuple[int, int]: Cell to mark.
        """
        print()
        print(f"Vez do Computador!")
        if self.estrategia == "aleatoria":
            tabuleiro_lista = tabuleiro.pegar_tabuleiro()
            linha = np.random.choice([0, 1, 2], replace=False)
            coluna = np.random.choice([0, 1, 2], replace=False)

            while tabuleiro_lista[linha][coluna] != "-":
                linha = np.random.choice([0, 1, 2], replace=False)
                coluna = np.random.choice([0, 1, 2], replace=False)

            return (linha, coluna)


class JogoMatriz:
    def __init__(self, jogador1: Union[JogadorHumano, JogadorComputador], jogador2: Union[JogadorHumano, JogadorComputador]) -> None:
        """Inicializes a game.

        Args:
            jogador1 (Union[JogadorHumano, JogadorComputador]): The first player. Plays with 1.
            jogador2 (Union[JogadorHumano, JogadorComputador]): The second player. Plays with 0.
        """
        self.tabuleiro = Tabuleiro()
        self.jogadores = [jogador1, jogador2]
        self.turno = 0
        
    def jogar(self) -> None:
        """Runs the game's mechanics.
        """
        while self.turno < 9:
            jogador_atual, valor = self.jogador_atual()
            jogada = jogador_atual.fazer_jogada(self.tabuleiro)
            self.tabuleiro.marcar_casa(jogada, valor)
            self.tabuleiro.imprimir_tabuleiro()
            
            acabou = self.checar_fim_de_jogo()
            if acabou != None:
                print(acabou)
                return
            else:
                self.turno += 1
    
    def checar_fim_de_jogo(self) -> Optional[str]:
        """Checks if the game ended.

        Returns:
            Optional[str]: Returns a string if the game has ended.
        """
        det = np.linalg.det(self.tabuleiro.matrix)
        
        if det == 1:
            return f"Jogador {self.jogadores[0].nome} ganhou!"

        if self.turno == 8:
            return f"Jogador {self.jogadores[1].nome} ganhou!"

        return None
        
    def jogador_atual(self) -> Union[JogadorHumano, JogadorComputador]:
        """Return the Jogador object of the actual player.

        Returns:
            Union[JogadorHumano, JogadorComputador]: Jogador object of the actual player.
        """
        if self.turno % 2 == 0:
            return (self.jogadores[0], 1)
        else:
            return (self.jogadores[1], 0)


#Verify if a string is a number
def is_number(n: str) -> bool:
    try:
        n = int(n)
        return True
    except:
        return False

#Verify if the values given makes a valid move
def movimento_valido(a: str, b: str) -> Tuple[int, int]:
    while (is_number(a) != True) or (is_number(b) != True) or (
        a not in ["1", "2", "3"]) or (b not in ["1", "2", "3"]):
        #Tests if only two values are given
        try:
            inputs = input("Digite uma jogada válida: ").strip()
            a, b = inputs.split()
        
        #If there aren't two values, puts a and b as a not valid value  
        except:
            a = b = "4"
    
    return (int(a), int(b))
