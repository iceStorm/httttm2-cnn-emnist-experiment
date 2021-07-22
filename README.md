# EMNIST hand-written (digits, letters) dataset - CNN

# colab
Contains the jupyter notebooks that can be used to run on Google Colab or your Local machine (with Annaconda suggested).

> ### dataset
* Make sure to download the dataset from following links, then uncompress it to the **```colab/dataset```** folder (like the following image):
* Official site: ```https://www.nist.gov/itl/products-and-services/emnist-dataset```
* Download here (from the official site above): ```http://www.itl.nist.gov/iaui/vip/cs_links/EMNIST/gzip.zip```

![](https://github.com/iceStorm/httttm2-cnn-emnist-experiment/blob/master/colab/dataset/make_sure_to_download_these_files.png)

> ### in the every ```Mounting``` block in jupyter notebook files:
> ```Make sure to replace with your exactly path, instead of: /content/drive/MyDrive/HTTTTM-2/Final Term```

#
# the real images
> ### Refer to: ```https://github.com/adipro7/Handwritten-Captcha-Recognition```
> ![image](https://user-images.githubusercontent.com/57426442/126608088-20a0349a-2e2c-4289-86ea-7b8cd4177039.png)


# 
# experiment-src
Contains the CNN model deployment that integrates with Python Flask.

## Installing instructions: inside the ```experiment-src``` folder
#### ```python -m venv venv ```
#### ```venv/Scripts/activate```
#### ```pip list```
#### ```pip install -r requirements.txt```
#### ```python index.py```

#

> **Demo**
> 
> ![](https://github.com/iceStorm/httttm2-cnn-emnist-experiment/blob/master/flask.gif)
