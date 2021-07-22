from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, HiddenField

from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    # image = FileField(
    #     label='Pick a security image',
    #     validators=[
    #         FileAllowed(message='Only .gif files accepted', upload_set=['.']),
    #         DataRequired(message='Please pick an security image')
    #     ]
    # )
    pass
