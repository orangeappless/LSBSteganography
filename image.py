from PIL import Image
import numpy as np


def get_image(image):
    img = Image.open(image, "r")

    return img


def get_image_dimensions(image):
    return image.size


def get_image_pixels(image):
    pixel_data = image.getdata()
    pixel_array = np.array(pixel_data)

    return pixel_array


def get_num_pixels(pixel_array):
    num_pixels = pixel_array.size//3

    return num_pixels


def create_new_image(pixel_array, height, width, image, image_name):
    img_pixels = pixel_array.reshape(height, width, 3)
    new_img = Image.fromarray(img_pixels.astype("uint8"), image.mode)

    new_img.save(image_name)
