# Academic API

Academic API demo cho Chủ đề 04, chạy Spring Boot trên cổng `8081` và dùng PostgreSQL database `academic_db`.

## Công cụ cần có

- JDK 17 (khuyến nghị Temurin hoặc Microsoft Build of OpenJDK).
- Maven Wrapper đã có trong project (`mvnw.cmd`); không bắt buộc cài Maven riêng.
- PostgreSQL 15/16 (có thể cài kèm pgAdmin).
- Postman để chạy collection.

Node.js không cần cho riêng Academic API. API dùng dữ liệu giả lập; không chứa dữ liệu sinh viên thật.

Tải từ trang chính thức: [Temurin JDK 17](https://adoptium.net/temurin/releases/?version=17), [PostgreSQL cho Windows](https://www.postgresql.org/download/windows/) và [Postman](https://www.postman.com/downloads/). PostgreSQL Windows installer có tùy chọn cài pgAdmin.

## 1. Kiểm tra cài đặt trên Windows

Mở PowerShell mới và kiểm tra Java:

```powershell
java -version
```

Kết quả cần hiển thị phiên bản 17. Repo đã có Maven Wrapper; lần đầu chạy wrapper cần Internet để tải Maven và dependencies.

## 2. Tạo database

Khởi động PostgreSQL. Trong pgAdmin, mở Query Tool kết nối database `postgres` và chạy:

```sql
CREATE DATABASE academic_db;
```

Nếu database đã tồn tại thì bỏ qua bước này. Khi chạy ứng dụng lần đầu, Spring Boot tự chạy `src/main/resources/schema.sql` và `data.sql` để tạo bảng và nạp 12 sinh viên mẫu. Cả hai file dùng `IF NOT EXISTS`/`ON CONFLICT` nên có thể khởi động lại an toàn.

## 3. Cấu hình kết nối

Mặc định API kết nối `localhost:5432`, database `academic_db`, username `postgres`, password `postgres`. Nếu thông tin PostgreSQL trên máy khác, đặt biến môi trường trong PowerShell trước khi chạy:

```powershell
$env:ACADEMIC_DB_USERNAME = "postgres"
$env:ACADEMIC_DB_PASSWORD = "mat_khau_postgres_cua_ban"
# Chỉ cần đổi nếu PostgreSQL không ở localhost:5432
$env:ACADEMIC_DB_URL = "jdbc:postgresql://localhost:5432/academic_db"
```

Thay `mat_khau_postgres_cua_ban` bằng mật khẩu bạn đã đặt khi cài PostgreSQL.

## 4. Chạy API

Từ thư mục `academic-api` trong repo `tich-hop-he-thong-chu-de-04`:

```powershell
.\mvnw.cmd spring-boot:run
```

Khi log báo ứng dụng đã khởi động, API ở `http://localhost:8081`. Để dừng, nhấn `Ctrl+C`.

## 5. Gọi thử

```powershell
curl.exe -i http://localhost:8081/api/students/B22DCCN001
```

Tạo sinh viên giả mới:

```powershell
curl.exe -i -X POST http://localhost:8081/api/students `
  -H "Content-Type: application/json" `
  -d '{"studentId":"B22DCCN013","fullName":"Nguyen Thi Test","email":"TestTN.b22cn013@stu.ptit.edu.vn","className":"D22CQCN01-B","major":"Cong nghe thong tin"}'
```

Collection đầy đủ nằm ở `../postman/academic.postman_collection.json`. Chạy các request theo thứ tự; request POST thành công tạo `B22DCCN013`, request kiểm tra trùng mã chạy sau đó.

## 6. Endpoint và mã phản hồi

| Method | Endpoint | Thành công | Lỗi chính |
|---|---|---:|---|
| GET | `/api/students/{studentId}` | 200 | 400 sai định dạng, 404 không có mã |
| POST | `/api/students` | 201 | 400 dữ liệu sai, 409 mã đã tồn tại |

Response lỗi dùng chung dạng `{ "status": 404, "error": "NOT_FOUND", "message": "..." }`.

## 7. Xử lý sự cố thường gặp

- `mvn` không được nhận diện: kiểm tra Maven đã thêm vào `Path`, sau đó mở PowerShell mới.
- `java -version` không phải 17: chỉnh `JAVA_HOME` và `Path` sang JDK 17.
- `Connection refused`: đảm bảo dịch vụ PostgreSQL đang chạy và cổng 5432 đúng.
- `password authentication failed`: đặt `ACADEMIC_DB_USERNAME`/`ACADEMIC_DB_PASSWORD` đúng trong cửa sổ PowerShell hiện tại.
- `database academic_db does not exist`: tạo database theo bước 2.
- Cổng 8081 đang được dùng: dừng ứng dụng chiếm cổng hoặc báo nhóm để thống nhất thay đổi contract.

