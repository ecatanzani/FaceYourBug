"""Sueprvisor class to handle custom exception"""
import traceback
import sys
import cv2

class Dian0Supervisor:
    def __init__(
        self,
        display_target_size: tuple = (650, 500),
        display_rarget_image: str = 'assets/happycat.jpg'):
        self.default_excepthook = sys.excepthook
        self.target_size: tuple = display_target_size
        self.image_path = display_rarget_image

    def __call__(self, exc_type, exc_value, exc_traceback):
        error_message: str = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        img = cv2.imread(self.image_path)
        img = cv2.resize(img, self.target_size[::-1], interpolation=cv2.INTER_AREA)
        print('[ERROR] YOU did it again bitch...')
        print(error_message)
        cv2.imshow("You're Fucked", img)
        cv2.waitKey(0)
        self.default_excepthook(exc_type, exc_value, exc_traceback)
