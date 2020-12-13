from pixelate.mosaic_style.abstract_mosaic_style import AbstructMosaicStyle


class PixelBlurMosaicStyle(AbstructMosaicStyle):
    """ピクセルモザイクパターンのスタイルパラメータ
    """

    level = None

    def __init__(self, level) -> None:
        self.level = int(level)

    @classmethod
    def from_json(cls, json_data) -> "PixelBlurMosaicStyle":
        return cls(json_data['level'])
