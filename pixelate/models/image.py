import io


class Image():

    def __init__(self, image_data: bytes):
        self.data = image_data

    def get_from_io(self) -> io.BytesIO:
        image_stream = io.BytesIO(self.data)
        return image_stream
