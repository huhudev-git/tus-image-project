import json

from flask import escape, render_template, request

from app.forms.image_upload_form import ImageUploadForm
from app.models.image import Image
from app.models.mosaic import Mosaic
from app import app


@app.route('/upload-image', methods=['POST'])
def handle_upload_image():
    form = ImageUploadForm()
    if form.validate_on_submit():
        # get image params
        image_data = form.image.data
        image = Image(image_data)

        # get mosaic type params
        mosaic_json = form.mosaic.data
        mosaic_dict = json.loads(mosaic_json)
        mosaic = Mosaic(**mosaic_dict)

        # find face pos

        # embedded mosaic

        # return
    pass


@app.route('/')
def index():
    # create form
    form = ImageUploadForm()

    # return HTML page
    return render_template(
        "index.html",
        form=form,
    )
