# Phần Thành viên 1: Academic API

## 1. Vai trò trong kiến trúc

Academic API là dịch vụ độc lập quản lý thông tin sinh viên trong `academic_db`. Dịch vụ cung cấp dữ liệu qua REST API trên cổng `8081`. Portal gọi API theo mã sinh viên; Portal không truy cập trực tiếp cơ sở dữ liệu Academic. Cách tổ chức này thể hiện tích hợp ứng dụng qua giao diện API và giảm phụ thuộc giữa Portal với cấu trúc bảng nội bộ.

## 2. Cơ sở lý thuyết liên quan

### 2.1. Tích hợp ứng dụng qua API

Mỗi ứng dụng công bố một giao diện trao đổi có quy tắc đầu vào, đầu ra và mã trạng thái. Trong demo, Academic chịu trách nhiệm tra cứu và tạo hồ sơ; Portal là bên gọi API và tổng hợp kết quả với dữ liệu từ Finance. Hai bên thống nhất hợp đồng API trước khi tích hợp.

### 2.2. REST endpoint và HTTP method

Endpoint là địa chỉ tài nguyên mà client gửi yêu cầu đến. Academic sử dụng `GET /api/students/{studentId}` để đọc hồ sơ và `POST /api/students` để tạo hồ sơ. `GET` không làm thay đổi dữ liệu; `POST` gửi một representation JSON để tạo tài nguyên mới.

### 2.3. Request/response JSON

Request tạo sinh viên và response trả hồ sơ đều dùng JSON UTF-8. Các trường theo camelCase: `studentId`, `fullName`, `email`, `className`, `major`. JSON giúp Portal và API trao đổi dữ liệu có cấu trúc mà không cần dùng chung ngôn ngữ lập trình hay truy cập trực tiếp database.

### 2.4. Mã trạng thái HTTP

`200 OK` là tra cứu thành công; `201 Created` là tạo sinh viên thành công; `400 Bad Request` là mã hoặc nội dung đầu vào không hợp lệ; `404 Not Found` là mã đúng định dạng nhưng không có trong database; `409 Conflict` là mã sinh viên đã tồn tại. Quy tắc này giúp client phân biệt lỗi dữ liệu, tài nguyên không tồn tại và xung đột khi tạo mới.

## 3. Cài đặt Academic API

Ứng dụng dùng Spring Boot, Spring Web, Spring JDBC, Jakarta Validation và PostgreSQL. `StudentController` khai báo endpoint; `StudentService` kiểm tra mã sinh viên và áp dụng nghiệp vụ; `JdbcStudentRepository` truy vấn/lưu dữ liệu; `GlobalExceptionHandler` chuyển lỗi thành JSON thống nhất theo hợp đồng.

Mã sinh viên kiểm tra theo `^B\d{2}DC[A-Z]{2}\d{3}$`. Dữ liệu POST bắt buộc có đủ trường; email được kiểm tra định dạng. CSDL có khóa chính `student_id`, vì vậy thao tác tạo trùng mã trả `409 Conflict`.

## 4. Kiểm thử bằng Postman

Collection `postman/academic.postman_collection.json` có các ca:

| Ca | Request | Kết quả mong đợi |
|---|---|---|
| Tra cứu có dữ liệu | GET `B22DCCN001` | 200, đủ 5 trường |
| Không tìm thấy | GET `B22DCCN999` | 404, `NOT_FOUND` |
| Mã sai định dạng | GET `abc123` | 400, `BAD_REQUEST` |
| Tạo mới | POST `B22DCCN013` | 201, trả bản ghi vừa tạo |
| Email sai | POST email không hợp lệ | 400, `BAD_REQUEST` |
| Tạo trùng mã | POST lại `B22DCCN013` | 409, `CONFLICT` |

Chạy POST tạo mới trước POST trùng mã. Sau khi API chạy thật, lưu ảnh request/response của từng ca vào thư mục bằng chứng của nhóm và ghi lại kết quả quan sát. Chưa điền kết quả thực tế trong tài liệu này khi chưa chạy trên môi trường đã cài đủ PostgreSQL, JDK và Maven.

## 5. Dữ liệu mẫu

`academic-api/src/main/resources/data.sql` chứa 12 hồ sơ hư cấu. Mã, email theo format nhóm quy định; ngành `Công nghệ thông tin` khớp tiền tố `CN`. Dữ liệu có thể nạp lại mà không tạo bản ghi trùng.
