import image
import encryption


def hide_data(data, data_length, total_pixels, pixel_array, img_height, img_width, cover_image, output_name):
    i = 0

    # Modify pixel array
    for pixel in range(total_pixels):
        for rgb in range(0, 3):
            if i < data_length:
                pixel_array[pixel][rgb] = int(bin(pixel_array[pixel][rgb])[2:9] + data[i], 2)
                i += 1

    image.create_new_image(pixel_array, img_height, img_width, cover_image, output_name)


def extract_data(total_pixels, pixel_array, output_name):
    # Extract LSB from each pixel array first
    extracted_lsb = ""

    for pixel in range(total_pixels):
        for rgb in range(0, 3):
            extracted_lsb += (bin(pixel_array[pixel][rgb])[2:][-1])

    extracted_lsb = [extracted_lsb[i:i+8] for i in range(0, len(extracted_lsb), 8)]

    # Reassemble data
    eof_marker = "$EOF"
    raw_output = ""

    for i in range(len(extracted_lsb)):
        if raw_output[-4:] == eof_marker:
            break
        else:
            raw_output += chr(int(extracted_lsb[i], 2))

    # Trim EOF marker and write to file
    trimmed = raw_output[:-4]

    with open(output_name, "w") as file:
        file.write(trimmed)

    # Decrypt data and write to file
    encryption.decrypt(trimmed)
