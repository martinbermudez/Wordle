from colorama import init
import random
init()


colors = {
    'green': '\033[92m',
    'yellow': '\033[93m',
    'grey': "\033[90m",
    'ENDC': '\033[0m'
}

def color_letter(letter, color):
    return colors[color] + letter + colors["ENDC"]

word_list = ["juego", "salto", "cañon", "suelo", "patio"]

# Iniciar el tablero
print("____________WORDLE!____________")

win = False
word = word_list[random.randint(0,len(word_list))]
print(word)
board = []
for i in range(6):
    board.append(['_' for l in range(5)])

game_loop = 0

while not win and (game_loop < len(word)):
    text = input('')
    while len(text) != len(word):
        print(f"la palabra debe tener {len(word)} caracteres.")
        text = input('')

    #win logic
    if word == text:
        board[game_loop] = [l for l in text]
        win = True
    # letra en la palabra
    else:
        test_line = []
        for j in range(len(text)):
            if text[j] == word[j]:
                test_line.append(color_letter(text[j], "green"))
            elif text[j] in word:
               test_line.append(color_letter(text[j], "yellow"))
            else:
                test_line.append(color_letter(text[j], "grey"))
         
        board[game_loop] = test_line

    #Dibujar tablero
    for i in range(5):
        print(" ".join(board[i]))
    game_loop += 1

#Resultado
if win:
    print(f"GANASTE! la palabra era {word}.")
else:
    print(f"te quedaste sin intentos! la palabra era {word}.")
