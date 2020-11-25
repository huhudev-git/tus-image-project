
from pixelate.mosaic_style.abstract_mosaic_style import AbstructMosaicStyle


class EyesLineMosaicStyle(AbstructMosaicStyle):
    """目に黒い線をひくモザイクパターンのスタイルパラメータ
    """

    @classmethod
    def from_json(cls, json_data) -> "EyesLineMosaicStyle":
        return cls
