import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from FCFSAlgorithm import fcfs
from SSTFAlgorithm import sstf
from SCANAlgorithm import scan
from C_SCANAlgorithm import c_scan
from LOOKAlgorithm import look
from C_LOOKAlgorithm import c_look


def run_algorithm():
    requests_str = requests_entry.get()
    requests = list(map(int, requests_str.split(',')))
    start = int(start_entry.get())
    direction = direction_combobox.get()
    algorithm = algorithm_combobox.get()

    if algorithm == "FCFS":
        seek_sequence, total_seek_time = fcfs(requests, start)
    elif algorithm == "SSTF":
        seek_sequence, total_seek_time = sstf(requests, start)
    elif algorithm == "SCAN":
        seek_sequence, total_seek_time = scan(requests, start, direction)    
    elif algorithm == "C-SCAN":
        seek_sequence, total_seek_time = c_scan(requests, start, direction)
    elif algorithm == "LOOK":
        seek_sequence, total_seek_time = look(requests, start, direction)
    elif algorithm == "C-LOOK":
        seek_sequence, total_seek_time = c_look(requests, start, direction)

    total_seek_time_label.config(text="Total Seek Time: " + str(total_seek_time))
    seek_sequence_label.config(text="Seek Sequence: " + str(seek_sequence))
    plot_disk_movement(seek_sequence, start)

def plot_disk_movement(seek_sequence, start):
    plt.figure(figsize=(10, 6))
    plt.plot(seek_sequence, range(len(seek_sequence)), marker='o', linestyle='-')
    plt.title("Disk Head Movement (" + algorithm_combobox.get() + " Algorithm)")
    plt.xlabel("Track")
    plt.ylabel("Time")
    plt.yticks(range(len(seek_sequence)), seek_sequence)
    plt.axhline(y=seek_sequence.index(start), color='r', linestyle='--', label="Start Position")
    plt.legend()
    plt.grid(True)
    plt.show()

# Create GUI
root = tk.Tk()
root.title("Disk Scheduling Algorithms")

# Requests Entry
requests_label = ttk.Label(root, text="Requests (comma-separated):")
requests_label.grid(row=0, column=0, padx=5, pady=5)
requests_entry = ttk.Entry(root)
requests_entry.grid(row=0, column=1, padx=5, pady=5)

# Start Position Entry
start_label = ttk.Label(root, text="Start Position:")
start_label.grid(row=1, column=0, padx=5, pady=5)
start_entry = ttk.Entry(root)
start_entry.grid(row=1, column=1, padx=5, pady=5)

# Direction Combobox
direction_label = ttk.Label(root, text="Direction:")
direction_label.grid(row=2, column=0, padx=5, pady=5)
direction_combobox = ttk.Combobox(root, values=["outward", "inward"])
direction_combobox.grid(row=2, column=1, padx=5, pady=5)

# Algorithm Combobox
algorithm_label = ttk.Label(root, text="Algorithm:")
algorithm_label.grid(row=3, column=0, padx=5, pady=5)
algorithm_combobox = ttk.Combobox(root, values=["FCFS", "SSTF", "SCAN", "C-SCAN", "LOOK", "C-LOOK"])
algorithm_combobox.grid(row=3, column=1, padx=5, pady=5)

# Total Seek Time Label
total_seek_time_label = ttk.Label(root, text="")
total_seek_time_label.grid(row=4, columnspan=2, padx=5, pady=5)

# Seek Sequence Label
seek_sequence_label = ttk.Label(root, text="")
seek_sequence_label.grid(row=5, columnspan=2, padx=5, pady=5)

# Run Button
run_button = ttk.Button(root, text="Run Algorithm", command=run_algorithm)
run_button.grid(row=6, columnspan=2, padx=5, pady=5)

root.mainloop()
