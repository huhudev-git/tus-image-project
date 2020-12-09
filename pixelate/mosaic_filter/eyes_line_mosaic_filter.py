import io
from typing import List

import cv2
import numpy as np
from pixelate.models.image import Image
from pixelate.models.position import Position
from pixelate.mosaic_filter.abstract_mosaic_filter import AbstractMosaicFilter
from pixelate.mosaic_style.abstract_mosaic_style import AbstructMosaicStyle


class EyesLineMosaicFilter(AbstractMosaicFilter):
    """
    目に黒い線をひく
    """

    name = "eyes"

    def process(self, image: Image, style: AbstructMosaicStyle, positions: List[Position]) -> io.BytesIO:
        '''写真を処理する
        '''
        image_stream = image.get_from_io()
        file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        length = len(positions)
        if length >= 2:
            for i in range(length // 2):
                i = i * 2
                X1 = (positions[i].startX * 2 + positions[i].endX) // 2
                Y1 = int((positions[i].startY * 2 + positions[i].endY * 1.7) // 2)
                X2 = (positions[i+1].startX * 2 + positions[i+1].endX) // 2
                Y2 = int((positions[i+1].startY * 2 + positions[i+1].endY * 1.7) // 2)

                Y = (Y1 + Y2) // 2
                Y1 = Y - style.line
                Y2 = Y + style.line

                cv2.rectangle(
                    img,
                    (X1, Y1),
                    (X2, Y2),
                    (0, 0, 0),
                    -1,
                )

        is_success, buffer = cv2.imencode(".jpg", img)
        if is_success:
            io_buf = io.BytesIO(buffer)
        else:
            io_buf = io.BytesIO()
        return io_buf
