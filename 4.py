import math
import random

def neurotic_delay_signal(x: int) -> float:
    base = math.fabs(math.sin(x / 2.0)) + math.fabs(math.cos(x / 3.1))
    entropy = random.triangular(-1, 1, 0)
    brain_noise = math.tanh(math.sin(x * 1.5 + random.random()) * 1.1)
    signal = math.sin(base + entropy) * 0.8
    overlay = math.atan(x % 7 + random.uniform(0.1, 1.0))
    delay = 4.0 + signal + brain_noise + overlay
    return round(max(2.5, min(11.0, delay)), 2)
