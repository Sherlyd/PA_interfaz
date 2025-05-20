import subprocess
import sys

# List of required libraries
required_libraries = ["ctypes", "sys", "os"]

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
import ctypes
import sys
import os

print("All required libraries are installed. Proceeding with execution...")


"""version en español"""

# # Carga la API de Vocal Tract Lab (VTL) según el sistema operativo
# if sys.platform == 'win32':
#     VTL = ctypes.cdll.LoadLibrary('./VocalTractLabApi.dll')
# else:
#     VTL = ctypes.cdll.LoadLibrary('./VocalTractLabApi.so')

# # Define la ruta del archivo .speaker utilizado para la síntesis vocal
# speaker_file_name = ctypes.c_char_p(b'C:/Users/sherl/Desktop/ya_el_fin/JD2.speaker')

# def generate_wav_from_ges(gesture_file_name_str):
#     """
#     Genera un archivo .wav a partir de un archivo .ges específico utilizando la API de VTL.

#     Parámetros:
#     - gesture_file_name_str: Ruta del archivo .ges.

#     Retorna:
#     - Un archivo .wav sintetizado con el sonido de la vocal extraída.
#     """

#     gesture_file_name = ctypes.c_char_p(gesture_file_name_str.encode())

#     # Extraer la vocal del nombre del archivo ges
#     base_name = os.path.basename(gesture_file_name_str)
#     vocal = base_name.split("_")[-1].split(".")[0]  # Extraer la vocal

#     # Definir el nombre del archivo .wav de salida
#     wav_file_name_str = f'{vocal}.wav'
#     wav_file_name = ctypes.c_char_p(wav_file_name_str.encode())

#     numSamples = ctypes.c_int(0)
#     audio = (ctypes.c_double * int(5 * 44100))()  # Reserva memoria para duración estimada

#     # Inicializa VTL con el archivo .speaker
#     failure = VTL.vtlInitialize(speaker_file_name)
#     if failure != 0:
#         raise ValueError(f'Error en vtlInitialize! Código de error: {failure}')

#     # Genera el archivo de audio desde el gestural score
#     print(f'Generando audio para la vocal "{vocal}"...')
#     failure = VTL.vtlGesturalScoreToAudio(gesture_file_name,
#                                           wav_file_name,
#                                           ctypes.byref(audio),
#                                           ctypes.byref(numSamples),
#                                           int(1))

#     if failure != 0:
#         raise ValueError(f'Error en vtlGesturalScoreToAudio! Código de error: {failure}')

#     VTL.vtlClose()

#     print(f'Generación de audio completada. Archivo guardado como: {wav_file_name.value.decode()}')

# def generate_wavs_from_multiple_ges(ges_folder):
#     """
#     Genera archivos .wav para todos los archivos .ges dentro de una carpeta específica.

#     Parámetros:
#     - ges_folder: Ruta de la carpeta que contiene archivos .ges.

#     Retorna:
#     - Múltiples archivos .wav correspondientes a los archivos .ges procesados.
#     """
    
#     if not os.path.exists(ges_folder):
#         raise ValueError(f"La carpeta {ges_folder} no existe.")

#     ges_files = [f for f in os.listdir(ges_folder) if f.endswith(".ges")]

#     if not ges_files:
#         print("No se encontraron archivos .ges en la carpeta.")
#         return

#     print(f"Procesando {len(ges_files)} archivos .ges en {ges_folder}...")

#     for ges_file in ges_files:
#         ges_path = os.path.join(ges_folder, ges_file)
#         generate_wav_from_ges(ges_path)

# # =======================
# # Ejemplo de uso
# # =======================
# if __name__ == "__main__":
#     # Generar un solo archivo .wav desde un archivo .ges específico
#     generate_wav_from_ges("C:/Users/sherl/Desktop/ya_el_fin/vocal_u.ges")

#     # Generar archivos .wav desde múltiples archivos .ges dentro de una carpeta
#     generate_wavs_from_multiple_ges("C:/Users/sherl/Desktop/ya_el_fin/")

"""English version"""


# Load the Vocal Tract Lab (VTL) API based on the operating system
if sys.platform == 'win32':
    VTL = ctypes.cdll.LoadLibrary('./VocalTractLabApi.dll')
else:
    VTL = ctypes.cdll.LoadLibrary('./VocalTractLabApi.so')

# Define the speaker file path used for vocal synthesis
speaker_file_name = ctypes.c_char_p(b'C:/Users/sherl/Desktop/ya_el_fin/JD2.speaker')

def generate_wav_from_ges(gesture_file_name_str):
    """
    Generates a .wav file from a specific .ges file using the VTL API.

    Parameters:
    - gesture_file_name_str: Path to the .ges file.

    Returns:
    - A synthesized .wav file with the extracted vowel sound.
    """

    gesture_file_name = ctypes.c_char_p(gesture_file_name_str.encode())

    # Extract the vowel from the .ges file name
    base_name = os.path.basename(gesture_file_name_str)
    vowel = base_name.split("_")[-1].split(".")[0]  # Extract vowel

    # Define the output .wav file name
    wav_file_name_str = f'{vowel}.wav'
    wav_file_name = ctypes.c_char_p(wav_file_name_str.encode())

    numSamples = ctypes.c_int(0)
    audio = (ctypes.c_double * int(5 * 44100))()  # Allocate memory for estimated duration

    # Initialize VTL with the .speaker file
    failure = VTL.vtlInitialize(speaker_file_name)
    if failure != 0:
        raise ValueError(f'Error in vtlInitialize! Error code: {failure}')

    # Generate the audio file from the gestural score
    print(f'Generating audio for vowel "{vowel}"...')
    failure = VTL.vtlGesturalScoreToAudio(gesture_file_name,
                                          wav_file_name,
                                          ctypes.byref(audio),
                                          ctypes.byref(numSamples),
                                          int(1))

    if failure != 0:
        raise ValueError(f'Error in vtlGesturalScoreToAudio! Error code: {failure}')

    VTL.vtlClose()

    print(f'Audio generation completed. File saved as: {wav_file_name.value.decode()}')

def generate_wavs_from_multiple_ges(ges_folder):
    """
    Generates .wav files for all .ges files inside a specified folder.

    Parameters:
    - ges_folder: Path to the folder containing .ges files.

    Returns:
    - Multiple .wav files corresponding to the .ges files.
    """
    
    if not os.path.exists(ges_folder):
        raise ValueError(f"The folder {ges_folder} does not exist.")

    ges_files = [f for f in os.listdir(ges_folder) if f.endswith(".ges")]

    if not ges_files:
        print("No .ges files were found in the folder.")
        return

    print(f"Processing {len(ges_files)} .ges files in {ges_folder}...")

    for ges_file in ges_files:
        ges_path = os.path.join(ges_folder, ges_file)
        generate_wav_from_ges(ges_path)

# =======================
# Example Usage
# =======================
if __name__ == "__main__":
    # Generate a single .wav file from a specific .ges file
    generate_wav_from_ges("C:/Users/sherl/Desktop/ya_el_fin/vocal_u.ges")

    # Generate .wav files from multiple .ges files inside a folder
    generate_wavs_from_multiple_ges("C:/Users/sherl/Desktop/ya_el_fin/")