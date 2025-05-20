import subprocess
import sys

non_standard_libs = []  

def install_and_import(library):
    """
    Verifica si una biblioteca externa está instalada; la instala si no lo está.
    """
    try:
        __import__(library)
    except ImportError:
        print(f"Installing missing library: {library}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])

for lib in non_standard_libs:
    install_and_import(lib)


import os
import sys
import ctypes
import platform
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

print("All required libraries are available. Proceeding with execution...")

"""version donde modifico varias partes, pero hay que tener cuidado con el 
uso en el programa, puede fallar"""
"""razon: 
    La modificación de los parámetros articulatorios en el archivo .ges 
    debe ajustarse al modelo estándar de VocalTractLab 2.3, donde los gestos 
    supraglóticos no definen directamente valores numéricos, sino que apuntan 
    a etiquetas de formas predefinidas en el archivo .speaker
"""
# # Vowel shapes defined in the loaded .speaker file
# valid_shapes = ["a", "e", "i", "o", "u"]

# def create_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa, output_filename):
#     """Creates a .ges file with the structure required by the VTL API."""
    
#     if vowel_label not in valid_shapes:
#         raise ValueError(f"The vowel '{vowel_label}' is not defined in the .speaker file.")

#     # Create root element for the gestural score
#     gestural_score = ET.Element('gestural_score')

#     # List of gesture types and corresponding values
#     tiers = [
#         ('vowel-gestures', vowel_label),
#         ('glottal-shape-gestures', 'modal'),
#         ('f0-gestures', f0_value),
#         ('lung-pressure-gestures', lung_pressure_dpa)
#     ]

#     # Add gesture sequences to the gestural score
#     for tier_type, value in tiers:
#         gesture_sequence = ET.SubElement(gestural_score, 'gesture_sequence', {'type': tier_type, 'unit': ''})
#         gesture_attribs = {
#             'value': str(value),
#             'slope': "0.000000",
#             'duration_s': f"{duration_s:.6f}",
#             'time_constant_s': "0.020000",
#             'neutral': "0"
#         }
#         ET.SubElement(gesture_sequence, 'gesture', gesture_attribs)

#     # Generate a pretty-printed XML string and write it to a file
#     pretty_xml = minidom.parseString(ET.tostring(gestural_score, encoding='unicode')).toprettyxml(indent="  ")
#     with open(output_filename, 'w', encoding='utf-8') as f:
#         f.write(pretty_xml)

#     print(f"Structured .ges file generated: {output_filename}")

# def generate_multiple_vowel_ges(duration_s, f0_value, lung_pressure_dpa):
#     """Generates .ges files for all vowels defined in the .speaker file."""
#     for vowel in valid_shapes:
#         output_filename = f"vowel_{vowel}.ges"
#         create_vowel_ges(vowel, duration_s, f0_value, lung_pressure_dpa, output_filename)

# def generate_single_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa):
#     """Generates a single .ges file for the specified vowel."""
#     if vowel_label not in valid_shapes:
#         raise ValueError(f"The vowel '{vowel_label}' is not defined in the .speaker file.")
    
#     output_filename = f"vowel_{vowel_label}.ges"
#     create_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa, output_filename)

# def modify_vocal_tract_position(ges_filename, jaw_height, lip_width, tongue_tip_x, tongue_tip_y):
#     """Modifies jaw, lip, and tongue tip position in an existing .ges file."""
    
#     tree = ET.parse(ges_filename)
#     root = tree.getroot()

#     # Add jaw gesture
#     jaw_sequence = ET.SubElement(root, 'gesture_sequence', {'type': 'jaw-gestures', 'unit': ''})
#     ET.SubElement(jaw_sequence, 'gesture', {
#         'value': str(jaw_height),
#         'slope': "0.000000",
#         'duration_s': "0.600000",
#         'time_constant_s': "0.020000",
#         'neutral': "0"
#     })

#     # Add lip gesture
#     lip_sequence = ET.SubElement(root, 'gesture_sequence', {'type': 'lip-gestures', 'unit': ''})
#     ET.SubElement(lip_sequence, 'gesture', {
#         'value': str(lip_width),
#         'slope': "0.000000",
#         'duration_s': "0.600000",
#         'time_constant_s': "0.020000",
#         'neutral': "0"
#     })

#     # Add tongue tip gesture (x, y coordinates)
#     tongue_sequence = ET.SubElement(root, 'gesture_sequence', {'type': 'tongue-tip-gestures', 'unit': ''})
#     ET.SubElement(tongue_sequence, 'gesture', {
#         'value': f"{tongue_tip_x},{tongue_tip_y}",
#         'slope': "0.000000",
#         'duration_s': "0.600000",
#         'time_constant_s': "0.020000",
#         'neutral': "0"
#     })

#     # Save modified .ges file
#     tree.write(ges_filename)
#     print(f"Modifications applied to file: {ges_filename}")

# # =======================
# # Example usage
# # =======================
# if __name__ == "__main__":
#     vowel_label = "u"
#     duration_s = 1
#     f0_value = "82"
#     lung_pressure_dpa = "8000"

#     ges_filename = f"vowel_{vowel_label}.ges"
#     create_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa, ges_filename)

#     # Generate .ges files for all vowels
#     generate_multiple_vowel_ges(duration_s=0.600, f0_value="100", lung_pressure_dpa="7000")

#     # Generate .ges file for a specific vowel
#     generate_single_vowel_ges(vowel_label="a", duration_s=0.600, f0_value="100", lung_pressure_dpa="7000")

#     # Modify vocal tract positions in a .ges file
#     modify_vocal_tract_position(
#         ges_filename,
#         jaw_height="1.5000",
#         lip_width="1.2000",
#         tongue_tip_x="3.5000",
#         tongue_tip_y="-1.0000"
#     )
"""version en español"""

# # Lista de vocales válidas definidas en el archivo .speaker utilizado por VTL (VocalTractLab)
# valid_shapes = ["a", "e", "i", "o", "u"]

# def create_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa, output_filename):
#     """Crea un archivo .ges con la estructura estándar requerida por VTL.
#     Los gestos supraglóticos apuntan a las etiquetas definidas en .speaker (no valores numéricos)."""
    
#     if vowel_label not in valid_shapes:
#         raise ValueError(f"La vocal '{vowel_label}' no está definida en el archivo .speaker.")
    
#     # Crear el elemento raíz 'gestural_score'
#     gestural_score = ET.Element('gestural_score')

#     # Definición de tiers (gestos)
#     tiers = [
#         ('vowel-gestures', vowel_label),              # Apunta a la forma de la vocal
#         ('glottal-shape-gestures', 'modal'),          # Forma glotal estándar
#         ('f0-gestures', str(f0_value)),                # Valor de F0 como string
#         ('lung-pressure-gestures', str(lung_pressure_dpa)) # Presión pulmonar
#     ]

#     # Añadir secuencias de gestos
#     for tier_type, value in tiers:
#         gesture_sequence = ET.SubElement(gestural_score, 'gesture_sequence', {'type': tier_type, 'unit': ''})
#         gesture_attribs = {
#             'value': str(value),
#             'slope': "0.000000",
#             'duration_s': f"{duration_s:.6f}",
#             'time_constant_s': "0.020000",
#             'neutral': "0"
#         }
#         ET.SubElement(gesture_sequence, 'gesture', gesture_attribs)

#     # Convertir a XML formateado
#     pretty_xml = minidom.parseString(ET.tostring(gestural_score, encoding='unicode')).toprettyxml(indent="  ")
    
#     # Guardar el archivo
#     with open(output_filename, 'w', encoding='utf-8') as f:
#         f.write(pretty_xml)

#     print(f"Archivo .ges generado: {output_filename}")

# def generate_multiple_vowel_ges(duration_s, f0_value, lung_pressure_dpa):
#     """Genera archivos .ges para todas las vocales definidas."""
#     for vowel in valid_shapes:
#         output_filename = f"vowel_{vowel}.ges"
#         create_vowel_ges(vowel, duration_s, f0_value, lung_pressure_dpa, output_filename)

# def generate_single_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa):
#     """Genera un único archivo .ges para la vocal especificada."""
#     if vowel_label not in valid_shapes:
#         raise ValueError(f"La vocal '{vowel_label}' no está definida en el archivo .speaker.")
    
#     output_filename = f"vowel_{vowel_label}.ges"
#     create_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa, output_filename)

# def modify_vocal_tract_shape_labels(ges_filename, new_vowel_label=None, new_lip_label=None, new_tongue_tip_label=None):
#     """
#     Modifica las etiquetas de las formas apuntadas en el archivo .ges para gestos supraglóticos.
#     - new_vowel_label: nueva etiqueta para 'vowel-gestures'
#     - new_lip_label: nueva etiqueta para 'lip-gestures'
#     - new_tongue_tip_label: nueva etiqueta para 'tongue-tip-gestures'
    
#     Nota: Esto no modifica valores numéricos, sino que cambia las referencias a formas predefinidas.
#     """
#     tree = ET.parse(ges_filename)
#     root = tree.getroot()

#     # Función auxiliar para cambiar etiqueta de gesto
#     def update_gesture_label(tier_type, new_label):
#         # Buscar el tier correspondiente
#         gesture_seq = root.find(f"./gesture_sequence[@type='{tier_type}']")
#         if gesture_seq is not None and new_label is not None:
#             # Asumimos que solo hay un gesto en la secuencia
#             gesture = gesture_seq.find('gesture')
#             if gesture is not None:
#                 gesture.set('value', new_label)
#             else:
#                 # Si no existe gesto, crearlo
#                 ET.SubElement(gesture_seq, 'gesture', {
#                     'value': new_label,
#                     'slope': "0.000000",
#                     'duration_s': "0.600000",
#                     'time_constant_s': "0.020000",
#                     'neutral': "0"
#                 })
#         elif gesture_seq is None and new_label is not None:
#             # Crear la secuencia y el gesto si no existe
#             gesture_seq = ET.SubElement(root, 'gesture_sequence', {'type': tier_type, 'unit': ''})
#             ET.SubElement(gesture_seq, 'gesture', {
#                 'value': new_label,
#                 'slope': "0.000000",
#                 'duration_s': "0.600000",
#                 'time_constant_s': "0.020000",
#                 'neutral': "0"
#             })

#     # Actualizar etiquetas según lo recibido
#     update_gesture_label('vowel-gestures', new_vowel_label)
#     update_gesture_label('lip-gestures', new_lip_label)
#     update_gesture_label('tongue-tip-gestures', new_tongue_tip_label)

#     # Guardar cambios
#     tree.write(ges_filename, encoding='utf-8', xml_declaration=True)
#     print(f"Archivo .ges modificado guardado: {ges_filename}")

# # =======================
# # Ejemplo de uso
# # =======================
# if __name__ == "__main__":
#     vowel_label = "u"
#     duration_s = 1.0
#     f0_value = "82"
#     lung_pressure_dpa = "8000"

#     ges_filename = f"vowel_{vowel_label}.ges"
    
#     # Crear archivo para una vocal
#     create_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa, ges_filename)

#     # Crear archivos para todas las vocales
#     generate_multiple_vowel_ges(duration_s=0.600, f0_value="100", lung_pressure_dpa="7000")

#     # Crear archivo para una vocal específica
#     generate_single_vowel_ges(vowel_label="a", duration_s=0.600, f0_value="100", lung_pressure_dpa="7000")

#     # Modificar etiquetas de formas en el archivo .ges (ejemplo)
#     modify_vocal_tract_shape_labels(
#         ges_filename,
#         new_vowel_label="o",        # Cambiar la vocal apuntada
#         new_lip_label="rounded",    # Ejemplo etiqueta para labios (debe estar en .speaker)
#         new_tongue_tip_label="tip_high"  # Ejemplo etiqueta para punta de lengua (en .speaker)
#     )



"""English version"""

import xml.etree.ElementTree as ET
from xml.dom import minidom

# Vowel shapes defined in the .speaker file
valid_shapes = ["a", "e", "i", "o", "u"]

def create_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa, output_filename):
    """
    Creates a .ges file with the standard structure required by VTL.
    Supraglottal gestures point to the shape labels defined in the .speaker file (not numeric values).
    """
    if vowel_label not in valid_shapes:
        raise ValueError(f"The vowel '{vowel_label}' is not defined in the .speaker file.")
    
    # Create root element 'gestural_score'
    gestural_score = ET.Element('gestural_score')

    # Define tiers (gestures)
    tiers = [
        ('vowel-gestures', vowel_label),                # Points to vowel shape
        ('glottal-shape-gestures', 'modal'),             # Standard glottal shape
        ('f0-gestures', str(f0_value)),                   # F0 value as string
        ('lung-pressure-gestures', str(lung_pressure_dpa)) # Lung pressure
    ]

    # Add gesture sequences
    for tier_type, value in tiers:
        gesture_sequence = ET.SubElement(gestural_score, 'gesture_sequence', {'type': tier_type, 'unit': ''})
        gesture_attribs = {
            'value': str(value),
            'slope': "0.000000",
            'duration_s': f"{duration_s:.6f}",
            'time_constant_s': "0.020000",
            'neutral': "0"
        }
        ET.SubElement(gesture_sequence, 'gesture', gesture_attribs)

    # Convert to pretty XML string
    pretty_xml = minidom.parseString(ET.tostring(gestural_score, encoding='unicode')).toprettyxml(indent="  ")
    
    # Save file
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)

    print(f".ges file generated: {output_filename}")

