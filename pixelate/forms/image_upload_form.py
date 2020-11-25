from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class ImageUploadForm(FlaskForm):
    image = FileField("image", validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!'),
    ])
    mosaic_pattern = StringField("mosaic-pattern", validators=[
        DataRequired(),
        Length(min=1, max=100),
    ])
    mosaic_style = StringField("mosaic-style", validators=[
        DataRequired(),
        Length(min=1, max=100),
    ])
