import cv2
import numpy as np

def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    data = list(img.flatten())
    
    # Biến chứa dữ liệu bit để đọc
    binary_data = ""
    
    # Lấy từng bit LSB từ ảnh
    for value in data:
        binary_data += bin(value)[-1]  # Lấy bit LSB của mỗi giá trị pixel

    # Chuyển đổi dãy bit thành văn bản
    text = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        char = chr(int(byte, 2))  # Chuyển từ chuỗi 8 bit thành ký tự
        text += char
        if char == "\0":  # Dừng lại khi gặp ký tự kết thúc chuỗi (nếu có)
            break

    return text

# Ví dụ sử dụng
image_path = "hide.png"
extracted_text = extract_text_from_image(image_path)
print("Tin đã được giấu là:", extracted_text)
