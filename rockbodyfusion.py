import turtle
import threading
import time
import math
import os
import sys
import warnings
import pygame

# ----------------- CONFIG MÚSICA -----------------
AUDIO_FILE = "rockyourbody.mp3"
START_TIME = 31.5

lyrics = [
    ("I wanna da-", 0.0, 0.7),
    ("I wanna dance in the lights", 0.0, 1.2),
    ("I wanna ro-", 0.0, 0.4),
    ("I wanna rock your body", 0.55, 1.2),
    ("I wanna go", 0.02, 0.7),
    ("I wanna go for a ride", 0.0, 1.3),
    ("Hop in the music and", 0.5, 1.2),
    ("Rock your body", 0.0, 1.2),
    ("Rock that body", 0.0, 0.35),
    ("come on, come on", 0.0, 0.25),
    ("rock that body", 0.0, 0.30),
    ("(rock your body)", 0.0, 0.35),
    ("Rock that body", 0.0, 0.30),
    ("come on, come on", 0.0, 0.2),
    ("rock that body", 0.10, 0.30),
]

# ----------------- MÚSICA -----------------


def play_music(start_sec=0):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(AUDIO_FILE)
        pygame.mixer.music.play(start=start_sec)
    except Exception as e:
        print("⚠️ Error con el audio:", e)


# ----------------- VENTANA -----------------
screen = turtle.Screen()
screen.setup(900, 600)
screen.title("#katecito UwU")
screen.bgcolor("black")
screen.tracer(0)


def cerrar_programa():
    try:
        pygame.mixer.music.stop()
        pygame.quit()
    except:
        pass
    turtle.bye()
    os._exit(0)


screen.getcanvas().winfo_toplevel().protocol(
    "WM_DELETE_WINDOW", cerrar_programa)

# --------------- TORTUGAS ---------------
CENTER_X, CENTER_Y = 0, -20

stick = turtle.Turtle()
stick.hideturtle()
stick.color("white")
stick.pensize(4)
stick.speed(0)

label = turtle.Turtle()
label.hideturtle()
label.penup()
label.color("cyan")
label.goto(0, 250)
label.write("#Tiktok", align="center", font=("Arial", 28, "bold"))

bg = turtle.Turtle()
bg.hideturtle()
bg.penup()

# 🆕 Subtítulos abajo 👇
lyrics_writer = turtle.Turtle()
lyrics_writer.hideturtle()
lyrics_writer.color("cyan")
lyrics_writer.penup()
lyrics_writer.goto(0, -250)  # posición abajo estilo subtítulo
lyrics_writer.speed(0)

t0 = time.time()
running = True

# ----------------- FIGURA -----------------


def draw_stick(ax, ay, left_arm_angle, right_arm_angle, left_leg_angle, right_leg_angle, head_tilt):
    stick.penup()
    stick.goto(ax, ay + 90)
    stick.setheading(0)
    stick.pendown()
    stick.circle(18)
    stick.penup()
    stick.goto(ax, ay + 72)
    stick.pendown()
    stick.goto(ax, ay + 10)
    stick.penup()
    stick.goto(ax, ay + 60)
    stick.setheading(left_arm_angle)
    stick.pendown()
    stick.forward(60)
    stick.penup()
    stick.goto(ax, ay + 60)
    stick.setheading(right_arm_angle)
    stick.pendown()
    stick.forward(60)
    stick.penup()
    stick.goto(ax, ay + 10)
    stick.pendown()
    stick.goto(ax, ay - 60)
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

# ----------------- ANIMACIÓN -----------------


def dance_loop():
    fps_sleep = 1/30
    while running:
        now = time.time() - t0
        beat = 0.5 + 0.5 * math.sin(now * 2.5)

        # Fondo con pulso sutil
        bg.clear()
        steps = 36
        radius = 260 * (0.85 + 0.15 * beat)
        for i in range(steps):
            ang = 2 * math.pi * i / steps
            x = math.cos(ang) * radius
            y = math.sin(ang) * radius + 10
            bg.goto(x, y)
            bg.dot(3, "#101010")

        # Movimiento del stickman
        arm_swing = math.sin(now * 6.0) * 45
        leg_swing = math.sin(now * 4.0) * 30
        head_tilt = math.sin(now * 2.5) * 10

        stick.clear()
        draw_stick(CENTER_X, CENTER_Y, 220 - arm_swing, -40 - arm_swing,
                   240 + leg_swing, -60 - leg_swing, head_tilt)

        # Hashtag animado
        label.clear()
        color_intensity = int(155 + 100 * beat)
        color_hex = "#{:02x}{:02x}{:02x}".format(
            0, color_intensity, 255 - color_intensity//2)
        label.color(color_hex)
        label.goto(0, 250)
        label.write("#Tiktok", align="center",
                    font=("Arial", 28, "bold"))

        screen.update()
        time.sleep(fps_sleep)

# ----------------- SUBTÍTULOS -----------------


def typewriter_window(texto, pre_delay, post_delay):
    time.sleep(pre_delay)
    lyrics_writer.clear()
    lyrics_writer.goto(0, -250)  # 👈 abajo estilo subtítulo
    output = ""
    for char in texto:
        output += char
        lyrics_writer.clear()
        lyrics_writer.write(output, align="center",
                            font=("Courier", 26, "bold"))
        screen.update()
        time.sleep(0.045)
    time.sleep(post_delay)


def lyrics_loop():
    warnings.filterwarnings("ignore", category=UserWarning)
    for frase, pre, post in lyrics:
        typewriter_window(frase, pre, post)
    global running
    running = False
    time.sleep(2)
    cerrar_programa()


# ----------------- EJECUCIÓN -----------------
threading.Thread(target=play_music, args=(START_TIME,), daemon=True).start()
threading.Thread(target=dance_loop, daemon=True).start()
threading.Thread(target=lyrics_loop, daemon=True).start()

turtle.done()
