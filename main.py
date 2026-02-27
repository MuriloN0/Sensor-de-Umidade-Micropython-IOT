from machine import Pin, ADC
import time

# Pinos atualizados conforme sua nova imagem
sensor = ADC(Pin(34))
sensor.atten(ADC.ATTN_11DB)

led_vermelho = Pin(12, Pin.OUT)
led_verde = Pin(14, Pin.OUT)
led_azul = Pin(27, Pin.OUT)
rele = Pin(26, Pin.OUT)

while True:
    # Leitura de 0 a 100%
    valor = (sensor.read() / 4095) * 100
    print(f"Umidade: {valor:.1f}%")

    # Lógica dos LEDs
    if valor < 30:
        led_vermelho.value(1) # LIGA
        led_verde.value(0)
        led_azul.value(0)
        rele.value(1)        # Liga bomba
    elif 30 <= valor <= 70:
        led_vermelho.value(0)
        led_verde.value(1)    # LIGA
        led_azul.value(0)
        rele.value(0)
    else:
        led_vermelho.value(0)
        led_verde.value(0)
        led_azul.value(1)     # LIGA
        rele.value(0)

    time.sleep(0.5)
