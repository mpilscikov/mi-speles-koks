import tkinter as tk
from game_ui import GameUI


# UI testēšana
def main():
    root = tk.Tk()
    app = GameUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()