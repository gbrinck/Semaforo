#Semaforo y pulsador
import machine
import utime
import _thread

led_rojo = machine.Pin(15, machine.Pin.OUT)
led_verde = machine.Pin(13, machine.Pin.OUT)
led_amarillo = machine.Pin(14, machine.Pin.OUT)

boton = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
bocina = machine.Pin(17, machine.Pin.OUT)

global boton_presionado
boton_presionado = False

def boton_estado():
    global boton_presionado
    while True:
        if boton.value() == 1:
            boton_presionado = True
        utime.sleep(0.01)
            
_thread.start_new_thread(boton_estado, ())


while True:
    led_verde.value(1)
    utime.sleep(5)
    led_verde.value(0)
    led_amarillo.value(1)
    utime.sleep(2)
    led_amarillo.value(0)
    led_rojo(1)
    utime.sleep(3)
    if boton_presionado == True:
        for veces in range(10):
            bocina.value(1)
            utime.sleep(0.2)
            bocina.value(0)
            utime.sleep(0.2)
        global boton_presionado
        boton_presionado = False
    led_rojo(0)