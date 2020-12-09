import io


class Image():

    def __init__(self, image_data: bytes):
        self.data = image_data

    def get_from_io(self) -> io.BytesIO:
        image_stream = io.BytesIO()
        image_stream.write(self.data)
        image_stream.seek(0)
        return image_stream
