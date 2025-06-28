import math
import random

def chaotic_human_delay(x: int) -> float:
    wave = math.sin(x / 1.5 + random.uniform(-0.5, 0.5)) * 1.1
    decay = math.exp(-x / 50.0)
    jitter = random.gauss(0, 0.6)
    feedback = math.sin(wave * x + jitter) * math.cos(x / 2.1)
    offset = math.log(x + 4.2) * 0.7 + random.uniform(-0.3, 0.3)
    delay = 3.5 + wave + decay + feedback + offset + jitter
    return round(max(2.0, min(11.5, delay)), 2)
