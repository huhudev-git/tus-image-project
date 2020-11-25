from typing import List

from pixelate.models.image import Image
from pixelate.models.position import Position
from pixelate.mosaic_filter.blur_mosaic_filter import BlurMosaicFilter
from pixelate.mosaic_style.abstract_mosaic_style import AbstructMosaicStyle


class PixelBlurMosaicFilter(BlurMosaicFilter):
    """
    モザイクパターン - ピクセル
    """

    name = "pixel_blur"

    def process(self, image: Image, style: AbstructMosaicStyle, positions: List[Position]) -> bytes:
        '''写真を処理する
        '''
        data = image.data
        return data
