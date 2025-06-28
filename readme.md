# 🧠 Human-Like Delay Generator

This project provides a collection of complex mathematical delay functions designed to simulate **human-like behavior** in automated scripts or bots.

Unlike basic `time.sleep(random.uniform(2, 5))` strategies, these delay functions use **chaotic waves, non-linear curves, entropy, and noise** to produce delays that are much harder to detect as artificial by anti-bot systems.

---

## 🚀 Features

- Multiple complex delay models
- Each function uses a unique combination of math patterns, randomness, and entropy
- Delays are clamped to a safe and realistic range (typically 2–12 seconds)
- Useful for anti-detection layers in automation tasks (e.g. joining, boosting, clicking)

---

## 📦 Functions

### `chaotic_human_delay(x: int) -> float`
Produces chaotic delays using trigonometric feedback loops and Gaussian jitter.

### `organic_delay_curve(x: int) -> float`
Generates smooth wave-based delays mimicking organic response curves.

### `neurotic_delay_signal(x: int) -> float`
Combines entropy, tanh noise, and signal-based delay randomness.

### `fractal_sync_delay(x: int) -> float`
Uses recursion-like sinusoidal forms to produce fractal-inspired delay timings.

---

## 📌 Example

```python
from delays import chaotic_human_delay
import time

for i in range(10):
    delay = chaotic_human_delay(i)
    print(f"Waiting for {delay} seconds...")
    time.sleep(delay)
