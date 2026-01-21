from PIL import Image, ImageDraw, ImageChops
import numpy as np


"""
mediante una imagen editar con forma circular
"""
def apply_cloud_mask_with_border_local(image_path, output_path, size=(500, 500), border_color=(255, 255, 0), border_width=6):
    # Abrir imagen local y redimensionar
    image = Image.open(image_path).convert("RGBA").resize(size)

    # Crear máscara de nube
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)

    # Dibujar óvalos para simular forma de nube
    ovals = [
        (100, 150, 400, 350),
        (150, 100, 350, 300),
        (50, 200, 300, 400),
        (200, 180, 450, 360),
    ]
    for oval in ovals:
        draw.ellipse(oval, fill=255)

    # Aplicar la máscara a la imagen
    image_np = np.array(image)
    image_np[:, :, 3] = np.array(mask)
    cloud_image = Image.fromarray(image_np)

    # Crear borde amarillo alrededor de la nube
    border = Image.new("RGBA", size, (0, 0, 0, 0))
    for i in range(1, border_width + 1):
        expanded_mask = Image.new("L", size, 0)
        expanded_draw = ImageDraw.Draw(expanded_mask)
        for oval in ovals:
            expanded_oval = (
                oval[0] - i,
                oval[1] - i,
                oval[2] + i,
                oval[3] + i,
            )
            expanded_draw.ellipse(expanded_oval, fill=255)
        border_mask = ImageChops.difference(expanded_mask, mask)
        border_color_layer = Image.new("RGBA", size, border_color + (255,))
        border.paste(border_color_layer, (0, 0), mask=border_mask)

    # Combinar borde + imagen en forma de nube
    final_image = Image.alpha_composite(border, cloud_image)
    final_image.save(output_path, "PNG")
    print(
        f"✅ Imagen con forma de nube y borde amarillo guardada en: {output_path}")


# 📁 Reemplaza con la ruta a tu imagen local
apply_cloud_mask_with_border_local(
    # 👉 tu archivo local aquí (mismo folder o ruta completa)
    "fot.png",
    "nube_con_borde.png"      # 👉 salida con nube y borde amarillo
)
