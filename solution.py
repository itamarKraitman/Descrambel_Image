import sqlite3
import numpy as np
import cv2

TILE_SIZE = 41


def rotate_tile_to_original_angle(tile_rotated: np.ndarray, rotation_direction: str) -> np.ndarray:
    """
    rotate tile to original form
    :param tile_rotated: tile rotated clockwise or counterclockwise
    :param rotation_direction:the direction the tile is rotated
    :return: tile rotated back to its original form
    """
    return cv2.rotate(tile_rotated,
                      cv2.ROTATE_90_CLOCKWISE) if rotation_direction == "clockwise" else cv2.rotate(
        tile_rotated, cv2.ROTATE_90_COUNTERCLOCKWISE)


def find_tile_and_place_in_descrambled(tile: tuple):
    """
    find the tile in the scrambled image, rotate it back to its original angle
    :param tile: tile in the scrambled image
    """
    # divide tile's properties to source coordinates, destination coordinates and rotation
    source, destination, rotation = tile[:2], tile[2:4], tile[4]
    # find tiles coordinates in scrambled image using destination coordinates
    x_in_scrambled, y_in_scrambled = destination[0] * TILE_SIZE, destination[1] * TILE_SIZE
    # find tile in scrambled image
    tile_in_scrambled = scrambled_image[y_in_scrambled:y_in_scrambled + TILE_SIZE,
                        x_in_scrambled:x_in_scrambled + TILE_SIZE]
    # rotate tile back to its original angle
    tile_descrambled = rotate_tile_to_original_angle(tile_rotated=tile_in_scrambled, rotation_direction=rotation)

    # place descrambled tile in descrambled image
    x_in_descrambled, y_in_descrambled = source[0] * TILE_SIZE, source[1] * TILE_SIZE
    descrambled_image[y_in_descrambled:y_in_descrambled + TILE_SIZE,
                        x_in_descrambled:x_in_descrambled + TILE_SIZE] = tile_descrambled


# connecting to db
with sqlite3.connect("assignment.sqlite") as conn:
    cursor = conn.cursor()

    # retrieve a list of all the tiles, each tile represented as tuple (sX, sY, desX, dexY, rotation)
    cursor.execute("SELECT * FROM transform")
    all_tiles = cursor.fetchall()

# read scrambled image
scrambled_image = cv2.imread("assignment.jpg")

# create a blank image with dimension 984*984 with 3 color channels (each pixel in RGB) to store the descrambled image
descrambled_image = np.zeros((984, 984, 3),
                             dtype=np.uint8)  # uint8 is the standard stat type used to represent a pixel (0,255)

# for each tile, isolate, rotate and place it in the descrambled image
for tile in all_tiles:
    find_tile_and_place_in_descrambled(tile=tile)

cv2.imwrite("Descrambled Image.jpg", descrambled_image)
