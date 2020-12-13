
import io
from typing import List

import cv2
import numpy as np
from pixelate.models.image import Image
from pixelate.models.position import Position
from pixelate.mosaic_filter.blur_mosaic_filter import BlurMosaicFilter
from pixelate.mosaic_style.abstract_mosaic_style import AbstructMosaicStyle
from pixelate.face_detect.main import face_detect


class GaussBlurMosaicFilter(BlurMosaicFilter):
    """
    モザイクパターン - ガウス
    """

    name = "gauss_blur"

    def process(self, image: Image, style: AbstructMosaicStyle, positions: List[Position]) -> io.BytesIO:
        '''写真を処理する
        '''
        image_stream = image.get_from_io()
        file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # Yamagishi Kanata | below
        for position in positions:
            h, w, c = img[
                position.startX:position.endX,
                position.startY:position.endY,
            ].shape

            target = cv2.resize(img[
                position.startX:position.endX,
                position.startY:position.endY],
                (int(w*100/h), 100)
            )

            for _ in range(1, style.level):
                target = cv2.GaussianBlur(target, (5, 5), 10)

            img[
                position.startX: position.endX,
                position.startY:position.endY,
            ] = cv2.resize(target, (w, h))

        is_success, buffer = cv2.imencode(".jpg", img)
        if is_success:
            io_buf = io.BytesIO(buffer)
        else:
            io_buf = io.BytesIO()
        return io_buf
