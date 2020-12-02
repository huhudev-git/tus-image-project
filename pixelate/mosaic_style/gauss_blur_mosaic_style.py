from pixelate.mosaic_style.abstract_mosaic_style import AbstructMosaicStyle


class GaussBlurMosaicStyle(AbstructMosaicStyle):
    """ガウスモザイクパターンのスタイルパラメータ
    """

    level = None

    def __init__(self, level) -> None:
        self.level = level
    
    @classmethod
    def from_json(cls, json_data) -> "GaussBlurMosaicStyle":
        return cls(json_data['level'])
