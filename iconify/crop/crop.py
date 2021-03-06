from PIL import Image


def scale(square_side):
    division = square_side // 10
    counter = 0
    while division:
        division = division // 10
        counter += 1
    return 10**(counter - 1)


def crop(image_name):
    image = Image.open(image_name)
    width = image.width
    height = image.height
    square_side = min(width, height)
    scaled_step = scale(square_side)
    scaling = 0
    print(scaling, scaled_step, square_side, max(width, height))
    while scaling * scaled_step + square_side < max(width, height):
        if square_side == width:
            squared_image = image.crop((0, scaling * scaled_step,
                                        square_side, square_side + scaling * scaled_step))
            resized_squared_image = squared_image.resize((150, 150))
            resized_squared_image.save(f"test_{scaling}.jpg")
            scaling += 1
        elif square_side == height:
            squared_image = image.crop((scaling * scaled_step, 0,
                                        square_side + scaling * scaled_step, square_side))
            resized_squared_image = squared_image.resize((150, 150))
            resized_squared_image.save(f"test_{scaling}.jpg")
            scaling += 1
