#!/usr/bin/python


import image


def main():
    img = image.get_image("new.png")
    img_pixels = image.get_image_pixels(img)
    print(img_pixels)


if __name__ == "__main__":
    main()
