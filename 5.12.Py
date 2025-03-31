import matplotlib.pyplot as plt, 
import numpy as np
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label="Sine Wave")
plt.plot(x, y2, label="Cosine Wave")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Sine and Cosine Waves")
plt.legend()
plt.show()
