"""
wordle.py
    _ _ _ _ _ _
    _ _ _ _ _ _
    _ _ _ _ _ _
    _ _ _ _ _ _
    _ _ _ _ _ _

Tareas:
    palabra == intento -> ganar.
    letra en la palabra -> ayuda.
    letra no esta en la palabra -> no existe.

    palabra dentro de la lista posible de palabras.
"""

# Iniciar el tablero
print("____________WORDLE!____________")
word = 'trineo'
board = []
for i in range(6):
    board.append(['_' for l in range(5)])

text = input('')
while len(text) != len(word):
    print(f"la palabra debe tener {len(word)} caracteres.")
    text = input('')

# Dibujar tablero
for i in range(6):
    print(" ".join(board[i]))

