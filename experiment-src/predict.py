from keras.models import load_model, model_from_json
import imutils
import cv2
import numpy as np

# loading the CNN model
json_file = open('model.json', mode='r')
json_content = json_file.read()
json_file.close()

the_model = model_from_json(json_content)
the_model.load_weights('model.h5')

CHARACTERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
              'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
              'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def get_character(class_index):
    return CHARACTERS[class_index]


def get_highlighted_image(grayed_image):
    # highlighting the letter contours
    thresh = cv2.threshold(grayed_image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    contour_coordinates = []
    for contour in contours:
        contour_coordinates.append(cv2.boundingRect(contour))

    # sorting the contours array to ensure the numbers is from left-to-right (keeping the original order)
    contour_coordinates = sorted(contour_coordinates, key=lambda tupl: tupl[0])

    return thresh, contour_coordinates


def scale(img):
    return cv2.resize(img, (20, 20), interpolation=cv2.INTER_AREA)


def image_resize(img):
    img = scale(img)

    IMG_COL = 28
    IMG_ROW = 28

    top = int((IMG_ROW - img.shape[0]) / 2)
    bottom = IMG_ROW - img.shape[0] - top

    left = int((IMG_COL - img.shape[1]) / 2)
    right = IMG_COL - img.shape[1] - left

    padded = cv2.copyMakeBorder(img.copy(), top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    return padded


def predict(highlighted_img, contour_coordinates, verbose=False) -> str:
    result = list()

    for i, ctr in enumerate(contour_coordinates):
        # Get bounding box
        x, y, w, h = ctr

        # Getting letter from the image by coordinates
        letter_img = highlighted_img[y:y + h, x - 1:x + w + 1]

        # resizing to 28×28
        letter_img = image_resize(letter_img)

        # converting the image to numpy array
        t = np.copy(np.array(letter_img))
        t = t / 255.0
        t = t.reshape(1, 784)

        # predicting
        pred = the_model.predict_classes(t)
        character = get_character(pred[0])

        result.append(character)

    return ''.join(list(map(lambda arr: arr[0], result)))


# main function
def get(img_name) -> str:
    from skimage.io import imread

    image = imread(f'static/{img_name}')
    grayed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return predict(*get_highlighted_image(grayed), verbose=True)
