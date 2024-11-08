from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Hàm để tính toán sự khác biệt giữa hai hình ảnh
def show_image_difference(image_path1, image_path2):
    # Mở hai ảnh
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    # Chuyển cả hai ảnh về chế độ RGB 
    image1 = image1.convert("RGB")
    image2 = image2.convert("RGB")

    # Chuyển hình ảnh thành mảng numpy
    img1 = np.array(image1)
    img2 = np.array(image2)

    # Tính toán sự khác biệt (chênh lệch giữa các pixel)
    diff = np.abs(img1 - img2)

    # Chuyển sự khác biệt thành hình ảnh để hiển thị
    diff_image = Image.fromarray(np.uint8(diff))

    # Hiển thị hình ảnh gốc, hình ảnh đã thay đổi và sự khác biệt
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].imshow(img1)
    axes[0].set_title('Gốc')
    axes[0].axis('off')

    axes[1].imshow(img2)
    axes[1].set_title('Sau khi giấu tin')
    axes[1].axis('off')

    axes[2].imshow(diff_image)
    axes[2].set_title('Sự khác biệt')
    axes[2].axis('off')

    plt.show()

# Ví dụ sử dụng
show_image_difference("Images.png", "hide.png")
