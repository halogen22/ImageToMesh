from .utils import *
import argparse
import cv2
import os

from .utils import STLGenerator


def main():
    """
    Main function to process input and output file paths.
    """
    parser = argparse.ArgumentParser(description="Process input and output paths.")
    parser.add_argument("--input_path", type=str, help="Path to the input file")
    parser.add_argument("--output_path", type=str, help="Path to the output file")
    parser.add_argument(
        "--pixel_width", type=float, default=1.0, help="Width of each pixel in the generated 3D model (default: 1.0)"
    )
    parser.add_argument(
        "--thickness", type=float, default=1.0, help="Thickness of the bottom plane in the STL model (default: 1.0)"
    )
    parser.add_argument(
        "--normalization_scale", type=float, default=255.0, 
        help="Scale factor for normalizing image pixel values (default: 255.0)"
    )
    args = parser.parse_args()

    input_path = args.input_path
    output_path = args.output_path
    pixel_width = args.pixel_width
    thickness = args.thickness
    normalization_scale = args.normalization_scale

    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist.")
        return

    # Read the input image
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {input_path}")
    print(f"Processing file '{input_path}'...")

    # Normalize the image using the user-defined scale
    normalized_image = (image / normalization_scale)

    # Generate the STL model using the normalized image and parameters
    stl_model = STLGenerator.generate_stl(normalized_image, pixel_width, thickness)

    try:
        # Save the STL model to the output path
        stl_model.save_as_stl(output_path)
        print(f"STL model successfully saved to '{output_path}'.")
    except Exception as e:
        print(f"Error processing files: {e}")
