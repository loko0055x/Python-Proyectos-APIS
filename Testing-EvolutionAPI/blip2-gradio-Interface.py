from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import gradio as gr

"""
Gradio es una herramienta que te permite crear interfaces web para tus modelos de IA en pocos minutos, sin saber frontend.
Con Gradio puedes:
Subir imágenes 📷
Escribir texto ✍️
Ver resultados en el navegador 🌐
Probar modelos de IA (como BLIP, GPT, Whisper, etc.)


"""

# Cargar el modelo y el procesador
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base")


def generate_caption(img):
    img_input = Image.fromarray(img)
    inputs = processor(img_input, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return (caption)


# Interfaz correcta
demo = gr.Interface(
    fn=generate_caption,
    inputs=[gr.Image(label="Image")],
    outputs=[gr.Text(label="Caption")]
)

demo.launch()
