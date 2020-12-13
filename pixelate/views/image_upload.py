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
            mosaic = Mosaic(mosaic_pattern, mosaic_style)
        except json.decoder.JSONDecodeError:
            return b""
        except ValueError:
            return b""

        # find face pos
        if mosaic_pattern == "eyes":
            detect = eye_detect
        else:
            detect = face_detect
        positions = detect(image)

        # embedded mosaic
        processed_image = mosaic.filter_interface(image, positions)

        return send_file(
            processed_image,
            mimetype='image/jpeg',
        )
    return b""
