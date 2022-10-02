#!/usr/bin/python


import argparse
import sys

import image
import utils
import encryption


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-m",
                        "--mode",
                        type=str,
                        help="program mode, either 'hide' or 'extract'",
                        required=True)

    parser.add_argument("-s",
                        "--source",
                        type=str,
                        help="name of source PNG image",
                        required=True)

    parser.add_argument("-d",
                        "--data", 
                        type=str, 
                        help="(HIDE mode only) file containing data, to be concealed",
                        required=False)

    parser.add_argument("-o",
                        "--output", 
                        type=str,
                        help="name of output PNG image, containing the concealed data",
                        required=True)

    args = parser.parse_args()

    return args


def hide(cover_image_source, data_source, output_name):
    # Get image stats
    img = image.get_image(cover_image_source)
    img_width, img_height = image.get_image_dimensions(img)
    cover_img_pixels = image.get_image_pixels(img)
    total_pixels = image.get_num_pixels(cover_img_pixels)

    # Get user input
    file_input = data_source

    with open(file_input, "rb") as file:
        data = file.read()

    # Add filename to data
    data += ("$SOURCENAME" + file_input).encode('utf-8')

    # Encrypt data
    data = encryption.encrypt(data)

    # Add EOF marker to data
    eof_marker = b"$EOF"
    data += eof_marker

    # Convert to binary representation
    bin_data = ''.join([format(i, "08b") for i in data])
    data_length = len(bin_data)
    
    print("Data length: ", data_length)
    print("Total pixels:", total_pixels)

    if data_length > total_pixels:
        print("Need a larger image")
        sys.exit()
    else:
        utils.hide_data(bin_data, data_length, total_pixels, cover_img_pixels, img_height, img_width, img, output_name)


def extract(image_source, output_name):
    # Get image stats
    img = image.get_image(image_source)
    image_pixels = image.get_image_pixels(img)
    total_pixels = image.get_num_pixels(image_pixels)

    utils.extract_data(total_pixels, image_pixels, output_name)


def main():
    parse_args()
    args = parse_args()

    if args.mode.lower() == "hide":
        cover_img_input = args.source
        input_data = args.data
        output_img_name = args.output
        hide(cover_img_input, input_data, output_img_name)

    elif args.mode.lower() == "extract":
        source_img = args.source
        output_img_name = args.output
        extract(source_img, output_img_name)

    else:
        print("Invalid option")
        sys.exit()


if __name__ == "__main__":
    main()
