import subprocess
import time
import pyautogui


def consolaOpen(ruta, command):
    subprocess.Popen('start cmd', shell=True)
    time.sleep(1.5)
    pyautogui.write('cd /d ' + ruta)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.write(command)
    pyautogui.press('enter')


commandngrok = "ngrok http --url=protrusible-miki-hooly.ngrok-free.app 5678"
commandwhisper = "python -m uvicorn whisper_api:app --host 0.0.0.0 --port 8000"
rutadalto = "D:\\MisProyectos-Programacion\\Visual-Studio-Code-Proyects\\Python-Proyects\\CursoPython-Dalto"


# Open n8n
consolaOpen("C:\\Users\\Usuario\\n8n-project-local-SinDocker", "n8n")

# Open Whisper
consolaOpen(rutadalto, commandwhisper)

# Open Ngrok
# consolaOpen("C:\\Windows\\system32", commandngrok)

# Open Local Tunel
# consolaOpen("C:\\Users\\Usuario", "lt --port 3000 --subdomain=katecito")
