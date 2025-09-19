import turtle
import pygame
import threading
import random
import time

# --- MÚSICA (opcional) ---
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("Archivos_Excel/audio.mp3")  # Cambia esta ruta a tu archivo de música
    pygame.mixer.music.play(start=115)  # Reproducción al inicio

threading.Thread(target=play_music, daemon=True).start()

# --- CONFIGURACIÓN DE VENTANA ---
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Para ti, mi amor ❤️, Mi Pequeña Campanitas de Belen xD")

# --- FONDO DE ESTRELLAS ---
stars = turtle.Turtle()
stars.hideturtle()
stars.speed(0)
stars.color("white")
stars.penup()

def draw_stars():
    for _ in range(80):  # Añadí más estrellas
        x = random.randint(-300, 300)
        y = random.randint(-200, 250)
        stars.goto(x, y)
        stars.dot(random.randint(2, 4), "white")

draw_stars()

# --- DIBUJAR CORAZÓN --- 
pen = turtle.Turtle()
pen.speed(0)
pen.color("pink")
pen.fillcolor("red")
pen.penup()
pen.goto(0, -100)
pen.pendown()

pen.begin_fill()
pen.left(140)
pen.forward(224)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.left(120)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.forward(224)
pen.end_fill()

# --- MENSAJE ROMÁNTICO ---
def typewriter_message(texto):
    typer = turtle.Turtle()
    typer.hideturtle()
    typer.color("white")
    typer.penup()
    typer.goto(0, -230)
    typer.write("", align="center", font=("Arial", 14, "bold"))
    
    mensaje_actual = ""
    for letra in texto:
        mensaje_actual += letra
        typer.clear()
        typer.write(mensaje_actual, align="center", font=("Arial", 14, "bold"))
        time.sleep(0.15)  # Velocidad de escritura

# Mensaje romántico especial para ella
mensaje = (
    "Mi amor, estas dos semanas han sido mágicas.\n"
    "Gracias por tu amor, paciencia y todo lo que me das cada día.\n"
    "Eres la razón de mi sonrisa, y hoy quiero dedicarte este detalle.\n"
    "Te amo más de lo que las palabras pueden expresar. ❤️"
)

threading.Thread(target=typewriter_message, args=(mensaje,), daemon=True).start()

# --- CORAZONCITO ANIMADO QUE SUBE Y BAJA --- 
def floating_heart(start_delay, heart_position):
    heart = turtle.Turtle()
    heart.color("white")
    heart.hideturtle()
    heart.penup()
    heart.goto(heart_position)
    heart.write("❤️", align="center", font=("Arial", 18, "normal"))
    
    # Esperar el retraso antes de comenzar a moverse
    time.sleep(start_delay)
    
    # Movimiento: Subir y bajar el corazón
    while True:
        # Subir el corazón
        for y in range(-180, 160, 2):
            heart.clear()
            heart.goto(heart_position[0], y)
            heart.write("❤️", align="center", font=("Arial", 18, "normal"))
            time.sleep(0.02)

        # Bajar el corazón
        for y in range(160, -180, -2):
            heart.clear()
            heart.goto(heart_position[0], y)
            heart.write("❤️", align="center", font=("Arial", 18, "normal"))
            time.sleep(0.02)

# Iniciar los corazones con retrasos y posiciones diferentes
def start_heart_animation():
    heart_positions = [(-100, -180), (0, -180), (100, -180)]  # Posiciones iniciales de los corazones
    start_delays = [0, 2, 4]  # Retrasos antes de que inicie cada corazón (2 segundos para el segundo, 4 para el tercero)

    for i in range(len(heart_positions)):
        threading.Thread(target=floating_heart, args=(start_delays[i], heart_positions[i]), daemon=True).start()

# Configuración de la pantalla
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Para tixx mi amor,mi pequeñas Campanitas de belen xD")
start_heart_animation()

turtle.done()
