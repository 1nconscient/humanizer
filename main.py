import math
import random

def ultra_human_delay(x: int) -> float:
    wave1 = math.sin(0.73 * x + random.uniform(-0.2, 0.2))
    wave2 = math.cos((x / 3.1) + math.pi + random.uniform(-0.1, 0.1)) * 0.85
  
    nonlinear = math.exp(math.sin(x / 4.2 + 0.5)) / math.log(x + 3.8)

    chaos = random.uniform(-1, 1) / (1 + abs(math.cos(x + 0.1)))

    weirdness = math.tanh(math.sin(x / 1.8) * math.cos(x / 2.2 + 1.5))

    decoy = (math.atan(x % 5 + random.random()) ** 2) / 4

    delay = (
        4.2 + wave1 + wave2 + nonlinear + chaos + weirdness + decoy
    )

    delay = round(max(2.0, min(12.0, delay)), 2)
    return delay
