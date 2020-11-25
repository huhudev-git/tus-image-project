import io
from flask import send_file, Blueprint


from pixelate.forms.image_upload_form import ImageUploadForm
from pixelate.models.image import Image
from pixelate.models.mosaic import Mosaic
from pixelate.face_detect import face_detect

bp = Blueprint("image_upload", __name__)


@bp.route('/upload-image', methods=['POST'])
def handle_upload_image():
    form = ImageUploadForm(meta={'csrf': False})
    if form.validate_on_submit():
        # get image params
        image_data = form.image.data.read()
        image = Image(image_data)

        # get mosaic type params
        mosaic_pattern = form.mosaic_pattern.data
        mosaic_style = form.mosaic_style.data
        mosaic = Mosaic(mosaic_pattern, mosaic_style)

        # find face pos
        positions = face_detect(image)

        # embedded mosaic
        processed_image = mosaic.filter_interface(image, positions)

        return send_file(
            io.BytesIO(processed_image),
            mimetype='image/jpeg',
            as_attachment=True,
            attachment_filename='download.jpg',
        )
    return b""
