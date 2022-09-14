from pynput.keyboard import Key, Controller
import time

keyboard = Controller() 

time.sleep(10) #so um tempo p preparar tudinho

keyboard.press(Key.space)
i = 0
while i != 37 * 255: #37 idas e vindas dao um ponto de amizade, c maximo de 255 pontos, entao roda ate maximizar
    keyboard.press(Key.left)
    time.sleep(0.15)
    keyboard.release(Key.left)
    keyboard.press(Key.right)
    time.sleep(0.15)
    keyboard.release(Key.right)
    i += 1