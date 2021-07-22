from urllib.request import urlretrieve
import requests as requests

import numpy as np
from skimage.io import imread, imsave

# ignoring SSL
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

HOST_URL = 'https://sinhvien.bvu.edu.vn'
REQUEST_URL = HOST_URL + '/ajaxpro/AjaxConfirmImage,PMT.Web.PhongDaoTao.ashx'


def retrieve_image_url(confirm_image_data):
    image_url = confirm_image_data.split(',')[0]
    image_url = image_url.split('"')[1]

    return HOST_URL + image_url


def get_confirm_image_url():
    response = requests.post(REQUEST_URL, verify=False, headers={
        'X-AjaxPro-Method': 'CreateConfirmImage',
    })

    return retrieve_image_url(response.text)


def get_image():
    # getting confirm image url
    confirm_image_url = get_confirm_image_url()
    print('\n\n', confirm_image_url)

    # showing image from the url
    image = imread(confirm_image_url)

    # saving the image into folder
    image_name = 'static/1.gif'
    print('path:', image_name)

    imsave(fname=image_name, arr=np.asarray(image))
