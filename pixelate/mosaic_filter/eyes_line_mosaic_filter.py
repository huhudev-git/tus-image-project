from typing import List

from pixelate.models.image import Image
from pixelate.models.position import Position
from pixelate.mosaic_filter.abstract_mosaic_filter import AbstractMosaicFilter
from pixelate.mosaic_style.abstract_mosaic_style import AbstructMosaicStyle


class EyesLineMosaicFilter(AbstractMosaicFilter):
    """
    目に黒い線をひく
    """

    name = "eyes"

    def process(self, image: Image, style: AbstructMosaicStyle, positions: List[Position]) -> bytes:
        '''写真を処理する
        '''
        data = image.data
        return data
