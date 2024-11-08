Thuật toán **Least Significant Bit (LSB)** là một phương pháp phổ biến trong kỹ thuật **giấu tin** (steganography), dùng để giấu thông tin trong một tệp hình ảnh mà không làm thay đổi đáng kể hình ảnh gốc. Ý tưởng của thuật toán LSB là thay đổi các bit ít quan trọng nhất của pixel hình ảnh để chứa thông tin bí mật, do đó người dùng khó nhận biết được sự thay đổi này khi xem hình ảnh.

### Cách thức hoạt động của thuật toán LSB:

1.  **Chọn kênh màu (Color Channel)**: Một hình ảnh có thể có nhiều kênh màu, ví dụ như RGB (đỏ, xanh lá, xanh dương). Mỗi kênh màu này sẽ có giá trị từ 0 đến 255 (8 bit cho mỗi kênh).
    
2.  **Chọn Pixel**: Hình ảnh được chia thành các pixel. Mỗi pixel có 3 giá trị (màu đỏ, màu xanh lá cây, và màu xanh dương) trong không gian màu RGB.
    
3.  **Thay đổi Bit Ít Quan Trọng Nhất (LSB)**:
    
    *   Thay vì thay đổi các bit quan trọng của màu sắc, thuật toán sẽ thay đổi bit ít quan trọng nhất (LSB). Ví dụ, thay vì thay đổi bit cao nhất của một giá trị màu (ví dụ 11111111), thuật toán thay đổi bit cuối cùng (LSB) (ví dụ 11111110).
        
    *   Điều này giúp giữ nguyên phần lớn màu sắc hình ảnh, vì thay đổi 1 bit ít quan trọng không làm thay đổi quá nhiều giá trị màu sắc.  
    https://imgur.com/Dfmz7lJ
        
4.  **Giấu Thông Tin**: Thông tin bí mật sẽ được mã hóa thành dạng nhị phân và được nhúng vào các bit ít quan trọng nhất của các pixel trong hình ảnh. Mỗi bit của thông tin sẽ thay thế LSB của từng pixel.
    

### Ví dụ về quá trình giấu tin:

Giả sử bạn có một giá trị pixel màu đỏ trong hình ảnh với giá trị nhị phân là 10110010. Bit ít quan trọng nhất là 0. Bạn có thông tin bí mật là 1, bạn có thể thay đổi giá trị này thành 10110011, chỉ thay đổi một bit nhưng vẫn giữ nguyên màu sắc gần như không đổi.

### Ưu điểm và nhược điểm:

*   **Ưu điểm**:
    
    *   Dễ dàng thực hiện.
        
    *   Không làm thay đổi hình ảnh nhiều.
        
*   **Nhược điểm**:
    
    *   Cần phải có một thuật toán giải mã để trích xuất thông tin.
        
    *   Nếu người nhận không biết phương pháp giấu tin, thông tin có thể bị lãng quên hoặc bị mất.