import io
from flask import send_file, Blueprint
import json


from pixelate.forms.image_upload_form import ImageUploadForm
from pixelate.models.image import Image
from pixelate.models.mosaic import Mosaic
from pixelate.face_detect import face_detect, eye_detect

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
        try:
            mosaic_style = json.loads(mosaic_style)
        except json.decoder.JSONDecodeError:
            return b""
        mosaic = Mosaic(mosaic_pattern, mosaic_style)

        # find face pos
        if mosaic_pattern == "eyes":
            positions = eye_detect(image)
        else:
            positions = face_detect(image)

        # embedded mosaic
        processed_image = mosaic.filter_interface(image, positions)

        return send_file(
            processed_image,
            mimetype='image/jpeg',
        )
    return b""
