import abc


class AbstructMosaicStyle(abc.ABC):
    """モザイクパターンのスタイルパラメータ
    """

    @abc.abstractclassmethod
    def from_json(cls, json_data):
        return cls()
