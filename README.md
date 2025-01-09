作成中。。。
# Mesh Generator

このスクリプトは、入力画像をもとに3Dモデル（STLファイルなど）を生成するツールです。ピクセルの輝度値に基づいて高さを計算し、3Dモデル用のファイルを作成します。

---

## 特徴

- 任意のグレースケール画像を3Dモデルに変換可能
- ピクセルの幅（`pixel_width`）、底面の厚さ（`thickness`）、正規化の範囲を引数として指定可能

---

## 必要条件

- Python3.10以上
- trimesh>=4.5.3
- pillow>=11.0.0
- opencv-python>=4.10.0.84
- matplotlib>=3.10.0
- numpy>=2.2.1
- pyglet<2

---
## インストール方法
```
pip install image-to-mesh
```

---

## 使用方法
### スクリプトの利用例
```python
import cv2
from image_to_mesh import MeshGenerator

# Define the image path and parameters
image_path = "./sample_img/4.1.04.tiff"  # Path to the input grayscale image
pixel_width = 1  # Width of each pixel in the generated 3D model
thickness = 1  # Thickness of the bottom plane in the STL model

# 画像を読み込み
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# meshの作成
mesh = MeshGenerator.generate_mesh((image / 255), pixel_width, thickness)

# meshの表示
mesh.display_3d_view()

# meshを2Dで表示
mesh.display_2d_view()

# STLファイルとして保存
mesh.save_to_file("output_model.stl")
```

### 実行コマンド

以下の形式でスクリプトを実行してください：

```bash
python -m image_to_mesh --input_path <input_path> --output_path <output_path> --pixel_width <value> --thickness <value> --normalize_range <value>
```

### 引数の説明

| 引数              | 必須 | 説明                                                                 |
|-------------------|------|----------------------------------------------------------------------|
| `--input_path`    | 必須 | 入力画像のファイルパス                                              |
| `--output_path`   | 必須 | 出力する3Dファイルのパス                                           |
| `--pixel_width`   | 任意 | 各ピクセルの幅（デフォルト: 1.0）                                   |
| `--thickness`     | 任意 | 底面の厚さ（デフォルト: 1.0）                                       |
| `--normalize_range` | 任意 | ピクセル値を正規化する範囲（デフォルト: 255）                       |

### 実行例

以下は実行コマンドの例です：

```bash
python -m image_to_mesh --input_path ./sample_img/input_image.tiff ./ --output_path output_model.stl --pixel_width 2.0 --thickness 0.5 --normalize_range 255
```

このコマンドは、`sample_img` ディレクトリ内の `input_image.tiff` を元に3Dモデルを生成し、`output_model.stl` に出力します。

---

## 出力結果

- 出力ファイルは、指定されたパスにSTL形式で保存されます。
- ファイルはピクセル輝度値に応じた3Dモデルを表現します。

---

## サンプル画像
[SIPI Image Database - Misc](https://sipi.usc.edu/database/database.php?volume=misc&image=1#top)

---

## 注意事項

- 入力画像はグレースケール画像である必要があります。
- 入力ファイルが存在しない場合や正しい形式でない場合、エラーが発生します。

---

## サポート

バグ等は[Issues](https://github.com/halogen22/ImageToMesh/issues)で報告してください

---

## ライセンス

このプロジェクトは [MITライセンス](./LICENSE) のもとで公開されています。詳細についてはLICENSEファイルをご確認ください。

---
