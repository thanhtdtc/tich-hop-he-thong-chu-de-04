# Chủ đề 04: Tích hợp ứng dụng qua REST API và Portal

Bài tập lớn học phần Nhập môn Tích hợp hệ thống. Hệ thống gồm hai dịch vụ độc lập
(Academic, Finance) và một Portal tổng hợp dữ liệu từ hai dịch vụ qua REST API.
Toàn bộ dữ liệu là dữ liệu giả lập.

## Thành viên

| Vai trò | Họ tên | MSSV | Phụ trách | Nhánh Git |
|---|---|---|---|---|
| Nhóm trưởng | [Điền] | [Điền] | Portal, tích hợp, Docker, tổng hợp báo cáo | `feature/portal` |
| Thành viên 1 | [Điền] | [Điền] | Academic API, Postman | `feature/academic` |
| Thành viên 2 | [Điền] | [Điền] | Finance API, kiểm thử lỗi | `feature/finance` |

## Kiến trúc

```
Người dùng -> Portal frontend :3000 -> Portal backend :8080
                                          |-> Academic API :8081 -> academic_db
                                          |-> Finance API  :8082 -> finance_db
```

Portal không có cơ sở dữ liệu riêng và không đọc trực tiếp CSDL của hệ thống khác.
Chi tiết endpoint, JSON mẫu và mã lỗi: xem [API-CONTRACT.md](API-CONTRACT.md).

## Cấu trúc thư mục

| Thư mục | Nội dung |
|---|---|
| `academic-api/` | Dịch vụ Academic (Spring Boot, cổng 8081) |
| `finance-api/` | Dịch vụ Finance (Spring Boot, cổng 8082) |
| `portal-backend/` | Portal backend (Spring Boot, cổng 8080) |
| `portal-frontend/` | Giao diện Portal (React + Ant Design, cổng 3000) |
| `postman/` | Postman collection kiểm thử |
| `docs/` | Sơ đồ, ảnh bằng chứng, báo cáo |

## Yêu cầu cài đặt

- Docker và Docker Compose (cách chạy nhanh nhất)
- Hoặc chạy thủ công: Java 17, Maven, Node.js 18+, PostgreSQL 14+
- Postman để chạy lại kiểm thử

## Chạy bằng Docker

```bash
cp .env.example .env        # điền mật khẩu thật nếu cần
docker compose up --build
```

| Thành phần | Địa chỉ |
|---|---|
| Portal giao diện | http://localhost:3000 |
| Portal backend | http://localhost:8080/api/portal/students/B22DCCN001/summary |
| Academic API | http://localhost:8081/api/students/B22DCCN001 |
| Finance API | http://localhost:8082/api/tuitions/B22DCCN001 |

> [Cập nhật lại các bước và địa chỉ này theo đúng cấu hình thực tế khi hoàn thiện.]

## Chạy thủ công (không dùng Docker)

1. Tạo hai database `academic_db` và `finance_db` trong PostgreSQL.
2. Chạy từng dịch vụ: `mvn spring-boot:run` trong `academic-api`, `finance-api`, `portal-backend`.
3. Chạy giao diện: `npm install` rồi `npm run dev` trong `portal-frontend`.

## Tái hiện các kịch bản kiểm thử

| Kịch bản | Cách thực hiện | Kết quả mong đợi |
|---|---|---|
| Thành công | Tra cứu `B22DCCN001` | 200, đủ thông tin sinh viên và học phí |
| Không tìm thấy | Tra cứu `B22DCCN999` | 404 |
| Đầu vào sai | Nhập `abc123` | 400, Portal không gọi API nào |
| Finance tắt | `docker compose stop finance-api` rồi tra cứu | 200 + cảnh báo, vẫn có thông tin sinh viên |
| Finance chậm | Chạy Finance với `FINANCE_DELAY_MS=5000` rồi tra cứu | 200 + cảnh báo sau khoảng 3 giây |
| Finance sai cổng | Đặt `FINANCE_URL` trỏ cổng sai, khởi động lại Portal | 200 + cảnh báo, trả lời nhanh |
| Academic tắt | `docker compose stop academic-api` rồi tra cứu | 503 |

Postman: nhập các file trong thư mục `postman/` vào Postman, chọn Run collection.

## Quy ước làm việc

- `main` luôn chạy được; không push thẳng, mọi thay đổi qua Pull Request và được nhóm trưởng review.
- Mỗi người làm trên nhánh riêng và chỉ sửa trong thư mục của mình.
- Commit message có tiền tố: `Academic: ...`, `Finance: ...`, `Portal: ...`, `Docs: ...`.
- Không commit mật khẩu thật, file `.env`, `target/`, `node_modules/`.
- Đổi tên trường, cổng hay mã lỗi phải báo nhóm và cập nhật `API-CONTRACT.md` trước khi sửa code.

## Dữ liệu giả lập

12 sinh viên `B22DCCN001` đến `B22DCCN012`, mỗi sinh viên có 1 đến 3 khoản học phí.
Không sử dụng dữ liệu cá nhân thực tế.
