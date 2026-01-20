from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Path
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
import os

# Crear directorio si no existe
os.makedirs('public', exist_ok=True)

# Rutas locales de imágenes
qr_path = "Commons_QR_code.png"
logo_path = "logo_navicf.png"
signatures_path = "firma.png"
course_image_path = "cursopesado.png"

# Cargar imágenes locales


def load_local_image(path):
    try:
        if os.path.exists(path):
            return Image.open(path)
        else:
            print(f"Advertencia: Imagen no encontrada: {path}")
            return None
    except Exception as e:
        print(f"Error cargando imagen: {e}")
        return None


print("Cargando imágenes locales...")
qr_img = load_local_image(qr_path)
logo_img = load_local_image(logo_path)
signatures_img = load_local_image(signatures_path)
course_img = load_local_image(course_image_path)

# Crear PDF
width, height = letter
c = canvas.Canvas("public/certificado.pdf", pagesize=letter)

BLUE_DARK = HexColor("#1E5BA8")
BLUE_LIGHT = HexColor("#5BA3D0")
BLUE_VERY_LIGHT = HexColor("#E8F1F7")
GRAY = HexColor("#333333")
WHITE = HexColor("#FFFFFF")

# Triángulo diagonal superior izquierdo

# Rectángulo azul oscuro en esquina superior izquierda
c.setFillColor(BLUE_DARK)
c.rect(0, height - 1.2*inch, 1.5*inch, 1.2*inch, fill=1, stroke=0)

# Línea diagonal blanca
c.setStrokeColor(WHITE)
c.setLineWidth(0.15*inch)
c.line(0.3*inch, height - 0.5*inch, 1.8*inch, height - 1.5*inch)

# Elemento decorativo azul claro en esquina inferior derecha
c.setFillColor(BLUE_LIGHT)
c.setStrokeColor(BLUE_LIGHT)
# Curva decorativa inferior derecha
c.setLineWidth(2)
for i in range(0, 80, 10):
    c.circle(width - 0.5*inch + i*0.02*inch, 0.3*inch +
             i*0.01*inch, 0.15*inch, fill=1, stroke=0)

c.setStrokeColor(GRAY)
c.setLineWidth(3)
c.line(0.4*inch, height - 0.35*inch, width - 0.4*inch, height - 0.35*inch)
c.line(0.4*inch, 0.5*inch, width - 0.4*inch, 0.5*inch)

c.setLineWidth(2)
c.line(0.35*inch, 0.5*inch, 0.35*inch, height - 0.35*inch)
c.line(width - 0.35*inch, 0.5*inch, width - 0.35*inch, height - 0.35*inch)

c.setFont("Helvetica-Bold", 14)
c.setFillColor(GRAY)
c.drawString(0.6*inch, height - 0.85*inch, "CEP")
c.setFont("Helvetica", 8)
c.drawString(0.55*inch, height - 1.05*inch, "CURSOS DE")
c.drawString(0.45*inch, height - 1.2*inch, "EQUIPOS")
c.drawString(0.5*inch, height - 1.35*inch, "PESADOS")

if logo_img:
    logo_img.thumbnail((1.2*inch, 0.8*inch), Image.Resampling.LANCZOS)
    logo_path = "temp_logo.png"
    logo_img.save(logo_path)
    c.drawImage(logo_path, width - 2.2*inch, height -
                1.1*inch, width=1.2*inch, height=0.8*inch)

c.setFont("Helvetica-Bold", 48)
c.setFillColor(BLUE_DARK)
c.drawCentredString(width/2, height - 2.2*inch, "CERTIFICADO")

c.setFont("Helvetica", 10)
c.setFillColor(GRAY)
c.drawCentredString(width/2, height - 2.5*inch, "OTORGADO A:")

c.setFont("Helvetica-Bold", 14)
c.setFillColor(GRAY)
c.drawCentredString(width/2, height - 2.9*inch,
                    "JOEL ARMANDO MIRANDA CARBAJAL")

c.setFont("Helvetica", 10)
c.setFillColor(GRAY)
c.drawCentredString(width/2, height - 3.2*inch, "DNI: 44573082")

c.setFont("Helvetica", 9)
c.setFillColor(GRAY)
text_y = height - 3.6*inch
c.drawCentredString(
    width/2, text_y, "En merito de haber aprobado satisfactoriamente el curso tecnico operativo- capacitacion")
text_y -= 0.25*inch
c.setFont("Helvetica-Bold", 9)
c.drawCentredString(
    width/2, text_y, "OPERACION Y MANTENIMIENTO DE RETROEXCAVADORA")

c.setFont("Helvetica", 9)
c.setFillColor(GRAY)
text_y -= 0.35*inch
c.drawCentredString(
    width/2, text_y, "En periodo programado de 2021-02-01 - 2021-06-09 con una duracion de 120 horas teorico y practico.")

c.setFont("Helvetica-Bold", 10)
c.setFillColor(GRAY)
text_y -= 0.5*inch
c.drawCentredString(width/2, text_y, "LIMA, 9 DE JUNIO DEL 2021")

if qr_img:
    qr_img.thumbnail((0.9*inch, 0.9*inch), Image.Resampling.LANCZOS)
    qr_path = "temp_qr.png"
    qr_img.save(qr_path)
    c.drawImage(qr_path, 0.6*inch, 1.2*inch, width=0.9*inch, height=0.9*inch)

signature_y = 1.5*inch
c.setLineWidth(1)
c.setStrokeColor(GRAY)

# Firma 1
c.line(0.8*inch, signature_y - 0.3*inch, 1.8*inch, signature_y - 0.3*inch)
c.setFont("Helvetica", 8)
c.drawCentredString(1.3*inch, signature_y - 0.5*inch, "NANCY FACUNDO PEÑA")
c.drawCentredString(1.3*inch, signature_y - 0.65*inch, "GERENTE GENERAL")

# Firma 2
c.line(2.8*inch, signature_y - 0.3*inch, 3.8*inch, signature_y - 0.3*inch)
c.drawCentredString(3.3*inch, signature_y - 0.5*inch, "YEISON PUCHOC MILLAN")
c.drawCentredString(3.3*inch, signature_y - 0.65*inch, "ING. MECANICO")

# Firma 3
c.line(4.8*inch, signature_y - 0.3*inch, 5.8*inch, signature_y - 0.3*inch)
c.drawCentredString(5.3*inch, signature_y - 0.5*inch, "VICTOR HUAMAN PAIMA")
c.drawCentredString(5.3*inch, signature_y - 0.65*inch, "INSTRUCTOR DE EQUIPOS")

if signatures_img:
    signatures_img.thumbnail((0.6*inch, 0.6*inch), Image.Resampling.LANCZOS)
    sig_path = "temp_signatures.png"
    signatures_img.save(sig_path)
    # Colocar sellos encima de las líneas de firma
    c.drawImage(sig_path, 1.0*inch, signature_y - 0.15 *
                inch, width=0.5*inch, height=0.5*inch)
    c.drawImage(sig_path, 3.0*inch, signature_y - 0.15 *
                inch, width=0.5*inch, height=0.5*inch)
    c.drawImage(sig_path, 5.0*inch, signature_y - 0.15 *
                inch, width=0.5*inch, height=0.5*inch)

# Guardar PDF
c.save()
print("✓ PDF generado exitosamente: public/certificado.pdf")

# Limpiar archivos temporales
for temp_file in ["temp_logo.png", "temp_qr.png", "temp_signatures.png"]:
    if os.path.exists(temp_file):
        os.remove(temp_file)
