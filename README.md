# BÁO CÁO & MÃ NGUỒN PHẦN MỀM TÍCH HỢP HỆ THỐNG - CHỦ ĐỀ 04
## THÀNH VIÊN 2: FINANCE API VÀ KIỂM THỬ LỖI

### 1. Giới thiệu tổng quan
Dự án này là thành phần của đồ án môn học **Nhập môn Tích hợp hệ thống** (Học viện Công nghệ Bưu chính Viễn thông - PTIT), **Chủ đề 04: Tích hợp ứng dụng thông qua REST API và Cổng thông tin Portal**.

Thành viên 2 phụ trách:
- Xây dựng dịch vụ **Finance API** (cổng `8082`, sử dụng Spring Boot và cơ sở dữ liệu `finance_db` trên PostgreSQL).
- Xây dựng **Postman Collection** kiểm thử đầy đủ các endpoint (200, 400, 404, kiểm tra cấu trúc dữ liệu và logic nghiệp vụ).
- Thiết kế và thực nghiệm **Kiểm thử ngoại lệ** khi Finance không phản hồi (3 cách) để kiểm chứng khả năng **suy giảm có kiểm soát (Graceful Degradation)** của Portal Backend.
- Hoàn thiện báo cáo cá nhân chuẩn quy định học viện (`BAO_CAO_CA_NHAN_THANH_VIEN_2.docx` và `BAO_CAO_CA_NHAN_THANH_VIEN_2.md`).

---

### 2. Cấu trúc thư mục
```
TichHopHeThong_ChuDe04_FinanceAPI/
├── README.md                                  # Hướng dẫn chi tiết sử dụng & kiểm thử
├── API-CONTRACT.md                            # Hợp đồng API chuẩn giữa Portal, Academic, Finance
├── BAO_CAO_CA_NHAN_THANH_VIEN_2.docx          # Báo cáo cá nhân bản Word (.docx chuẩn PTIT)
├── BAO_CAO_CA_NHAN_THANH_VIEN_2.md            # Báo cáo cá nhân bản Markdown hoàn chỉnh
├── docker-compose.yml                         # Cấu hình khởi chạy PostgreSQL và Finance API
├── postman/
│   └── finance.postman_collection.json        # Postman Collection chứa 7 kịch bản test kèm test script
├── scripts/
│   ├── run_test_suite.py                      # Script Python tự động chạy các ca F1 -> F7
│   └── simulate_failure.sh                    # Hướng dẫn & minh họa 3 ca kiểm thử ngoại lệ
└── finance-api/                               # Mã nguồn dịch vụ Finance API (Spring Boot)
    ├── pom.xml
    ├── Dockerfile
    └── src/
        ├── main/
        │   ├── java/com/ptit/finance/
        │   │   ├── FinanceApiApplication.java
        │   │   ├── config/CorsConfig.java
        │   │   ├── controller/TuitionController.java
        │   │   ├── dto/StatusRequest.java
        │   │   ├── dto/ErrorResponse.java
        │   │   ├── exception/BadRequestException.java
        │   │   ├── exception/NotFoundException.java
        │   │   ├── exception/GlobalExceptionHandler.java
        │   │   ├── model/Tuition.java
        │   │   └── repository/TuitionRepository.java
        │   └── resources/
        │       ├── application.yml
        │       ├── schema.sql
        │       └── data.sql
        └── test/java/com/ptit/finance/TuitionControllerTest.java
```

---

### 3. Hướng dẫn khởi chạy

#### Cách 1: Khởi chạy bằng Docker Compose (Khuyên dùng)
Yêu cầu: Đã cài đặt Docker và Docker Compose.
```bash
# Khởi động PostgreSQL (finance_db) và Finance API (port 8082)
docker compose up -d

# Xem log hoạt động
docker compose logs -f finance-api
```

#### Cách 2: Khởi chạy trực tiếp bằng Maven
Yêu cầu: Đã có PostgreSQL đang chạy tại localhost:5432 với database `finance_db`, user `app`, password `app` (hoặc cấu hình lại biến môi trường).
```bash
cd finance-api
mvn clean spring-boot:run
```

---

### 4. Kiểm thử các chức năng chính (Postman & Script)

#### 4.1. Nhập Postman Collection
- Mở Postman -> Chọn **Import** -> Chọn file `postman/finance.postman_collection.json`.
- Chạy toàn bộ Collection bằng **Collection Runner**. Toàn bộ 7 request đều có Assertions kiểm tra status code và nội dung JSON.

#### 4.2. Chạy kiểm thử tự động bằng Python
```bash
python3 scripts/run_test_suite.py
```

Danh sách các ca kiểm thử:
1. `GET /api/tuitions/B22DCCN001`: Trả 200 OK và mảng học phí gồm 2 khoản (2026-1: UNPAID, 2025-2: PAID).
2. `GET /api/tuitions/B22DCCN013`: Trả 404 Not Found (mã đúng nhưng chưa có học phí).
3. `GET /api/tuitions/abc123`: Trả 400 Bad Request (mã không khớp regex `^B\d{2}DC[A-Z]{2}\d{3}$`).
4. `PUT /api/tuitions/1/status` với body `{"status":"PAID"}`: Trả 200 OK và bản ghi cập nhật sang `PAID`.
5. `PUT /api/tuitions/1/status` với body `{"status":"DONE"}`: Trả 400 Bad Request (trạng thái ngoài PAID/UNPAID).
6. `PUT /api/tuitions/9999/status`: Trả 404 Not Found (ID không tồn tại).
7. `GET /api/tuitions/slow?delay=5000`: Trả 200 OK sau khi ngủ đúng thời gian chỉ định.

---

### 5. Kiểm thử ngoại lệ: 3 cách làm Finance không phản hồi
Thành viên 2 chịu trách nhiệm kiểm thử khả năng chịu lỗi của Portal khi Finance gặp sự cố:
1. **Cách a (Tắt dịch vụ)**:
   ```bash
   docker compose stop finance-api
   ```
   - Portal gọi sang sẽ bị từ chối kết nối ngay lập tức (`ConnectException`).
   - Phản hồi từ Portal: HTTP 200, `student` đầy đủ thông tin, `tuitions = null`, `warnings = ["Không lấy được học phí"]`. Thời gian phản hồi: < 50ms.
2. **Cách b (Làm chậm dịch vụ với biến môi trường)**:
   ```bash
   FINANCE_DELAY_MS=5000 docker compose up -d finance-api
   ```
   - Finance sẽ cố tình trễ 5 giây khi xử lý `GET /api/tuitions/{studentId}`.
   - Portal có cấu hình timeout cho Finance là 3 giây (3000ms).
   - Phản hồi từ Portal: Sau đúng 3 giây xảy ra `ReadTimeoutException`, Portal thực hiện suy giảm có kiểm soát, trả về HTTP 200 + dữ liệu sinh viên + cảnh báo học phí.
3. **Cách c (Cấu hình sai cổng)**:
   - Trong Portal Backend, đổi `FINANCE_URL=http://localhost:9999`.
   - Kết nối bị từ chối ngay lập tức tương tự Cách a.
