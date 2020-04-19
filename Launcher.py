# Pygame-Modul importieren.
import pygame

# Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.
import Game
from Game import main

# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.
if __name__ == '__main__':
    # Unsere Main-Funktion aufrufen.
    Game.main()

