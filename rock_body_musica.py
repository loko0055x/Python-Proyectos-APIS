import time
from rich.console import Console

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

console = Console()

# Colores alternados y emojis
colors = ["bold white on black", "bold magenta on black", "bold cyan on black"]
emojis = [" 🔥", " 🎧", " 💪", " ✨", " 🚀"]


def typewriter(texto, pre_delay, post_delay, style, emoji):
    time.sleep(pre_delay)
    for char in texto:
        console.print(char, style=style, end="")
        time.sleep(0.045)
    console.print(emoji)
    time.sleep(post_delay)


# Título
console.print(
    "[bold cyan on black]🎤Tiktok  🚀[/bold cyan on black]\n")

# Subtítulos
for i, (frase, pre, post) in enumerate(lyrics):
    style = colors[i % len(colors)]
    emoji = emojis[i % len(emojis)]
    typewriter(frase, pre, post, style, emoji)
