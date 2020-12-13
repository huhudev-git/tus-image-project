
from pixelate.mosaic_style.abstract_mosaic_style import AbstructMosaicStyle


class EyesLineMosaicStyle(AbstructMosaicStyle):
    """目に黒い線をひくモザイクパターンのスタイルパラメータ
    """

    line = 0

    def __init__(self, line) -> None:
        self.line = int(line)

    @classmethod
    def from_json(cls, json_data) -> "EyesLineMosaicStyle":
        return cls(json_data['line'])
