import math
import random

def organic_delay_curve(x: int) -> float:
    phase_shift = math.pi / 3 + random.uniform(-0.2, 0.2)
    oscillation = math.sin(x * 0.9 + phase_shift) + math.sin(x / 3.7)
    variability = math.sqrt(abs(math.cos(x * 0.5))) * random.uniform(0.5, 1.5)
    pulse = math.tanh(math.sin(x / 2.5) * 1.3)
    chaos = random.uniform(-1.0, 1.0) * 0.4
    delay = 5.0 + oscillation + variability + pulse + chaos
    return round(max(1.8, min(12.0, delay)), 2)
