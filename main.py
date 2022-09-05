from machine import I2S
from machine import Pin

SCK_PIN = 32
WS_PIN = 25
SD_PIN = 33
I2S_ID = 0
BUFFER_LENGTH_IN_BYTES = 2000

audio_out = I2S(
    1,
    sck=Pin(SCK_PIN),
    ws=Pin(WS_PIN),
    sd=Pin(SD_PIN),
    mode=I2S.TX,
    bits=16,
    format=I2S.STEREO,
    rate=44100,
    ibuf=9600)

samples = bytearray(2048)


with open("Ding-dong-2s.wav", "rb") as file:
    samples_read = file.readinto(samples)
    while samples_read > 0:
        audio_out.write(samples[:samples_read])
        samples_read = file.readinto(samples)
