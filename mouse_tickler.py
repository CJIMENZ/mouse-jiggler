import tkinter as tk
from tkinter import messagebox
import pyautogui
import threading
import time

class MouseMoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Mover")
        self.root.geometry("300x250")

        # Default interval in seconds
        self.interval = 30  
        # Whether the mouse mover is running
        self.running = False
        # Countdown variable
        self.countdown = self.interval
        # Track start time for stopwatch
        self.start_time = None

        # ---- Interval Input ----
        self.interval_label = tk.Label(self.root, text="Interval (seconds):", font=("Arial", 12))
        self.interval_label.pack(pady=(10, 0))

        self.interval_entry = tk.Entry(self.root, font=("Arial", 12), width=10)
        self.interval_entry.pack()
        self.interval_entry.insert(0, str(self.interval))  # Default value

        # ---- Countdown Label ----
        self.label = tk.Label(self.root, text=f"Next move in: {self.interval} seconds", font=("Arial", 14))
        self.label.pack(pady=10)

        # ---- Stopwatch Label ----
        self.stopwatch_label = tk.Label(self.root, text="Running time: 00:00:00", font=("Arial", 12))
        self.stopwatch_label.pack(pady=10)

        # ---- Start/Stop Buttons ----
        self.start_button = tk.Button(self.root, text="Start", font=("Arial", 12), command=self.start_movement)
        self.start_button.pack(side="left", padx=20, pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", font=("Arial", 12), command=self.stop_movement, state="disabled")
        self.stop_button.pack(side="right", padx=20, pady=10)

    def move_mouse(self):
        """Move the mouse periodically and update the countdown."""
        while self.running:
            if self.countdown > 0:
                self.label.config(text=f"Next move in: {self.countdown} seconds")
                time.sleep(1)
                self.countdown -= 1
            else:
                # Get the current position and move the mouse slightly
                x, y = pyautogui.position()
                pyautogui.moveTo(x + 10, y + 10, duration=0.2)
                pyautogui.moveTo(x, y, duration=0.2)
                self.countdown = self.interval

    def start_movement(self):
        """Start the mouse movement."""
        if not self.running:
            # Read the interval from the Entry box
            try:
                self.interval = int(self.interval_entry.get())
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a valid number.")
                return
            
            # Check if the interval is positive
            if self.interval <= 0:
                messagebox.showerror("Invalid input", "Please enter a positive (non-zero) number.")
                return

            self.running = True
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")

            self.countdown = self.interval
            # Record the start time for the stopwatch
            self.start_time = time.time()

            # Start the separate thread for mouse movement
            threading.Thread(target=self.move_mouse, daemon=True).start()

            # Kick off the stopwatch updates
            self.update_stopwatch()

    def stop_movement(self):
        """Stop the mouse movement."""
        if self.running:
            self.running = False
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")
            self.label.config(text="Mouse mover stopped.")
            # Reset countdown
            self.countdown = self.interval

    def update_stopwatch(self):
        """Update the stopwatch label every second using Tkinter's after mechanism."""
        if self.running:
            elapsed = int(time.time() - self.start_time)
            # Convert elapsed time (seconds) into HH:MM:SS
            elapsed_str = time.strftime("%H:%M:%S", time.gmtime(elapsed))
            self.stopwatch_label.config(text=f"Running time: {elapsed_str}")

            # Schedule the next update in 1 second
            self.root.after(1000, self.update_stopwatch)
        else:
            # If not running, reset the stopwatch text or leave it as is
            self.stopwatch_label.config(text="Running time: 00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = MouseMoverApp(root)
    root.mainloop()