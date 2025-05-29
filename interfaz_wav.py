# audio_gui/interface.py

import subprocess
import sys
import importlib.util
import platform
import os
import numpy as np
import matplotlib.pyplot as plt
import wave
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import scipy.signal  

def install_if_missing(package, import_name=None):
    """Instala el paquete si no está presente en el entorno."""
    import_name = import_name or package
    if importlib.util.find_spec(import_name) is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Instalación de librerías necesarias
install_if_missing("numpy")
install_if_missing("matplotlib")
install_if_missing("pillow")
install_if_missing("scipy")  

# Verificar entorno de ejecución en Windows
if platform.system() == "Windows":
    import winsound
else:
    print("Advertencia: 'winsound' solo está disponible en Windows.")

class AudioIterador:
    """Iterador personalizado para recorrer datos de audio en bloques."""
    def __init__(self, audio_data, block_size=1024):
        self.audio_data = audio_data
        self.block_size = block_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.audio_data):
            raise StopIteration
        block = self.audio_data[self.index:self.index + self.block_size]
        self.index += self.block_size
        return block

class AudioApp:
    """Aplicación gráfica para visualizar y analizar audio WAV."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Interfaz Gráfica de la Onda Sonora")

        self.wav_file_name = "u.wav"
        self.audio_data = None
        self.sampling_rate = None
        self.time = None

        self.fig, self.ax = plt.subplots(figsize=(10, 4))

        self.load_audio()
        self.plot_audio()
        self.create_widgets()

    def load_audio(self):
        """Carga los datos del archivo WAV y los normaliza."""
        try:
            with wave.open(self.wav_file_name, "rb") as wave_file:
                self.sampling_rate = wave_file.getframerate()
                self.audio_data = np.frombuffer(
                    wave_file.readframes(-1), dtype=np.int16
                )

            self.audio_data = self.audio_data / np.max(np.abs(self.audio_data))

            self.time = np.linspace(
                0,
                len(self.audio_data) / self.sampling_rate,
                num=len(self.audio_data)
            )
        except Exception as e:
            print(f"Error al cargar audio: {e}")

    def plot_audio(self):
        """Dibuja la forma de onda del audio."""
        self.ax.plot(self.time, self.audio_data, color="b")
        self.ax.set_xlabel("Tiempo [s]")
        self.ax.set_ylabel("Amplitud")
        self.ax.set_title("Onda Sonora")
        self.ax.grid()

    def guardar_imagen_completa(self):
        """Guarda el gráfico automáticamente en formato PNG."""
        archivo_guardado = "onda_sonora.png"
        self.fig.savefig(archivo_guardado)
        print(f"Imagen guardada automáticamente en: {archivo_guardado}")

    def reproducir_audio(self):
        """Reproduce el archivo WAV."""
        try:
            winsound.PlaySound(self.wav_file_name, winsound.SND_FILENAME)
        except Exception as e:
            print(f"Error reproduciendo audio: {e}")

    def analizar_frecuencia(self):
        """Realiza un análisis de frecuencia con FFT."""
        freqs, spectrum = scipy.signal.welch(self.audio_data, self.sampling_rate)
        plt.figure(figsize=(8, 4))
        plt.semilogy(freqs, spectrum)
        plt.xlabel("Frecuencia [Hz]")
        plt.ylabel("Densidad espectral")
        plt.title("Análisis de Frecuencia (FFT)")
        plt.grid()
        plt.show()

    def create_widgets(self):
        """Crea los componentes visuales."""
        canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        canvas.get_tk_widget().pack()

        tk.Button(self.root, text="Reproducir Audio", command=self.reproducir_audio).pack()
        tk.Button(self.root, text="Analizar Frecuencia", command=self.analizar_frecuencia).pack()

    def run(self):
        """Ejecuta la aplicación."""
        self.root.mainloop()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = AudioApp()
    app.guardar_imagen_completa()
    app.run()
