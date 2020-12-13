from typing import Dict, List

from pixelate.models.image import Image
from pixelate.models.position import Position
from pixelate.mosaic_filter.abstract_mosaic_filter import AbstractMosaicFilter
from pixelate.mosaic_filter.eyes_line_mosaic_filter import EyesLineMosaicFilter
from pixelate.mosaic_filter.gauss_blur_mosaic_filter import \
    GaussBlurMosaicFilter
from pixelate.mosaic_filter.pixel_blur_mosaic_filter import \
    PixelBlurMosaicFilter
from pixelate.mosaic_style.abstract_mosaic_style import AbstructMosaicStyle
from pixelate.mosaic_style.eyes_line_mosaic_style import EyesLineMosaicStyle
from pixelate.mosaic_style.gauss_blur_mosaic_style import GaussBlurMosaicStyle
from pixelate.mosaic_style.pixel_blur_mosaic_style import PixelBlurMosaicStyle


class Mosaic():

    _filters = {
        EyesLineMosaicFilter.name: EyesLineMosaicFilter,
        GaussBlurMosaicFilter.name: GaussBlurMosaicFilter,
        PixelBlurMosaicFilter.name: PixelBlurMosaicFilter,
    }

    _styles = {
        EyesLineMosaicFilter.name: EyesLineMosaicStyle,
        GaussBlurMosaicFilter.name: GaussBlurMosaicStyle,
        PixelBlurMosaicFilter.name: PixelBlurMosaicStyle,
    }

    def __init__(self, pattern: str, style_data: Dict):
        self.pattern = pattern

        self._filter = self.get_filter()
        self._style = self.get_style(style_data)

    def get_filter(self) -> AbstractMosaicFilter:
        filter_ = self._filters.get(self.pattern, None)
        if filter_ is None:
            return GaussBlurMosaicFilter()
        return filter_()

    def get_style(self, style_data: Dict) -> AbstructMosaicStyle:
        style = self._styles.get(self.pattern, None)
        if style is None:
            return GaussBlurMosaicStyle.from_json({"level": 1})
        return style.from_json(style_data)

    def filter_interface(self, image: Image, positions: List[Position]) -> bytes:
        return self._filter.process(image, self._style, positions)
