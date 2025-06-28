import math
import random

def fractal_sync_delay(x: int) -> float:
    base_wave = math.sin(x * 0.8 + math.cos(x / 2.0))
    recursion = math.sin(math.sin(x / 1.3 + random.uniform(-0.4, 0.4)))
    modulation = math.exp(-abs(math.sin(x))) * 1.2
    randomness = random.uniform(-0.5, 0.5)
    noise_overlay = math.log(x + 5.0) * 0.6 + randomness
    delay = 3.7 + base_wave + recursion + modulation + noise_overlay
    return round(max(2.0, min(12.0, delay)), 2)
