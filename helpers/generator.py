from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFilter
from os import listdir
from os.path import join
import random


def generate_plate_number():
    """
    Function generates polish style driving plate number
    """
    letters = 'ABCDEFGHIJKLMNOUPRSTUVWXYZ'
    digits = '0123456789'
    patterns = [" {}{} {}{}{}{}{}".format(random.choice(letters), 
                                          random.choice(letters),
                                          random.choice(digits),
                                          random.choice(digits),
                                          random.choice(digits),
                                          random.choice(digits),
                                          random.choice(digits)), 
                " {}{} {}{}{}{}{}".format(random.choice(letters), 
                                          random.choice(letters),
                                          random.choice(digits),
                                          random.choice(digits),
                                          random.choice(digits),
                                          random.choice(digits),
                                          random.choice(letters)),
                " {}{} {}{}{}{}{}".format(random.choice(letters), 
                                          random.choice(letters),
                                          random.choice(digits),
                                          random.choice(digits),
                                          random.choice(digits),
                                          random.choice(letters),
                                          random.choice(letters)),
                " {}{} {}{}{}{}{}".format(random.choice(letters), 
                                          random.choice(letters),
                                          random.choice(digits),
                                          random.choice(letters),
                                          random.choice(digits),
                                          random.choice(digits),
                                          random.choice(digits)),
                " {}{} {}{}{}{}{}".format(random.choice(letters),
                                          random.choice(letters),
                                          random.choice(digits),
                                          random.choice(letters),
                                          random.choice(letters),
                                          random.choice(digits),
                                          random.choice(digits)),
                " {}{}{} {}{}{}{}".format(random.choice(letters),
                                          random.choice(letters),
                                          random.choice(letters),
                                          random.choice(letters),
                                          random.choice(digits),
                                          random.choice(digits),
                                          random.choice(digits)),
                " {}{}{} {}{}{}{}".format(random.choice(letters),
                                          random.choice(letters),
                                          random.choice(letters),
                                          random.choice(digits),
                                          random.choice(digits),
                                          random.choice(letters),
                                          random.choice(letters)),
                " {}{}{} {}{}{}{}".format(random.choice(letters),
                                          random.choice(letters),
                                          random.choice(letters),
                                          random.choice(digits),
                                          random.choice(letters),
                                          random.choice(digits),
                                          random.choice(digits)),
                " {}{}{} {}{}{}{}".format(random.choice(letters),
                                          random.choice(letters),
                                          random.choice(letters),
                                          random.choice(digits),
                                          random.choice(digits),
                                          random.choice(letters),
                                          random.choice(digits)),
                " {}{}{} {}{}{}{}".format(random.choice(letters),
                                          random.choice(letters),
                                          random.choice(letters),
                                          random.choice(digits),
                                          random.choice(letters),
                                          random.choice(letters),
                                          random.choice(digits)),
                " {}{}{} {}{}{}{}".format(random.choice(letters),
                                          random.choice(letters),
                                          random.choice(letters),
                                          random.choice(letters),
                                          random.choice(letters),
                                          random.choice(digits),
                                          random.choice(digits)),
                " {}{}{} {}{}{}{}{}".format(random.choice(letters),
                                            random.choice(letters),
                                            random.choice(letters),
                                            random.choice(digits),
                                            random.choice(digits),
                                            random.choice(digits),
                                            random.choice(digits),
                                            random.choice(digits)),
                " {}{}{} {}{}{}{}{}".format(random.choice(letters),
                                            random.choice(letters),
                                            random.choice(letters),
                                            random.choice(digits),
                                            random.choice(digits),
                                            random.choice(digits),
                                            random.choice(digits),
                                            random.choice(letters)),
                " {}{}{} {}{}{}{}{}".format(random.choice(letters),
                                            random.choice(letters),
                                            random.choice(letters),
                                            random.choice(digits),
                                            random.choice(digits),
                                            random.choice(digits),
                                            random.choice(letters),
                                            random.choice(letters)),
                " {}{}{} {}{}{}{}".format(random.choice(letters),
                                          random.choice(letters),
                                          random.choice(letters),
                                          random.choice(letters),
                                          random.choice(digits),
                                          random.choice(digits),
                                          random.choice(letters)),
                " {}{}{} {}{}{}{}".format(random.choice(letters),
                                          random.choice(letters),
                                          random.choice(letters),
                                          random.choice(letters),
                                          random.choice(digits),
                                          random.choice(letters),
                                          random.choice(letters)),
                " {} {}{}{}".format(random.choice(letters),
                                    random.choice(digits),
                                    random.choice(digits),
                                    random.choice(digits)),
                " {} {}{}{}".format(random.choice(letters),
                                    random.choice(digits),
                                    random.choice(digits),
                                    random.choice(letters)),
                " {} {}{}{}".format(random.choice(letters),
                                    random.choice(digits),
                                    random.choice(letters),
                                    random.choice(digits)),
                " {} {}{}{}".format(random.choice(letters),
                                    random.choice(letters),
                                    random.choice(digits),
                                    random.choice(digits)),
                " {} {}{}{}".format(random.choice(letters),
                                    random.choice(digits),
                                    random.choice(letters),
                                    random.choice(letters)),
                " {} {}{}{}".format(random.choice(letters),
                                    random.choice(letters),
                                    random.choice(letters),
                                    random.choice(digits)),
                " {} {}{}{}".format(random.choice(letters),
                                    random.choice(letters),
                                    random.choice(digits),
                                    random.choice(letters))]
    return random.choice(patterns)


