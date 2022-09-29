from ctypes import resize
import PIL.Image
import os


ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def grayify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters


def main(new_width=500):
    try:
        image = PIL.Image.open(r'fundamentals\oop\1622739538__ninjas_vs_pirates\ninjas_vs_pirates\circle.png')
    except:
        print(f"'battle_art.jpg' is not a valid pathname to an image.")
    
    else:
        new_image_data = pixels_to_ascii(grayify(resize_image(image)))
        pixel_count = len(new_image_data)
        ascii_image = "\n".join(
        new_image_data[i:(i+new_width)] for i in range(0, pixel_count))
        print(ascii_image)

        with open(r"fundamentals\oop\1622739538__ninjas_vs_pirates\ninjas_vs_pirates\ascii_image.txt", "w") as f:
            f.write(ascii_image)



main()
