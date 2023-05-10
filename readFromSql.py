import sqlite3
import numpy as np
import cv2
from collections import Counter

conn = sqlite3.connect('assignment.sqlite')
cursor = conn.cursor()  # creating cursor to interact with database

cursor.execute("SELECT * FROM transform ")
rows = cursor.fetchall()

cursor.execute("SELECT MAX(source_tile_x), MIN(source_tile_x), MAX(source_tile_y), MIN(source_tile_y) FROM transform ")
tiles_properties = cursor.fetchall()
print(tiles_properties)

cursor.execute("SELECT direction FROM transform ")
directions = cursor.fetchall()
print(Counter(directions).keys())
print(Counter(directions))

cursor.execute("SELECT * FROM transform WHERE source_tile_x = 0 ORDER BY source_tile_y")
zeros = cursor.fetchall()
print(zeros)

for ele in zeros[0]:
    print(ele)

image = cv2.imread("assignment.jpg")
pixel = image[0, 0]
print(type(pixel))


# 0-23 is the range
# each row is tuple of the format: (source_x, source_y, destination_x, destination_y)
# find pixel in scrambled using calculation offset
# to rotate- using rotate() of PIL or openCV

# for row in rows:
#     print(row)

def find_pixel_in_scrambled_image(source_x: int, source_y: int) -> tuple:
    """
    Calculate coordinates of descrambled image from scrambled coordinates
    :param source_x: source x coordinate
    :param source_y: source y coordinate
    :return: coordinates in descrambled image
    """
    pass


def rotate_pixel_to_original(pixel_rotated: np.ndarray, rotation_direction: str) -> np.ndarray:
    """
    rotate pixel to original form
    :param pixel_rotated: pixel rotated clockwise or counterclockwise
    :param rotation_direction:the direction the pixel is rotated
    :return: pixel rotated back to its original form
    """
    pass
