from pixelate.mosaic_style.abstract_mosaic_style import AbstructMosaicStyle


class GaussBlurMosaicStyle(AbstructMosaicStyle):
    """ガウスモザイクパターンのスタイルパラメータ
    """
    
    @classmethod
    def from_json(cls, json_data) -> "GaussBlurMosaicStyle":
        return cls()
