#Semaforo
import machine
import utime

led_rojo = machine.Pin(15, machine.Pin.OUT)
led_verde = machine.Pin(13, machine.Pin.OUT)
led_amarillo = machine.Pin(14, machine.Pin.OUT)

while True:
    led_verde.value(1)
    utime.sleep(5)
    led_verde.value(0)
    led_amarillo.value(1)
    utime.sleep(2)
    led_amarillo.value(0)
    led_rojo(1)
    utime.sleep(3)
    led_rojo(0)