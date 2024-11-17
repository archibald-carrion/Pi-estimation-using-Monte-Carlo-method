import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from monte_carlo_method import monte_carlo_pi

class Application:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Monte Carlo Pi Approximation")
        self.window.geometry("800x600")

        # block resizing of window
        self.window.resizable(False, False)
        
        # Configure grid
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)
        
        # Bind the closing event
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Input frame
        self.input_frame = ctk.CTkFrame(self.window)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        # Input widgets
        self.points_label = ctk.CTkLabel(self.input_frame, text="Number of Points:")
        self.points_label.grid(row=0, column=0, padx=5, pady=5)
        
        # Entry widget for number of points
        self.points_entry = ctk.CTkEntry(self.input_frame)
        self.points_entry.grid(row=0, column=1, padx=5, pady=5)
        self.points_entry.insert(0, "1000") # Default value of 1000
        
        # Run button widget
        self.run_button = ctk.CTkButton(self.input_frame, text="Run Simulation", command=self.run_simulation)
        self.run_button.grid(row=0, column=2, padx=5, pady=5)
        
        # Result label
        self.result_label = ctk.CTkLabel(self.input_frame, text="Estimated π: --")
        self.result_label.grid(row=0, column=3, padx=5, pady=5)
        
        # Graph frame
        self.graph_frame = ctk.CTkFrame(self.window)
        self.graph_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        # Create matplotlib figure in dark mode
        plt.style.use('dark_background')
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(fill='both', expand=True)
        
        # Initial simulation
        self.run_simulation()
    
    # Function to properly close the application window
    def on_closing(self):
        # Properly close matplotlib figure
        plt.close(self.fig)
        
        # Destroy all widgets
        for widget in self.window.winfo_children():
            widget.destroy()
        
        # note: I never had to use this before, but for some reason the program was not closing properly without it
        # Cancel all pending after events
        for after_id in self.window.tk.call('after', 'info'):
            self.window.after_cancel(after_id)
        
        # Destroy the window
        self.window.quit()
        self.window.destroy()
           
    def run_simulation(self):
        try:
            n_points = int(self.points_entry.get())
            if n_points <= 0:
                raise ValueError("Number of points must be positive")
            
            # Clear previous plot
            self.ax.clear()
            
            # Run simulation
            pi_approx, x_inside, y_inside, x_outside, y_outside = monte_carlo_pi(n_points)
            
            # Plot points
            self.ax.scatter(x_inside, y_inside, c='green', s=1, alpha=0.6, label='Inside')
            self.ax.scatter(x_outside, y_outside, c='red', s=1, alpha=0.6, label='Outside')
            
            # Plot circle
            circle = plt.Circle((0, 0), 1, fill=False, color='white')
            self.ax.add_artist(circle)
            
            # Plot square
            self.ax.set_xlim(-1, 1)
            self.ax.set_ylim(-1, 1)
            self.ax.grid(True)
            self.ax.set_aspect('equal')
            self.ax.legend()
            
            # Update result label
            self.result_label.configure(text=f"Estimated π: {pi_approx:.6f}")
            
            # Refresh canvas
            self.canvas.draw()
            
        except ValueError as e:
            self.result_label.configure(text="Error: Invalid input")
    
    def run(self):
        self.window.mainloop()