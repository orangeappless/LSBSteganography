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


def get_num_pixels(pixel_array, image_type):
    if image_type == "RGBA":
        num_pixels = pixel_array.size//4
    elif image_type == "RGB":
        num_pixels = pixel_array.size//3

    return num_pixels


def create_new_image(pixel_array, height, width, image, image_name):
    dim = 0

    if image.mode == "RGBA":
        dim = 4
    elif image.mode == "RGB":
        dim = 3

    img_pixels = pixel_array.reshape(height, width, dim)
    new_img = Image.fromarray(img_pixels.astype("uint8"), image.mode)

    new_img.save(image_name)
