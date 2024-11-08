import cv2
import numpy as np

def hide_text_in_image(image_path, text):
    img = cv2.imread(image_path)
    data = list(img.flatten())
    
    # Chuyển đổi văn bản thành dãy bit
    binary_data = ''.join(format(ord(i), '08b') for i in text)

    # Kiểm tra xem hình ảnh có đủ dung lượng để chứa dữ liệu không
    if len(binary_data) > len(data):
        raise ValueError("Hinh anh k du dung luong de giau du lieu.")

    # Thay thế các bit LSB
    index = 0
    for i in range(len(binary_data)):
        data[index] = int(bin(data[index])[2:9] + binary_data[i], 2)
        index += 1

    # Chuyển đổi dữ liệu trở lại hình ảnh
    img_new = np.array(data, dtype=np.uint8).reshape(img.shape)

    # Lưu hình ảnh đã giấu
    cv2.imwrite("hide.png", img_new)

# Ví dụ sử dụng
image_path = "Images.png"
text_to_hide = "Hello, I'm Duong"
hide_text_in_image(image_path, text_to_hide)