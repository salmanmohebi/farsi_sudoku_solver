import os

import cv2


def get_all_file(directory):
    image_path_list = []
    valid_image_extensions = [".jpg", ".jpeg", ".png", ".tif", ".tiff"]  # specify your vald extensions here
    valid_image_extensions = [item.lower() for item in valid_image_extensions]
    for file in os.listdir(directory):
        extension = os.path.splitext(file)[1]
        if extension.lower() not in valid_image_extensions:
            continue
        image_path_list.append(os.path.join(directory, file))
    return image_path_list


image_directory = '../../numbers/0/'
path_list = get_all_file(image_directory)
print(path_list)
for imagePath in path_list:
    image = cv2.imread(imagePath)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.resize(image, (500, 500))
    cv2.imshow('imageeeeeee', image)
    cv2.waitKey(0)
