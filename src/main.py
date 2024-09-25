import os
import sys

cur_dir = os.path.abspath(os.path.dirname(__file__))

sys.path.append(cur_dir + "/../modules/")
from controller import Controller


def main():
    """ main """
    controller = Controller()
    controller.start()


if __name__ == '__main__':
    main()