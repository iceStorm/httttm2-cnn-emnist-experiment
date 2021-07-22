import os

from flask import Flask, render_template, flash, request

from form import UploadForm
from predict import get
from service import get_image

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HTTTTM-2'


@app.route('/', methods=['GET'])
def index():
    form = UploadForm()

    images = os.listdir('static/images')
    images = list(map(lambda name: f'images/{name}', images))
    return render_template('index.html', form=form, images=images)


@app.route('/predict', methods=['POST'])
def predict():

    print('\n\nPredicting..')
    result = get(request.form['image_id'])
    print('\nPredicted:', result)

    return result


if __name__ == '__main__':
    app.run(debug=True)
