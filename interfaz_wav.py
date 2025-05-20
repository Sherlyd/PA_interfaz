
import subprocess
import sys

# List of required libraries
required_libraries = [
    "numpy", "matplotlib", "wave", "tkinter", "pydub", "playsound"
]

def install_and_import(library):
    """Checks if a library is installed; installs it if missing."""
    try:
        __import__(library)
    except ImportError:
        print(f"Installing missing library: {library}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])

# Ensure all required libraries are installed
for lib in required_libraries:
    install_and_import(lib)

# Proceed with execution after ensuring dependencies are installed
import os
import numpy as np
import matplotlib.pyplot as plt
import wave
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pydub import AudioSegment
from playsound import playsound

print("All required libraries are installed. Proceeding with execution...")

"""version en español"""
# # Cargar el archivo WAV y extraer los datos de audio
# wav_file_name = "u.wav"
# wave_file = wave.open(wav_file_name, "rb")
# sampling_rate = wave_file.getframerate()
# audio_data = np.frombuffer(wave_file.readframes(-1), dtype=np.int16)
# wave_file.close()

# # Normalizar los datos de audio para la visualización
# audio_data = audio_data / np.max(np.abs(audio_data))
# time = np.linspace(0, len(audio_data) / sampling_rate, num=len(audio_data))

# # Cargar el archivo de audio para extracción de segmentos y reproducción
# audio_segment = AudioSegment.from_wav(wav_file_name)

# # Inicializar la interfaz gráfica
# root = tk.Tk()
# root.title("Interfaz Gráfica de la Onda Sonora")

# # Crear la gráfica para visualizar la onda sonora
# fig, ax = plt.subplots(figsize=(10, 4))
# ax.plot(time, audio_data, color="b")
# ax.set_xlabel("Tiempo [s]")
# ax.set_ylabel("Amplitud")
# ax.set_title("Onda Sonora")
# ax.grid()

# # Incrustar la gráfica en la interfaz Tkinter
# canvas = FigureCanvasTkAgg(fig, master=root)
# canvas_widget = canvas.get_tk_widget()
# canvas_widget.pack()

# # Variables para la selección del usuario
# start_x = None
# end_x = None
# segmento_audio = None
# seleccion_visual = None
# linea_inicio = None

# def guardar_imagen_completa():
#     """Guarda la onda sonora completa como imagen."""
#     archivo_guardado = filedialog.asksaveasfilename(defaultextension=".png",
#                                                     filetypes=[("Imágenes PNG", "*.png")],
#                                                     title="Guardar Imagen Completa")
#     if archivo_guardado:
#         fig.savefig(archivo_guardado)
#         print(f"Imagen guardada: {archivo_guardado}")

# def guardar_audio():
#     """Guarda el segmento de audio seleccionado."""
#     if segmento_audio:
#         archivo_guardado = filedialog.asksaveasfilename(defaultextension=".wav",
#                                                         filetypes=[("Archivos WAV", "*.wav")],
#                                                         title="Guardar Selección")
#         if archivo_guardado:
#             segmento_audio.export(archivo_guardado, format="wav")
#             print(f"Archivo guardado: {archivo_guardado}")

# def reproducir_audio():
#     """Reproduce el segmento de audio seleccionado."""
#     if segmento_audio:
#         temp_wav_path = "C:/Users/sherl/Desktop/seleccion.wav"
#         segmento_audio.export(temp_wav_path, format="wav")
#         playsound(temp_wav_path)

# # Botones
# tk.Button(root, text="Guardar Imagen Completa", command=guardar_imagen_completa).pack()
# tk.Button(root, text="Guardar Selección de Audio", command=guardar_audio).pack()
# tk.Button(root, text="Reproducir Selección", command=reproducir_audio).pack()

# root.mainloop()

"""English version"""

# Load the WAV file and extract audio data
wav_file_name = "u.wav"
wave_file = wave.open(wav_file_name, "rb")
sampling_rate = wave_file.getframerate()
audio_data = np.frombuffer(wave_file.readframes(-1), dtype=np.int16)
wave_file.close()

# Normalize the audio data for visualization
audio_data = audio_data / np.max(np.abs(audio_data))
time = np.linspace(0, len(audio_data) / sampling_rate, num=len(audio_data))

# Load the audio file for segment extraction and playback
audio_segment = AudioSegment.from_wav(wav_file_name)

# Initialize the graphical user interface
root = tk.Tk()
root.title("Sound Wave Graphical Interface")

# Create the plot for the waveform visualization
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(time, audio_data, color="b")
ax.set_xlabel("Time [s]")
ax.set_ylabel("Amplitude")
ax.set_title("Sound Wave")
ax.grid()

# Embed the plot into the Tkinter interface
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Variables for user selection
start_x = None
end_x = None
audio_segment_selected = None
selection_visual = None
start_line = None

def on_click(event):
    """Handles user selection of a specific time segment from the waveform."""
    global start_x, end_x, selection_visual, start_line
    
    if start_x is None:  # First click: start of selection
        start_x = event.xdata
        print(f"Selection started at: {start_x:.2f}s")
        
        # Draw the start selection line in green
        if start_line is not None:
            start_line.remove()
        start_line = ax.axvline(start_x, color="green", linestyle="--", linewidth=1)
        canvas.draw()
    
    else:  # Second click: end of selection
        end_x = event.xdata
        if start_x != end_x:
            if selection_visual:
                selection_visual.remove()
            selection_visual = ax.axvspan(start_x, end_x, color="red", alpha=0.3)  # Highlight selection in red
            canvas.draw()
            print(f"Selected section from {start_x:.2f}s to {end_x:.2f}s")

            # Convert time to milliseconds
            start_ms = int(start_x * 1000)
            end_ms = int(end_x * 1000)

            # Extract the selected audio segment
            global audio_segment_selected
            audio_segment_selected = audio_segment[start_ms:end_ms]
            start_x = None

canvas.mpl_connect("button_press_event", on_click)

def save_full_waveform_image():
    """Saves the complete waveform as an image."""
    saved_file = filedialog.asksaveasfilename(defaultextension=".png",
                                              filetypes=[("PNG Images", "*.png")],
                                              title="Save Full Waveform Image")
    if saved_file:
        fig.savefig(saved_file)
        print(f"Image saved: {saved_file}")

def save_selected_audio():
    """Saves the selected audio segment as a WAV file."""
    if audio_segment_selected:
        saved_file = filedialog.asksaveasfilename(defaultextension=".wav",
                                                  filetypes=[("WAV Files", "*.wav")],
                                                  title="Save Selected Audio")
        if saved_file:
            audio_segment_selected.export(saved_file, format="wav")
            print(f"Audio file saved: {saved_file}")

def play_selected_audio():
    """Plays the selected audio segment."""
    if audio_segment_selected:
        temp_wav_path = "C:/Users/sherl/Desktop/selected.wav"
        audio_segment_selected.export(temp_wav_path, format="wav")

        if os.path.exists(temp_wav_path):
            playsound(temp_wav_path)
        else:
            print("Error: Unable to generate audio file.")

def remove_selection():
    """Removes the current selection from the waveform visualization."""
    global selection_visual, audio_segment_selected, start_x, end_x
    if selection_visual is not None:
        selection_visual.remove()
        selection_visual = None
        audio_segment_selected = None
        start_x = None
        end_x = None
        canvas.draw()
        print("Selection removed.")

# Buttons
btn_save_audio = tk.Button(root, text="Save Selected Audio", command=save_selected_audio)
btn_save_audio.pack()

btn_play_audio = tk.Button(root, text="Play Selected Audio", command=play_selected_audio)
btn_play_audio.pack()

btn_save_waveform = tk.Button(root, text="Save Full Waveform", command=save_full_waveform_image)
btn_save_waveform.pack()

btn_remove_selection = tk.Button(root, text="Remove Selection", command=remove_selection)
btn_remove_selection.pack()

# Launch the graphical interface
root.mainloop()