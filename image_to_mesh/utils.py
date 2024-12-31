import numpy as np
from .mesh_model import MeshModel


class MeshGenerator:

    @classmethod
    def generate_mesh(cls, image: np.ndarray, pixel_width: float, thickness: float) -> MeshModel:
        """
        Generate MeshModel data from a 2D image.

        Args:
            image (np.ndarray): 2D grayscale image array.
            pixel_width (float): Width of each pixel in the model.
            thickness (float): Thickness of the bottom plane.

        Returns:
            MeshModel: Generated 3D model object.
        """
        image: np.ndarray = cls._load_image(image)
        height: int = image.shape[0]
        width: int = image.shape[1]
        vertices: list[list[float]] = cls._generate_vertices(image, pixel_width, thickness)
        faces: list[list[int]] = cls._generate_faces(height, width)
        return MeshModel(vertices, faces, image)

    @staticmethod
    def _load_image(image: np.ndarray) -> np.ndarray:
        """
        Validate and load a 2D image.

        Args:
            image (np.ndarray): Input image array.

        Returns:
            np.ndarray: Validated 2D image.

        Raises:
            ValueError: If the input image is not 2D.
        """
        if len(image.shape) != 2:
            raise ValueError(f"Invalid image shape '{image.shape}'. Input must be a 2D array.")
        return image
        
    @staticmethod
    def _generate_vertices(heights: np.ndarray, pixel_width: float, thickness: float) -> list[list[float]]:
        """
        Generate vertices for the mesh model.

        Args:
            heights (np.ndarray): 2D image array.
            pixel_width (float): Width of each pixel in the model.
            thickness (float): Thickness of the bottom plane.

        Returns:
            tuple[list[list[float]], np.ndarray]: List of vertices and height map.
        """
        height, width = heights.shape
        vertices = []

        for y in range(height):
            for x in range(width):
                z_top = heights[y, x]
                vertices.append([x * pixel_width, y * pixel_width, z_top])
                z_bottom = -thickness
                vertices.append([x * pixel_width, y * pixel_width, z_bottom])

        return vertices

    @staticmethod
    def _generate_faces(height: int, width: int) -> list[list[int]]:
        """
        Generate faces for the STL model.

        Args:
            height (int): Height of the 2D image.
            width (int): Width of the 2D image.

        Returns:
            list[list[int]]: List of faces for the STL model.
        """
        faces = []

        # Top surface
        for y in range(height - 1):
            for x in range(width - 1):
                top_v0 = (y * width + x) * 2
                top_v1 = (y * width + (x + 1)) * 2
                top_v2 = ((y + 1) * width + x) * 2
                top_v3 = ((y + 1) * width + (x + 1)) * 2

                faces.append([top_v0, top_v1, top_v2])
                faces.append([top_v1, top_v3, top_v2])

        # Bottom surface
        for y in range(height - 1):
            for x in range(width - 1):
                bottom_v0 = (y * width + x) * 2 + 1
                bottom_v1 = (y * width + (x + 1)) * 2 + 1
                bottom_v2 = ((y + 1) * width + x) * 2 + 1
                bottom_v3 = ((y + 1) * width + (x + 1)) * 2 + 1

                faces.append([bottom_v0, bottom_v2, bottom_v1])
                faces.append([bottom_v1, bottom_v2, bottom_v3])

        # Sides - Internal
        for y in range(height - 1):
            for x in range(width - 1):
                left_top = (y * width + x) * 2
                left_bottom = left_top + 1
                right_top = (y * width + (x + 1)) * 2
                right_bottom = right_top + 1

                faces.append([left_top, left_bottom, right_bottom])
                faces.append([left_top, right_bottom, right_top])

        # Remove duplicate faces
        faces = np.unique(np.array(faces), axis=0).tolist()

        return faces
    