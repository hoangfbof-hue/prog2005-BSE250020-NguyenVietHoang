import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)
y1 = x**2
y2 = x**3

plt.figure(figsize=(10, 6))
plt.plot(x, y1, color='blue', linestyle='-', linewidth=2, label='$y = x^2$')

plt.plot(x, y2, color='red', linestyle='--', linewidth=2, label='$y = x^3$')

plt.title('Đồ thị so sánh hàm số $y = x^2$ và $y = x^3$', fontsize=14)
plt.xlabel('Trục X', fontsize=12)
plt.ylabel('Trục Y', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='best', fontsize=11)
plt.show()
