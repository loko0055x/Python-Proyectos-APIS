from PIL import Image
import os


def combine_images_2x2(image_paths, output_path, size=(500, 500)):
    # Asumiendo que todas las imágenes tienen fondo transparente (RGBA)
    images = [Image.open(p).convert("RGBA").resize(size) for p in image_paths]

    # Crear nueva imagen con fondo transparente
    combined_width = size[0] * 2
    combined_height = size[1] * 2
    combined_image = Image.new(
        "RGBA", (combined_width, combined_height), (0, 0, 0, 0))

    # Posiciones (x, y) para colocar las imágenes
    positions = [
        (0, 0),                         # arriba izquierda
        (size[0], 0),                   # arriba derecha
        (0, size[1]),                   # abajo izquierda
        (size[0], size[1])              # abajo derecha
    ]

    # Pegar imágenes en sus posiciones
    for img, pos in zip(images, positions):
        combined_image.paste(img, pos, mask=img)

    # Guardar resultado
    combined_image.save(output_path, "PNG")
    print(f"✅ Imagen combinada guardada en: {output_path}")


# 📂 Asegúrate que los nombres de archivos están bien y en el mismo folder
image_files = ["nube_con_borde.png", "nube_con_borde1.png",
               "nube_con_borde2.png", "nube_con_borde3.jpg"]  # tus imágenes con transparencia
combine_images_2x2(image_files, "combinado.png")
