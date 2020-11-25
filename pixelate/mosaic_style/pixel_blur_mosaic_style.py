from pixelate.mosaic_style.abstract_mosaic_style import AbstructMosaicStyle


class PixelBlurMosaicStyle(AbstructMosaicStyle):
    """ピクセルモザイクパターンのスタイルパラメータ
    """

    @classmethod
    def from_json(cls, json_data) -> "PixelBlurMosaicStyle":
        return cls()
