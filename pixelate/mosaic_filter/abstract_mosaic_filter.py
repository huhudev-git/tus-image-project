import abc
from typing import List

from pixelate.models.image import Image
from pixelate.models.position import Position
from pixelate.mosaic_style.abstract_mosaic_style import AbstructMosaicStyle


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
