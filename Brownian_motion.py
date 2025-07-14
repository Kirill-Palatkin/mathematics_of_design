import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


num_balls = 20
radius = 0.03
box_size = 2.0
mass = 1.0

positions = np.random.rand(num_balls, 2) * box_size
velocities = np.random.randn(num_balls, 2) * 0.05
colors = np.random.rand(num_balls, 3)

fig, ax = plt.subplots()
ax.set_xlim(0, box_size)
ax.set_ylim(0, box_size)
ax.set_aspect('equal')

circles = [plt.Circle((x, y), radius, color=color) for x, y, color in zip(positions[:, 0], positions[:, 1], colors)]
for circle in circles:
    ax.add_patch(circle)


def update(frame):
    global positions, velocities

    positions += velocities

    for i in range(num_balls):
        if positions[i, 0] < radius or positions[i, 0] > box_size - radius:
            velocities[i, 0] = -velocities[i, 0]
        if positions[i, 1] < radius or positions[i, 1] > box_size - radius:
            velocities[i, 1] = -velocities[i, 1]

    for i in range(num_balls):
        for j in range(i + 1, num_balls):
            dist = np.linalg.norm(positions[i] - positions[j])
            if dist < 2 * radius:
                normal = positions[i] - positions[j]
                normal /= np.linalg.norm(normal)

                tangent = np.array([-normal[1], normal[0]])

                v1n = np.dot(velocities[i], normal)
                v1t = np.dot(velocities[i], tangent)
                v2n = np.dot(velocities[j], normal)
                v2t = np.dot(velocities[j], tangent)

                v1n_new = (v1n * (mass - mass) + 2 * mass * v2n) / (mass + mass)
                v2n_new = (v2n * (mass - mass) + 2 * mass * v1n) / (mass + mass)

                velocities[i] = v1n_new * normal + v1t * tangent
                velocities[j] = v2n_new * normal + v2t * tangent

    for i, circle in enumerate(circles):
        circle.center = positions[i]

    return circles


ani = animation.FuncAnimation(fig, update, frames=1000, interval=20, blit=True)

plt.show()
