from flask import Blueprint, render_template
from pixelate.forms.image_upload_form import ImageUploadForm
from pixelate.mosaic_filter.eyes_line_mosaic_filter import EyesLineMosaicFilter
from pixelate.mosaic_filter.gauss_blur_mosaic_filter import \
    GaussBlurMosaicFilter
from pixelate.mosaic_filter.pixel_blur_mosaic_filter import \
    PixelBlurMosaicFilter

bp = Blueprint("index", __name__)


@bp.route('/')
def index():
    # create form
    form = ImageUploadForm(meta={'csrf': False})
    filters_list = [
        EyesLineMosaicFilter.name,
        GaussBlurMosaicFilter.name,
        PixelBlurMosaicFilter.name,
    ]

    # return HTML page
    return render_template(
        "index.html",
        form=form,
        filters_list=filters_list,
    )
