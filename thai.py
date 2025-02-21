import tkinter as tk
import random

# List of Thai consonants and their names
consonants = [
    ("ก", "gor kai"),
    ("ข", "khor khai"),
    ("ฃ", "khor khuat"),
    ("ค", "khor khon"),
    ("ฅ", "khor ra khang"),
    ("ฆ", "khor khok"),
    ("ง", "ngor ngu"),
    ("จ", "jor jan"),
    ("ฉ", "chor ching"),
    ("ช", "chor chang"),
    ("ซ", "sor so"),
    ("ฌ", "chor chao"),
    ("ญ", "yor ying"),
    ("ฎ", "dor cha da"),
    ("ฏ", "tor patak"),
    ("ฐ", "thor than"),
    ("ฑ", "thor thong"),
    ("ฒ", "thor thung"),
    ("ณ", "nor nen"),
    ("ด", "dor dek"),
    ("ต", "tor tao"),
    ("ถ", "thor thung"),
    ("ท", "thor thahan"),
    ("ธ", "thor thong"),
    ("น", "nor nu"),
    ("บ", "bor bai mai"),
    ("ป", "por pla"),
    ("ผ", "phor phai"),
    ("ฝ", "for fang"),
    ("พ", "phor phan"),
    ("ฟ", "for fan"),
    ("ภ", "phor phap"),
    ("ม", "mor ma"),
    ("ย", "yor yak"),
    ("ร", "ror ruea"),
    ("ล", "lor ling"),
    ("ว", "wor waen"),
    ("ศ", "sor sala"),
    ("ษ", "sor seu"),
    ("ส", "sor sam"),
    ("ห", "hor hiip"),
    ("ฬ", "lor ching"),
    ("อ", "or ang"),
    ("ฮ", "hor nok hak")
]

class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcard Game")
        self.root.geometry("400x400")

        # Card Frame
        self.card_frame = tk.Frame(self.root)
        self.card_frame.pack(pady=20)

        self.card_label = tk.Label(self.card_frame, text="", font=("Arial", 80), width=10, height=5, relief="solid")
        self.card_label.pack()

        # Flip Button
        self.flip_button = tk.Button(self.root, text="Flip Card", command=self.flip_card)
        self.flip_button.pack(pady=20)

        # Initialize the card
        self.current_consonant = None
        self.show_consonant()

    def show_consonant(self):
        self.current_consonant = random.choice(consonants)
        self.card_label.config(text=self.current_consonant[0])

    def flip_card(self):
        if self.card_label.cget("text") == self.current_consonant[0]:
            self.card_label.config(text=self.current_consonant[1])
        else:
            self.show_consonant()

# Create the main window
root = tk.Tk()
game = FlashcardGame(root)

# Run the game
root.mainloop()
