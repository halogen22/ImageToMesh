import cv2
import matplotlib.pyplot as plt
import numpy as np
import trimesh
from trimesh.exchange import export


class STLModel:

    def __init__(self, vertices: np.ndarray, faces: np.ndarray, stl_heights: np.ndarray):
        """
        Initialize the STLModel instance.

        Args:
            vertices (np.ndarray): Array of vertex coordinates.
            faces (np.ndarray): Array of face indices.
        """
        self._vertices: np.ndarray = vertices
        self._faces: np.ndarray = faces
        self._stl_heights: np.ndarray = stl_heights
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

    def save_as_stl(self, output_stl: str) -> None:
        """
        Save the STL model as an STL file.

        Args:
            output_stl (str): File path to save the STL.
        """
        STL_SIGNATUR: str = "stl"
        if output_stl.split(".")[-1] != STL_SIGNATUR:
            output_stl = output_stl + STL_SIGNATUR
        export.export_mesh(self.get_mesh(), output_stl)
        print(f"STL file saved as '{output_stl}'.")

    def description(self) -> None:
        """Print details of the STL model including volume and mass properties."""
        stl_mesh: trimesh.Trimesh = self.get_mesh()
        volume: float = stl_mesh.volume
        center_of_mass: list[float] = stl_mesh.center_mass
        inertia: list[list[float]] = stl_mesh.moment_inertia

        print(f"Volume: {volume}")
        print(f"Center Mass: {center_of_mass}")
        print(f"Inertia: {inertia}")

    def display_3d_view(self) -> None:
        """Display the 3D view of the STL model."""
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
            stl_heights (np.ndarray): Height map used for visualization.
            cmap (str): Colormap to use for visualization. Default is 'viridis'.
        """
        plt.figure(figsize=(10, 10))
        plt.imshow(self._stl_heights, cmap=cmap, origin='upper')
        plt.colorbar(label="Height (z_top values)")
        plt.title("Top-down 2D View (Height Map)")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()