def generate_multiple_vowel_ges(duration_s, f0_value, lung_pressure_dpa):
    """Generates .ges files for all defined vowels."""
    for vowel in valid_shapes:
        output_filename = f"vowel_{vowel}.ges"
        create_vowel_ges(vowel, duration_s, f0_value, lung_pressure_dpa, output_filename)

def generate_single_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa):
    """Generates a single .ges file for the specified vowel."""
    if vowel_label not in valid_shapes:
        raise ValueError(f"The vowel '{vowel_label}' is not defined in the .speaker file.")
    
    output_filename = f"vowel_{vowel_label}.ges"
    create_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa, output_filename)

def modify_vocal_tract_shape_labels(ges_filename, new_vowel_label=None, new_lip_label=None, new_tongue_tip_label=None):
    """
    Modifies the shape labels referenced in the .ges file for supraglottal gestures.
    - new_vowel_label: new label for 'vowel-gestures'
    - new_lip_label: new label for 'lip-gestures'
    - new_tongue_tip_label: new label for 'tongue-tip-gestures'
    
    Note: This does not modify numeric values but changes references to predefined shapes.
    """
    tree = ET.parse(ges_filename)
    root = tree.getroot()

    # Helper function to update gesture label
    def update_gesture_label(tier_type, new_label):
        gesture_seq = root.find(f"./gesture_sequence[@type='{tier_type}']")
        if gesture_seq is not None and new_label is not None:
            # Assuming there is only one gesture in the sequence
            gesture = gesture_seq.find('gesture')
            if gesture is not None:
                gesture.set('value', new_label)
            else:
                # If no gesture exists, create one
                ET.SubElement(gesture_seq, 'gesture', {
                    'value': new_label,
                    'slope': "0.000000",
                    'duration_s': "0.600000",
                    'time_constant_s': "0.020000",
                    'neutral': "0"
                })
        elif gesture_seq is None and new_label is not None:
            # Create sequence and gesture if not present
            gesture_seq = ET.SubElement(root, 'gesture_sequence', {'type': tier_type, 'unit': ''})
            ET.SubElement(gesture_seq, 'gesture', {
                'value': new_label,
                'slope': "0.000000",
                'duration_s': "0.600000",
                'time_constant_s': "0.020000",
                'neutral': "0"
            })

    # Update labels as provided
    update_gesture_label('vowel-gestures', new_vowel_label)
    update_gesture_label('lip-gestures', new_lip_label)
    update_gesture_label('tongue-tip-gestures', new_tongue_tip_label)

    # Save changes
    tree.write(ges_filename, encoding='utf-8', xml_declaration=True)
    print(f".ges file modified and saved: {ges_filename}")

# =======================
# Example
# =======================
if __name__ == "__main__":
    vowel_label = "u"
    duration_s = 1.0
    f0_value = "82"
    lung_pressure_dpa = "8000"

    ges_filename = f"vowel_{vowel_label}.ges"
    
    # Create file for one vowel
    create_vowel_ges(vowel_label, duration_s, f0_value, lung_pressure_dpa, ges_filename)

    # Create files for all vowels
    generate_multiple_vowel_ges(duration_s=0.600, f0_value="100", lung_pressure_dpa="7000")

    # Create file for a specific vowel
    generate_single_vowel_ges(vowel_label="a", duration_s=0.600, f0_value="100", lung_pressure_dpa="7000")

    # Modify shape labels in the .ges file (example)
    modify_vocal_tract_shape_labels(
        ges_filename,
        new_vowel_label="o",        # Change referenced vowel shape
        new_lip_label="rounded",    # Example lip shape label (must be defined in .speaker)
        new_tongue_tip_label="tip_high"  # Example tongue tip shape label (in .speaker)
    )
