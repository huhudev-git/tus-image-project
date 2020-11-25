# 要件定義

## 目的

写真をアップロードし、顔認識して、顔の部分を自動的にモザイクにしてもらうウェブアプリケーション

## Framework

- [Python 3.8.6](https://www.python.org/downloads/release/python-386/)
- [Flask](https://flask.palletsprojects.com/)
- OpenCV

<center>
<img src="README/web-application-architecture.png" width=400px>
</center>

今回データベースレイヤーがない、プレゼンテーションレイヤーとビジネスレイヤーしかない。大筋はリクエストをPython関数に渡し、Python関数の中に処理する、処理した結果を返す。

## Usage

```sh
# clone the repository
git clone https://github.com/huhudev-git/tus-image-project
cd tus-image-project

# create virtual environment
python -m venv venv

# linux
source venv/bin/activate
# win
source venv/Scripts/activate

# install denpandencies
pip install -r requirements.txt
```

実行する

```sh
# linux
export FLASK_APP=pixelate
# windows
set FLASK_APP=pixelate

flask run
```

## Path

### `/`

- Method: GET
- Params: None
- Content-Type: text/html
- Return: html(ウェブページ)

詳細

- アップロード
- モザイクのスタイルの選択
- モザイクのパターンの選択
- preview機能

### `/upload-image`

- Method: POST
- Params: 以下参照
- Content-Type: multipart/form-data
- Return: bytes(processed image)

処理流れ

- 写真を取得する
  - データサイズ制限
  - サイズ制限
- モザイクのパラメータを取得する
- 画像に顔認識する
- モザイクのパラメータによって写真を処理する
- 処理した写真を返す

#### リクエスト

| name         | type   | description                    |
| :----------- | :----- | :----------------------------- |
| mosaic_type  | string | リクエストのモザイクのパターン |
| mosaic_style | string | リクエストのモザイクのスタイル |
| image        | blob   | 画像の内容                     |

#### レスポンス

| name  | type | description |
| :---- | :--- | :---------- |
| image | blob | 画像の内容  |

#### 参考

> [Blob](https://developer.mozilla.org/ja/docs/Web/API/Blob)

## 画面仕様

|               `/`               |        `/`(after upload)        |               全体               |
| :-----------------------------: | :-----------------------------: | :------------------------------: |
| ![-](README/mosaicface1-01.png) | ![-](README/mosaicface1-02.png) | ![-](README/enl_fz0uyaaaic2.jpg) |

## 機能

### 顔認識

- OpenCV
  - Haar cascades
  - HOG + Linear SVM
  - Deep learning-based face detectors.

返すもの `List[Position]`

- Position
  - The starting x-coordinate of the face bounding box
  - The ending x-coordinate of the face
  - The starting y-coordinate of the face location
  - The ending y-coordinate of the face

> - [Blur and anonymize faces with OpenCV and Python](https://www.pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/)
> - [Face detection with OpenCV and deep learning](https://www.pyimagesearch.com/2020/04/06/blur-and-anonymize-faces-with-opencv-and-python/)

`pixelate/face_detect/main.py`

```py
def face_detect(image: bytes) -> List[Position]:
    pass
```

### モザイクをつける

一つのスタイル/パターンで、一つのクラスで実装する

- 目に黒い線をひく
- モザイクパターン
  - ガウス
  - ピクセル
- 使うもの
  - OpenCV

#### クラスデザイン

![-](README/filter-class.svg)

```py
class AbstractMosaicFilter(abc.ABC):

    # フロントエンドのほうのモザイクパターンの名前
    name = None

    @abc.abstractmethod
    def process(self, image: Image, style: AbstructMosaicStyle, positions: List[Position]) -> bytes:
        '''写真を処理し、モザイクをつけた写真を返す

        Args:
            image (bytes): アップロードした写真
            style (Any): モザイクのスタイル
            positions (List[Position]): 顔認識の位置

        Returns:
            bytes: モザイクをつけた写真
        '''
        pass

class EyesLineMosaicFilter(AbstractMosaicFilter):
  """
  目に黒い線をひく
  """
  pass

class BlurMosaicFilter(AbstractMosaicFilter):
  pass

class GaussBlurMosaicFilter(BlurMosaicFilter):
  """
  モザイクパターン - ガウス
  """
  pass

class PixelBlurMosaicFilter(BlurMosaicFilter):
  """
  モザイクパターン - ピクセル
  """
  pass
```
