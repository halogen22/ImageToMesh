STL Generator
=============

This script is a tool for generating 3D models (e.g., STL files) based on input images. 
It calculates heights based on pixel brightness values and creates files for 3D models.

---

Features
--------

- Converts any grayscale image into a 3D model.
- Allows specifying pixel width (`pixel_width`), base thickness (`thickness`), and normalization range as arguments.

---

Requirements
------------

- Python 3.10 or higher
- `trimesh>=4.5.3`
- `pillow>=11.0.0`
- `opencv-python>=4.10.0.84`
- `matplotlib>=3.10.0`
- `numpy>=2.2.1`
- `pyglet<2`

---

Installation
------------

.. code-block:: bash

   pip install image-to-mesh

---

Usage
-----

Example Usage in a Script
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import cv2
   from image_to_mesh import MeshGenerator

   # Define the image path and parameters
   image_path = "./sample_img/4.1.04.tiff"  # Path to the input grayscale image
   pixel_width = 1  # Width of each pixel in the generated 3D model
   thickness = 1  # Thickness of the bottom plane in the STL model

   # Load the image
   image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

   # Create the mesh
   mesh = MeshGenerator.generate_mesh((image / 255), pixel_width, thickness)

   # Display the mesh in 3D
   mesh.display_3d_view()

   # Display the mesh in 2D
   mesh.display_2d_view()

   # Save the mesh as an STL file
   mesh.save_to_file("output_model.stl")

Execution Command
~~~~~~~~~~~~~~~~~

Run the script with the following format:

.. code-block:: bash

   python -m image_to_mesh --input_path <input_path> --output_path <output_path> --pixel_width <value> --thickness <value> --normalize_range <value>

Argument Description
~~~~~~~~~~~~~~~~~~~~

+-------------------+----------+---------------------------------------------------------------+
| Argument          | Required | Description                                                   |
+===================+==========+===============================================================+
| ``--input_path``  | Yes      | File path of the input image                                  |
+-------------------+----------+---------------------------------------------------------------+
| ``--output_path`` | Yes      | Path to save the output 3D file                               |
+-------------------+----------+---------------------------------------------------------------+
| ``--pixel_width`` | Optional | Width of each pixel (default: 1.0)                            |
+-------------------+----------+---------------------------------------------------------------+
| ``--thickness``   | Optional | Thickness of the base (default: 1.0)                          |
+-------------------+----------+---------------------------------------------------------------+
| ``--normalize_range`` | Optional | Range for normalizing pixel values (default: 255)              |
+-------------------+----------+---------------------------------------------------------------+

Execution Example
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   python -m image_to_mesh --input_path ./sample_img/input_image.tiff ./ --output_path output_model.stl --pixel_width 2.0 --thickness 0.5 --normalize_range 255

This command generates a 3D model based on ``input_image.tiff`` in the ``sample_img`` directory and saves it as ``output_model.stl``.

---

Output
------

- The output file is saved in STL format at the specified path.
- The file represents a 3D model based on pixel brightness values.

---

Notes
-----

- The input image must be a grayscale image.
- Errors will occur if the input file does not exist or is in an incorrect format.

---
Sample Image
-----

`SIPI Image Database - Misc <https://sipi.usc.edu/database/database.php?volume=misc&image=1#top>`

---

Support
-------

Report bugs or issues on the `Issues <https://github.com/halogen22/ImageToMesh/issues>`_ page.

---

License
-------

This project is licensed under the `MIT License <./LICENSE>`_. See the LICENSE file for more details.
