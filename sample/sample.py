import cv2
import sys
sys.path.append("~/imageToStl")

from image_to_mesh import MeshGenerator


# Define the image path and parameters
image_path = "./sample_img/4.1.04.tiff"  # Path to the input grayscale image
pixel_width = 1  # Width of each pixel in the generated 3D model
thickness = 1  # Thickness of the bottom plane in the STL model

# Load the image in grayscale
# Note: cv2.IMREAD_GRAYSCALE ensures the image is loaded as a 2D array of pixel intensities (0-255)
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Normalize the image to a range of [0, 1] for further processing
# This allows max_height to scale the pixel intensities proportionally
normalized_image = ((image / 255))* 10

# Generate the STL model using the normalized image and parameters
# The MeshGenerator.generate_mesh method creates vertices and faces for the 3D representation
mesh = MeshGenerator.generate_mesh(normalized_image, pixel_width, thickness)

# Display the generated 3D model for verification
# Opens an interactive 3D viewer for inspecting the model
mesh.display_3d_view()

# Display the generated 2D model for verification
# Opens an interactive 2D viewer for inspecting the model
mesh.display_2d_view()

# Print model details such as volume, center of mass, and moment of inertia
# Useful for confirming the model's physical properties
mesh.description()

# Save the generated STL model to a file
# Replace 'output_model.stl' with the desired output file path
output_stl_path = "./output_model.stl"
mesh.save_to_file(output_stl_path)
