from pyboy import PyBoy

pyboy = PyBoy('pokemon_rote.gb')

try:
    while True:
        pyboy.tick()
except KeyboardInterrupt:
    print("Cerrando el emulador...")
finally:
    pyboy.stop()