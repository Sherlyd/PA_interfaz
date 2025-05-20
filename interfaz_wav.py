# audio_gui/interface.py

# Verificar e instalar librerías necesarias
import subprocess
import sys
import importlib.util
import platform

def install_if_missing(package, import_name=None):
    """Instala el paquete si no está presente en el entorno."""
    import_name = import_name or package
    if importlib.util.find_spec(import_name) is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Instalar librerías externas que requieren pip
install_if_missing("numpy")
install_if_missing("matplotlib")

# Notas sobre otros módulos:
# - os, sys, subprocess, wave: vienen con la biblioteca estándar de Python (no se instalan)
# - tkinter: viene por defecto en Windows y macOS. En Linux instalar con: sudo apt install python3-tk
# - winsound: solo está disponible en Windows

# ==== IMPORTACIONES ====
import os
import numpy as np
import matplotlib.pyplot as plt
import wave
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Verificar que se esté ejecutando en Windows antes de importar winsound
if platform.system() == "Windows":
    import winsound
else:
    print("Advertencia: 'winsound' solo está disponible en Windows. La reproducción de audio no funcionará.")


class AudioApp:
    """
    Clase que define una aplicación gráfica para visualizar y reproducir
    archivos de audio en formato WAV, utilizando Tkinter y Matplotlib.
    """

    def __init__(self):
        # Inicialización de la ventana principal
        self.root = tk.Tk()
        self.root.title("Interfaz Gráfica de la Onda Sonora")

        # Archivo de audio por defecto
        self.wav_file_name = "u.wav"

        # Variables para almacenar datos de audio y tiempo
        self.audio_data = None
        self.sampling_rate = None
        self.time = None

        # Crear figura de Matplotlib para graficar
        self.fig, self.ax = plt.subplots(figsize=(10, 4))

        # Cargar, graficar audio y crear widgets de la GUI
        self.load_audio()
        self.plot_audio()
        self.create_widgets()

    def load_audio(self):
        """
        Carga los datos del archivo WAV y los normaliza.
        Calcula también el vector de tiempo para graficar.
        """
        try:
            with wave.open(self.wav_file_name, "rb") as wave_file:
                self.sampling_rate = wave_file.getframerate()
                self.audio_data = np.frombuffer(
                    wave_file.readframes(-1), dtype=np.int16
                )

            # Normalización de la señal de audio (valores entre -1 y 1)
            self.audio_data = self.audio_data / np.max(np.abs(self.audio_data))

            # Generación del vector de tiempo correspondiente a la señal
            self.time = np.linspace(
                0,
                len(self.audio_data) / self.sampling_rate,
                num=len(self.audio_data)
            )
        except Exception as e:
            print(f"Error loading audio: {e}")

    def plot_audio(self):
        """
        Dibuja la forma de onda del audio en la figura de Matplotlib.
        """
        self.ax.plot(self.time, self.audio_data, color="b")
        self.ax.set_xlabel("Tiempo [s]")
        self.ax.set_ylabel("Amplitud")
        self.ax.set_title("Onda Sonora")
        self.ax.grid()

    def create_widgets(self):
        """
        Crea los componentes visuales (widgets) de la interfaz,
        incluyendo el gráfico, botones de guardar imagen y reproducir audio.
        """
        # Embebe el gráfico en la interfaz Tkinter
        canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

        # Botón para guardar imagen
        tk.Button(self.root, text="Guardar Imagen Completa",
                  command=self.guardar_imagen_completa).pack()

        # Botón para reproducir audio
        tk.Button(self.root, text="Reproducir Audio",
                  command=self.reproducir_audio).pack()

    def guardar_imagen_completa(self):
        """
        Permite al usuario guardar la imagen del gráfico como archivo PNG.
        """
        archivo_guardado = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Imágenes PNG", "*.png")],
            title="Guardar Imagen Completa"
        )
        if archivo_guardado:
            self.fig.savefig(archivo_guardado)
            print(f"Imagen guardada: {archivo_guardado}")

    def reproducir_audio(self):
        """
        Reproduce el archivo WAV cargado utilizando la biblioteca winsound.
        """
        try:
            winsound.PlaySound(self.wav_file_name, winsound.SND_FILENAME)
        except Exception as e:
            print(f"Error reproduciendo audio: {e}")

    def run(self):
        """
        Inicia el bucle principal de la interfaz gráfica (loop de eventos).
        """
        self.root.mainloop()

# ejecutar la aplicación
if __name__ == "__main__":
    app = AudioApp()
    app.run()
