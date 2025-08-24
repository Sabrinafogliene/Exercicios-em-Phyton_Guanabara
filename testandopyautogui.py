import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.5#A cada comenando espera 0.3 segundos

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("Nome Oliver Origem")
pyautogui.press("enter")
#pyautogui.hotkey('ctrl', 'c') para combinação de teclas