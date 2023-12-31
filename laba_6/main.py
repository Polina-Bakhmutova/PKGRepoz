import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.spatial.transform import Rotation
import mplcursors
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class Interactive3DPlot:
    def __init__(self, vertices):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_box_aspect([1, 1, 1])
        self.vertices = vertices
        self.rotation_matrix = np.eye(3)

    def create_letter_B(self):
        return np.array([
            [0, 0, 0],
            [1, 0, 0],
            [1, 0.4, 0],
            [0.6, 0.4, 0],
            [0.6, 0.6, 0],
            [1, 0.6, 0],
            [1, 1, 0],
            [0, 1, 0],
            [0, 1, 1],
            [1, 1, 1],
            [1, 0, 1],
            [0, 0, 1],
        ])

    def apply_transformation(self, vertices):
        return np.dot(vertices, self.rotation_matrix)

    def plot_3d(self, event=None):
        self.ax.clear()
        rotated_vertices = self.apply_transformation(self.vertices)
        faces = [
            [rotated_vertices[0], rotated_vertices[1], rotated_vertices[5], rotated_vertices[6]],
            [rotated_vertices[1], rotated_vertices[2], rotated_vertices[4], rotated_vertices[5]],
            [rotated_vertices[2], rotated_vertices[3], rotated_vertices[4]],
            [rotated_vertices[4], rotated_vertices[5], rotated_vertices[8], rotated_vertices[9]],
            [rotated_vertices[5], rotated_vertices[6], rotated_vertices[7], rotated_vertices[8]],
            [rotated_vertices[9], rotated_vertices[10], rotated_vertices[11], rotated_vertices[8]],
        ]
        colors = ['red', 'green', 'blue', 'purple', 'orange', 'pink']
        self.ax.add_collection3d(Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.5))
        self.ax.quiver(0, 0, 0, 1.2, 0, 0, color='red', arrow_length_ratio=0.1)
        self.ax.quiver(0, 0, 0, 0, 1.2, 0, color='green', arrow_length_ratio=0.1)
        self.ax.quiver(0, 0, 0, 0, 0, 1.2, color='purple', arrow_length_ratio=0.1)
        self.ax.set_title("Rotated Letter B")
        self.ax.set_box_aspect([1, 1, 1])
        mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(f'({sel.target[0]:.2f}, {sel.target[1]:.2f}, {sel.target[2]:.2f})'))
        plt.draw()

    def on_key_event(self, event):
        if event.key == 'left':
            self.rotation_matrix = Rotation.from_rotvec(-np.radians(10) * np.array([0, 0, 1])).as_matrix() @ self.rotation_matrix
        elif event.key == 'right':
            self.rotation_matrix = Rotation.from_rotvec(np.radians(10) * np.array([0, 0, 1])).as_matrix() @ self.rotation_matrix
        elif event.key == 'up':
            self.rotation_matrix = Rotation.from_rotvec(-np.radians(10) * np.array([1, 0, 0])).as_matrix() @ self.rotation_matrix
        elif event.key == 'down':
            self.rotation_matrix = Rotation.from_rotvec(np.radians(10) * np.array([1, 0, 0])).as_matrix() @ self.rotation_matrix
        self.plot_3d()

    def run(self):
        self.vertices = self.create_letter_B()
        self.fig.canvas.mpl_connect('key_press_event', self.on_key_event)
        self.plot_3d()
        plt.show()

if __name__ == "__main__":
    app = Interactive3DPlot([])
    app.run()