def create_license_plate(plate_scaling_factor=1, colour='white'):
    """
    Function creates an image of licence plate

    plate_scaling_factor (float/int): sets scale for license plate
    colour (str): sets licence plate's colour (white or yellow)
    """
    colours = {'white': (255, 255, 255, 255), 'yellow': (255, 255, 0, 255)}

    pl_img = Image.new('RGBA', 
                       (int(235 * plate_scaling_factor),
                        int(50 * plate_scaling_factor)), 
                       colours[colour])
    new_pl = ImageDraw.Draw(pl_img)
    font = ImageFont.truetype("font/arklatrs.ttf", int(41 * plate_scaling_factor))
    new_pl.rectangle([0 * plate_scaling_factor, 
                      0 * plate_scaling_factor, 
                      int(25 * plate_scaling_factor), 
                      int(50 * plate_scaling_factor)],fill="blue")

    new_pl.text((int(5 * plate_scaling_factor), 
                 int(1 * plate_scaling_factor)),"*",font=font,fill="yellow")
    new_pl.text((int(21 * plate_scaling_factor), 
                 int(5 * plate_scaling_factor)),"|",font=font)
    new_pl.text((int(25 * plate_scaling_factor), 
                 int(5 * plate_scaling_factor)),generate_plate_number(),font=font,fill="black")


    return pl_img


def generate_image(backgrounds='backgrounds', bg_scaling_factor=1, transform=False, blur=False, tilt=False, colour='white'):
    """
    Function iterates over images stored in backgrounds, generates a licence plate and
    pastes it onto the background.

    backgrounds (str): directory where background images are being stored
    bg_scaling_factor (int/float): Determines how large image will be, multiplier for 800x600 resolution
    transform (bool): if set, transforms licence plate randomly
    blur (bool): if set, blurs the image (the degree of blurriness is a random 0-3)
    tilt (bool): if set, tilts the image randomly from -45degree to 45 degree
    colour (str): determines the colour of the license plate
    """

    for bground in listdir(backgrounds):

    	plate_img = create_license_plate(random.uniform(0.3, 2), colour)

        img = Image.open(join(backgrounds, bground))
        img = img.resize((int(800 * bg_scaling_factor), 
                          int(600 * bg_scaling_factor)))

        img_w, img_h = img.size
        plate_w, plate_h = plate_img.size

        offset = (random.randint(1, img_w-plate_w), random.randint(1, img_h-plate_h))

        # transform plate a bit, so it's not perfect rectangle. Does not transform ideally - adds
        # a black bg filling at the sides, but this will be ommitted during labelling data phase

        plate_w, plate_h = plate_img.size
        angle = random.uniform(-0.5, 0.5) if transform else 0
        xshift = abs(angle) * plate_w / 4.5
        new_pl_w = plate_w + int(round(xshift))
        plate_img = plate_img.transform((new_pl_w, plate_h), Image.AFFINE, (1, angle, -xshift if angle > 0 else 0, 0, 1, 0), Image.BICUBIC)

        img.paste(plate_img, offset)
        img = img.filter(ImageFilter.GaussianBlur(random.uniform(0, 3) if blur else 0))
        img = img.rotate(random.uniform(-45, 45) if tilt else 0, False)
        #img.show()
        img.save('generated/' + bground)

# Generate images
# with some plates of different sizes - no transformations
generate_image(backgrounds='backgrounds/regular')
# with plates transformed only
generate_image(backgrounds='backgrounds/transformed', transform=True)
# with blur only
generate_image(backgrounds='backgrounds/blurred', blur=True)
# with tilt only
generate_image(backgrounds='backgrounds/tilted', tilt=True)
# with all possible effects
generate_image(backgrounds='backgrounds/all', transform=True, blur=True, tilt=True)
# with yellow plates
generate_image(backgrounds='backgrounds/yellow', colour='yellow')
# with yellow plates and all possible effects
generate_image(backgrounds='backgrounds/yellow_all', transform=True, blur=True, tilt=True, colour='yellow')
