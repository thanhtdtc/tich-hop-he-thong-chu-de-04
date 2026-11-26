# Academic API evidence

Lưu ảnh chụp Postman hoặc terminal của các ca kiểm thử Academic tại thư mục này.

- `A-01-success.png` — GET sinh viên tồn tại, HTTP 200.
- `A-02-not-found.png` — GET mã đúng định dạng nhưng không tồn tại, HTTP 404.
- `A-03-invalid-id.png` — GET mã sai định dạng, HTTP 400.
- `A-04-create.png` — POST sinh viên mới, HTTP 201.
- `A-05-invalid-data.png` — POST dữ liệu/email không hợp lệ, HTTP 400.
- `A-06-duplicate.png` — POST trùng mã, HTTP 409.

Chụp ảnh sau khi mỗi request hoàn tất. Không đưa mật khẩu PostgreSQL hoặc thông tin cá nhân thật vào ảnh.
