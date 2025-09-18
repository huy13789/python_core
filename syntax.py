import tkinter as tk
from tkinter import messagebox
import random

class DoanSoGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("🎯 Trò chơi đoán số")
        self.master.geometry("400x250")
        self.so_bi_mat = random.randint(1, 100)
        self.so_lan_doan = 0

        self.label = tk.Label(master, text="Mình đã chọn một số từ 1 đến 100.\nHãy nhập số bạn đoán:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Arial", 14))
        self.entry.pack(pady=5)

        self.button = tk.Button(master, text="Đoán", command=self.ktra_doan, font=("Arial", 14))
        self.button.pack(pady=10)

        self.result = tk.Label(master, text="", font=("Arial", 12))
        self.result.pack(pady=5)

        self.master.bind('<Return>', lambda event: self.ktra_doan())

    def ktra_doan(self):
        try:
            doan = int(self.entry.get())
            self.so_lan_doan += 1

            if doan < self.so_bi_mat:
                self.result.config(text="🔻 Số bạn đoán nhỏ hơn số bí mật.")
            elif doan > self.so_bi_mat:
                self.result.config(text="🔺 Số bạn đoán lớn hơn số bí mật.")
            else:
                messagebox.showinfo("🎉 Chúc mừng!", f"Bạn đã đoán đúng số {self.so_bi_mat} sau {self.so_lan_doan} lần!")
                self.reset_game()
        except ValueError:
            self.result.config(text="⚠️ Vui lòng nhập một số nguyên hợp lệ.")

    def reset_game(self):
        self.so_bi_mat = random.randint(1, 100)
        self.so_lan_doan = 0
        self.entry.delete(0, tk.END)
        self.result.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = DoanSoGUI(root)
    root.mainloop()
