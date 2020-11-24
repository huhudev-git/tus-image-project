from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    ValidationError,
)
from wtforms.validators import DataRequired
from flask_wtf.file import (
    FileField,
    FileRequired,
)


class ImageUploadForm(FlaskForm):
    image = FileField("image", validators=[FileRequired()])
    mosaic = StringField("mosaic", validators=[DataRequired()])

    def validate_image(self, image):
        pass

    def validate_mosaic(self, mosaic):
        if mosaic.data == "":
            raise ValidationError("Invaild")

        if len(mosaic.data) > 100:
            raise ValidationError("Invaild")
