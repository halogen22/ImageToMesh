import cv2
import matplotlib.pyplot as plt
import numpy as np
import trimesh
from trimesh.exchange import export


class Model3D:

    def __init__(self, vertices: np.ndarray, faces: np.ndarray, heights: np.ndarray):
        """
        Initialize the Model3D instance.

        Args:
            vertices (np.ndarray): Array of vertex coordinates.
            faces (np.ndarray): Array of face indices.
            heights (np.ndarray): Height map used for visualization.
        """
        self._vertices: np.ndarray = vertices
        self._faces: np.ndarray = faces
        self._heights: np.ndarray = heights
        self._stl_mesh: trimesh.Trimesh | None = self._convert_mesh()

    def _convert_mesh(self) -> None:
        """Convert vertices and faces into a Trimesh object."""
        try:
            stl_mesh: trimesh.Trimesh = trimesh.Trimesh(vertices=self._vertices, faces=self._faces)
            # TODO: Investigation why this error(watertight) occurs
            # if not stl_mesh.is_watertight:
            #     raise ValueError("Mesh is not watertight.")
            self._stl_mesh = stl_mesh
        except Exception as e:
            raise RuntimeError(f"An error occurred during mesh conversion: {e}")

    def get_mesh(self) -> trimesh.Trimesh:
        """Get the STL mesh object, generating it if necessary."""
        if self._stl_mesh is None:
            self._convert_mesh()
        return self._stl_mesh

    def save_as_stl(self, output_file: str) -> None:
        """
        Save the 3D model as an file.

        Args:
            output_file (str): File path to save the file(e.g.stl).
        """
        export.export_mesh(self.get_mesh(), output_file)
        print(f"File saved as '{output_file}'.")

    def description(self) -> None:
        """Print details of the 3D model including volume and mass properties."""
        mesh: trimesh.Trimesh = self.get_mesh()
        volume: float = mesh.volume
        center_of_mass: list[float] = mesh.center_mass
        inertia: list[list[float]] = mesh.moment_inertia

        print(f"Volume: {volume}")
        print(f"Center Mass: {center_of_mass}")
        print(f"Inertia: {inertia}")

    def display_3d_view(self) -> None:
        """Display the 3D view of the 3D model."""
        try:
            self.get_mesh().show()
        except:
            raise ValueError(
                "Failed to display the 3D model.\n"
                "The input mesh may be invalid.\n"
                f"Details: {e}")
        
    def display_2d_view(self, cmap: str = 'viridis') -> None:
        """
        Display a top-down 2D view based on the height map.

        Args:
            cmap (str): Colormap to use for visualization. Default is 'viridis'.
        """
        plt.figure(figsize=(10, 10))
        plt.imshow(self._heights, cmap=cmap, origin='upper')
        plt.colorbar(label="Height (z_top values)")
        plt.title("Top-down 2D View (Height Map)")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()