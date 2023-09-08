import tkinter as tk
from tkinter import ttk
import scipy.stats as stats

def calculate_cumulative_prob():
    n = int(n_entry.get())
    p = float(p_entry.get())
    x = int(x_entry.get())

    cumulative_prob = stats.binom.cdf(x, n, p)
    result_label.config(text=f'P(X ≤ {x}) = {cumulative_prob:.4f}')

root = tk.Tk()
root.title("Cumulative Binomial Distribution Calculator")

n_label = ttk.Label(root, text="Number of Trials (n):")
n_label.pack()
n_entry = ttk.Entry(root)
n_entry.pack()

p_label = ttk.Label(root, text="Probability of Success (p):")
p_label.pack()
p_entry = ttk.Entry(root)
p_entry.pack()

x_label = ttk.Label(root, text="Value for Cumulative Distribution (x):")
x_label.pack()
x_entry = ttk.Entry(root)
x_entry.pack()

calculate_button = ttk.Button(root, text="Calculate", command=calculate_cumulative_prob)
calculate_button.pack()

result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()
