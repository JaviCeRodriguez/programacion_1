import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo: int) -> np.ndarray:
    """Genera una caminata aleatoria de largo 'largo'."""
    pasos = np.random.randint(-1,2,largo)    
    return pasos.cumsum()

N = 100000
colors = plt.cm.rainbow(np.linspace(0, 1, 12))

walks = [randomwalk(N) for _ in range(12)]
plt.subplot(2, 2, (1, 2), title='12 Caminatas al azar', ylabel='Distancia al origen', xlabel='Pasos')
for idx, walk in enumerate(walks):
    plt.plot(walk, color=colors[idx])
plt.axhline(0, color='black', linewidth=0.5)

plt.subplot(2, 2, 3, title='La caminata que más se aleja', ylabel='Distancia al origen', xlabel='Pasos')
idx_min_walk = np.argmin([np.abs(walk[-1]) for walk in walks])
print('La caminata que más se aleja es la número', idx_min_walk)
plt.plot(walks[idx_min_walk], color=colors[idx_min_walk])

plt.subplot(2, 2, 4, title='La caminata que menos se aleja', ylabel='Distancia al origen', xlabel='Pasos')
idx_max_walk = np.argmax([np.abs(walk[-1]) for walk in walks])
plt.plot(walks[idx_max_walk], color=colors[idx_max_walk])
print('La caminata que menos se aleja es la número', idx_max_walk)
plt.show()