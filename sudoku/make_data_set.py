import cv2
import numpy as np

import os.path


def display(image, name='image'):
    cv2.namedWindow(name, 0)
    cv2.resizeWindow(name, 2000, 1400)
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_all_file(directory):
    image_path_list = []
    valid_image_extensions = [".jpg", ".jpeg", ".png", ".tif",
                              ".tiff"]  # specify your vald extensions here
    valid_image_extensions = [item.lower() for item in valid_image_extensions]

    for file in os.listdir(directory):
        extension = os.path.splitext(file)[1]
        if extension.lower() not in valid_image_extensions:
            continue
        image_path_list.append(os.path.join(directory, file))
        return image_path_list


def segment_images(image_path_list, images_path):
    for imagePath in image_path_list:
        image = cv2.imread(imagePath)

        # display the image on screen with imshow()
        # after checking that it loaded
        if image is not None:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            _, threshed_image = cv2.threshold(gray, 127, 255,
                                              cv2.THRESH_BINARY_INV)

            kernel_matrix = np.ones((2, 2), np.uint8)
            img_dilation = cv2.dilate(
                threshed_image, kernel_matrix, iterations=1
            )
            _, contours, _ = cv2.findContours(img_dilation.copy(),
                                              cv2.RETR_EXTERNAL,
                                              cv2.CHAIN_APPROX_SIMPLE)

            for i, contour in enumerate(contours):
                x, y, w, h = cv2.boundingRect(contour)
                segment_image = gray[y:y + h, x:x + w]
                cv2.imwrite(os.path.join(
                    images_path, f'image-{x}-file{i}.png'), segment_image
                )
        elif image is None:
            print("Error loading: " + imagePath)
            # end this loop iteration and move on to next image
            continue


if __name__ == '__main__':
    image_directory = '../../numbers/'
    path_list = get_all_file(image_directory)
    segment_images(path_list, image_directory)
