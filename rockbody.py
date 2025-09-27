import turtle
import threading
import time
import math
import os
import sys

# ----------------- MÚSICA -----------------


def play_music(start_sec=0):
    try:
        import pygame
    except Exception:
        print("pygame no instalado: la música no sonará.")
        return

    try:
        pygame.mixer.init()
    except Exception as e:
        print("No se pudo inicializar audio:", e)
        return

    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    audio_path = os.path.join(base_path, "rockyourbody.mp3")
    if not os.path.isfile(audio_path):
        print("No se encontró audio.mp3 en:", base_path)
        return

    try:
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play(start=start_sec)
    except Exception as e:
        print("Error reproduciendo audio:", e)


# Arranca la música en hilo (comenta si no quieres música)
threading.Thread(target=play_music, args=(0,), daemon=True).start()


# ----------------- VENTANA -----------------
screen = turtle.Screen()
screen.setup(900, 600)
screen.title("#rockyourbody")
screen.bgcolor("black")
screen.tracer(0)  # actualizaciones manuales para suavizar

# Para cerrar limpio


def cerrar_programa():
    try:
        import pygame
        pygame.mixer.music.stop()
        pygame.quit()
    except:
        pass
    turtle.bye()
    os._exit(0)


screen.getcanvas().winfo_toplevel().protocol(
    "WM_DELETE_WINDOW", cerrar_programa)


# --------------- ELEMENTOS DE DIBUJO ---------------
CENTER_X, CENTER_Y = 0, -20

# figura (stick) - usaremos una tortuga para las líneas del cuerpo
stick = turtle.Turtle()
stick.hideturtle()
stick.color("white")
stick.pensize(4)
stick.speed(0)

# texto #rockyourbody
label = turtle.Turtle()
label.hideturtle()
label.penup()
label.color("cyan")
label.goto(0, 250)
label.write("#rockyourbody", align="center", font=("Arial", 28, "bold"))

# fondo pulso
bg = turtle.Turtle()
bg.hideturtle()
bg.penup()

# parámetros de animación
t0 = time.time()
running = True

# función para dibujar el cuerpo según ángulos


def draw_stick(ax, ay, left_arm_angle, right_arm_angle, left_leg_angle, right_leg_angle, head_tilt):
    stick.clear()
    # cabeza
    stick.penup()
    stick.goto(ax, ay + 90)
    stick.setheading(0)
    stick.pendown()
    stick.circle(18)  # cabeza

    # cuello -> torso
    stick.penup()
    stick.goto(ax, ay + 72)
    stick.pendown()
    stick.goto(ax, ay + 10)

    # brazos
    # brazo izquierdo
    stick.penup()
    stick.goto(ax, ay + 60)
    stick.setheading(left_arm_angle)
    stick.pendown()
    stick.forward(60)

    # brazo derecho
    stick.penup()
    stick.goto(ax, ay + 60)
    stick.setheading(right_arm_angle)
    stick.pendown()
    stick.forward(60)

    # torso al ombligo
    stick.penup()
    stick.goto(ax, ay + 10)
    stick.pendown()
    stick.goto(ax, ay - 60)

    # piernas
    stick.penup()
    stick.goto(ax, ay - 60)
    stick.setheading(left_leg_angle)
    stick.pendown()
    stick.forward(80)

    stick.penup()
    stick.goto(ax, ay - 60)
    stick.setheading(right_leg_angle)
    stick.pendown()
    stick.forward(80)


# animación principal: la figura "baila"
def dance_loop():
    fps_sleep = 1/30
    beat = 0
    amplitude = 1
    while running:
        now = time.time() - t0
        # pulso de fondo (latido) - basado en seno
        beat = 0.5 + 0.5 * math.sin(now * 2.5)  # velocidad del pulso
        radius = 300 * (0.85 + 0.15 * beat)

        # dibujar fondo circular pulsante (no relleno grande para no tapar)
        bg.clear()
        bg.goto(0, -radius - 50)
        bg.color((0.05 * beat + 0.05, 0.0, 0.0))
        # hacemos un "halo" con puntos
        steps = 36
        for i in range(steps):
            ang = 2 * math.pi * i / steps
            x = math.cos(ang) * radius
            y = math.sin(ang) * radius + 10
            bg.goto(x, y)
            bg.dot(int(4 + 4 * beat), ("#161616" if beat < 0.6 else "#222222"))

        # parámetros de movimiento del stick (basados en seno y cos)
        sway = math.sin(now * 3.0) * 12  # inclinación cuerpo
        arm_swing = math.sin(now * 6.0) * 45  # swing brazos
        leg_swing = math.sin(now * 4.0) * 30  # swing piernas
        head_tilt = math.sin(now * 2.5) * 10

        # dibuja varias figuras para dar efecto 'eco' y movimiento
        # figura central
        draw_stick(CENTER_X, CENTER_Y, 220 - arm_swing, -40 -
                   arm_swing, 240 + leg_swing, -60 - leg_swing, head_tilt)

        # una figura levemente a la izquierda y otra a la derecha para sensación de pista
        draw_stick(CENTER_X - 140, CENTER_Y - 10, 220 - arm_swing*0.7, -40 -
                   arm_swing*0.7, 240 + leg_swing*0.6, -60 - leg_swing*0.6, head_tilt*0.6)
        draw_stick(CENTER_X + 140, CENTER_Y - 10, 220 - arm_swing*0.7, -40 -
                   arm_swing*0.7, 240 + leg_swing*0.6, -60 - leg_swing*0.6, head_tilt*0.6)

        # añadir texto hashtag con pulso de color
        label.clear()
        color_intensity = int(155 + 100 * beat)
        color_hex = "#{:02x}{:02x}{:02x}".format(
            0, color_intensity, 255 - color_intensity//2)
        label.color(color_hex)
        label.goto(0, 250)
        label.write("#rockyourbody", align="center",
                    font=("Arial", 28, "bold"))

        screen.update()
        time.sleep(fps_sleep)


# Ejecutar hilo de animación
anim_thread = threading.Thread(target=dance_loop, daemon=True)
anim_thread.start()

# Mantener ventana abierta hasta que el usuario la cierre
turtle.done()
