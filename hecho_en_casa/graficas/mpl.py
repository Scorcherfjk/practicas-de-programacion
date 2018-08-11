import matplotlib.pyplot as plt
from random import sample

fig, axes = plt.subplots(nrows=2, ncols=2)
        
x = range(1,11)
y1 = sample(range(20), len(x))
y2 = sample(range(20), len(x))
y3 = sample(range(20), len(x))
y4 = sample(range(20), len(x))

axes[0,0].plot(x, y1)
axes[0,0].set_title("Gráfico 1")

axes[0,1].stem(x, y2)
axes[0,1].set_title("Gráfico 2")

axes[1,0].step(x, y3)
axes[1,0].set_title("Gráfico 3")

axes[1,1].bar(x, y4)
axes[1,1].set_title("Gráfico 4")

fig.tight_layout()
plt.show()