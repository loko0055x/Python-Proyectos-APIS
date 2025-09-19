import turtle
import pygame
import threading
import random
import time
import os
import sys
# --- MÚSICA (opcional) ---


#def play_music():
#    pygame.mixer.init()
#    pygame.mixer.music.load("audio.mp3")   
#    pygame.mixer.music.play(start=115)   
    


def play_music():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print(f"Error al inicializar el mixer: {e}")
        return  # Sale de la función si falla el mixer

    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    ruta_audio = os.path.join(base_path, "audio.mp3")

    try:
        pygame.mixer.music.load(ruta_audio)
        pygame.mixer.music.play(start=105)
    except pygame.error as e:
        print(f"Error al reproducir audio: {e}")
        
        
        
threading.Thread(target=play_music, daemon=True).start()

# --- CONFIGURACIÓN DE VENTANA ---
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("🎵😉💖 La luz de mi Alma 🎶… ")

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
    "Mi amor, estos días han sido mágicos para mí, xD.\n"
    "Cuatro semanas a tu lado se sienten\nComo un mes lleno de cosas bonitas. UwU\n"
    "Gracias por tu paciencia, tu cariño Me encantas\n"
    "Te quiero mucho ❤️ maylov \nmás de lo que las palabras pueden expresar.❤️\n"
    "De todo lo que pasó este año,tú eres de las cosas más bonitas.\n"
    "DE you para vo xdddd Belen 🌟😊❤️ #15 "
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

def cerrar_programa():
    pygame.mixer.music.stop()
    pygame.quit()
    turtle.bye()
    os._exit(0)  # Mata todos los hilos de golpe de forma segura

# Detectar el cierre de ventana (la X)
screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", cerrar_programa)

# Configuración de la pantalla
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Para ti, mi amor ❤️ Mi Pequeña Campanitas de Belen.")
start_heart_animation()

turtle.done()
