import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation

class AplicacionGrafica:
    def __init__(self, master):
        self.master = master
        self.master.title("Gráfica de Barras Animada")
        
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña de gráfica
        self.tab_grafica = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_grafica, text="Gráfica")
        
        # Pestaña de datos
        self.tab_datos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_datos, text="Datos")
        
        self.crear_grafica()
        self.crear_tabla_datos()
    
    def crear_grafica(self):
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.tab_grafica)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.anim = animation.FuncAnimation(self.fig, self.actualizar_grafica, interval=1000)
    
    def crear_tabla_datos(self):
        self.df = pd.DataFrame({'Categoría': ['A', 'B', 'C', 'D'], 'Valor': [10, 20, 15, 25]})
        self.table = ttk.Treeview(self.tab_datos)
        self.table['columns'] = list(self.df.columns)
        self.table['show'] = 'headings'
        
        for column in self.table['columns']:
            self.table.heading(column, text=column)
        
        for i, row in self.df.iterrows():
            self.table.insert('', 'end', values=list(row))
        
        self.table.pack(fill=tk.BOTH, expand=True)
        
        # Botón para actualizar datos
        ttk.Button(self.tab_datos, text="Actualizar Datos", command=self.actualizar_datos).pack()
    
    def actualizar_datos(self):
        # Aquí iría la lógica para actualizar los datos desde Excel
        # Por simplicidad, solo actualizamos los datos de manera aleatoria
        self.df['Valor'] = np.random.randint(1, 50, size=len(self.df))
        self.table.delete(*self.table.get_children())
        for i, row in self.df.iterrows():
            self.table.insert('', 'end', values=list(row))
    
    def actualizar_grafica(self, i):
        self.ax.clear()
        self.ax.bar(self.df['Categoría'], self.df['Valor'])
        self.ax.set_ylim(0, 50)  # Ajusta este valor según tus necesidades

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGrafica(root)
    root.mainloop()
