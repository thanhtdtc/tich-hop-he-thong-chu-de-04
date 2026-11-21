# API-CONTRACT.md

Hợp đồng API - Chủ đề 04: Tích hợp ứng dụng qua REST API và Portal

> Đây là thỏa thuận chung của cả nhóm. **Không ai tự ý đổi** tên trường, cổng, mã lỗi khi chưa báo nhóm và cập nhật file này trước khi sửa code.

| Phiên bản | Ngày | Người sửa | Nội dung |
|---|---|---|---|
| 1.0 | ..../..../...... | Nhóm trưởng | Bản đầu tiên, cả nhóm đã xác nhận |

---

## 1. Quy ước chung

- Mã sinh viên theo regex `^B\d{2}DC[A-Z]{2}\d{3}$`, ví dụ `B22DCCN001`.
- Dữ liệu giả lập: 12 sinh viên `B22DCCN001` đến `B22DCCN012`, mỗi sinh viên có 1 đến 3 khoản học phí (có cả `PAID` và `UNPAID`). Không dùng dữ liệu cá nhân thật.
- Mọi API nhận và trả JSON (`Content-Type: application/json`), mã hóa UTF-8.
- Tên trường JSON dùng `camelCase`. Ngày dùng định dạng `yyyy-MM-dd`. Số tiền là số nguyên (VNĐ).
- Mọi response lỗi dùng chung một định dạng (mục 6).

## 2. Dịch vụ, cổng và cơ sở dữ liệu

| Dịch vụ | Cổng | CSDL | Người phụ trách |
|---|---|---|---|
| Academic API | 8081 | `academic_db` (PostgreSQL) | Thành viên 1 |
| Finance API | 8082 | `finance_db` (PostgreSQL) | Thành viên 2 |
| Portal backend | 8080 | Không có | Nhóm trưởng |
| Portal frontend | 3000 | Không có | Nhóm trưởng |

Portal chỉ gọi hai API, **không** đọc trực tiếp CSDL của Academic hay Finance.

## 3. Mô hình dữ liệu

**student** (academic_db)

| Cột | Kiểu | Ràng buộc |
|---|---|---|
| student_id | VARCHAR(12) | Khóa chính, đúng regex mã sinh viên |
| full_name | VARCHAR(100) | Bắt buộc |
| email | VARCHAR(100) | Đúng định dạng email |
| class_name | VARCHAR(50) | Tên lớp |
| major | VARCHAR(50) | Ngành |

**tuition** (finance_db)

| Cột | Kiểu | Ràng buộc |
|---|---|---|
| id | BIGINT | Khóa chính, tự tăng |
| student_id | VARCHAR(12) | Mã tham chiếu, có chỉ mục, **không** tạo khóa ngoại sang academic_db |
| semester | VARCHAR(10) | Ví dụ `2026-1` |
| amount | BIGINT | Lớn hơn 0 |
| status | VARCHAR(10) | Chỉ `PAID` hoặc `UNPAID` |
| due_date | DATE | Hạn đóng |

## 4. Endpoint

### 4.1. Academic API (cổng 8081)

#### GET /api/students/{studentId}

Lấy thông tin một sinh viên.

- Thành công: `200`
```json
{
  "studentId": "B22DCCN001",
  "fullName": "Nguyen Van A",
  "email": "a@stu.ptit.edu.vn",
  "className": "D22CQCN01-B",
  "major": "CNTT"
}
```
- Mã sai định dạng: `400`. Không có trong DB: `404`.

#### POST /api/students

Thêm sinh viên mới.

- Request:
```json
{
  "studentId": "B22DCCN013",
  "fullName": "Tran Thi B",
  "email": "b@stu.ptit.edu.vn",
  "className": "D22CQCN01-B",
  "major": "CNTT"
}
```
- Thành công: `201`, body là bản ghi vừa tạo (cùng dạng như GET).
- Thiếu trường bắt buộc, mã sai định dạng, email sai: `400`.
- Mã đã tồn tại: `409`.

### 4.2. Finance API (cổng 8082)

#### GET /api/tuitions/{studentId}

Lấy danh sách khoản học phí của một sinh viên.

- Thành công: `200`
```json
[
  {
    "id": 1,
    "studentId": "B22DCCN001",
    "semester": "2026-1",
    "amount": 8500000,
    "status": "UNPAID",
    "dueDate": "2026-12-15"
  }
]
```
- Mã sai định dạng: `400`. Sinh viên chưa có khoản học phí nào: `404`.

#### PUT /api/tuitions/{id}/status

Cập nhật trạng thái thanh toán của một khoản học phí.

- Request:
```json
{ "status": "PAID" }
```
- Thành công: `200`, body là bản ghi đã cập nhật (cùng dạng như phần tử trong GET).
- `status` khác `PAID` / `UNPAID`: `400`. Không có `id`: `404`.

#### Kiểm thử Finance chậm (chỉ dùng để test timeout, không dùng trong luồng thật)

- `GET /api/tuitions/slow?delay={ms}`: chờ `delay` mili giây rồi mới trả danh sách học phí. Gọi trực tiếp bằng Postman để chứng minh Finance thật sự chậm.
- Biến môi trường `FINANCE_DELAY_MS` (mặc định 0): nếu đặt, ví dụ `FINANCE_DELAY_MS=5000`, endpoint `GET /api/tuitions/{studentId}` sẽ chờ chừng đó mili giây trước khi trả lời. Dùng cách này để kiểm tra Portal có cắt timeout sau 3 giây hay không, vì Portal chỉ gọi `/api/tuitions/{studentId}`, không gọi `/slow`.

### 4.3. Portal backend (cổng 8080)

#### GET /api/portal/students/{studentId}/summary

Tổng hợp thông tin sinh viên (Academic) và học phí (Finance).

- Đủ dữ liệu: `200`
```json
{
  "student": {
    "studentId": "B22DCCN001",
    "fullName": "Nguyen Van A",
    "email": "a@stu.ptit.edu.vn",
    "className": "D22CQCN01-B",
    "major": "CNTT"
  },
  "tuitions": [
    {
      "id": 1,
      "studentId": "B22DCCN001",
      "semester": "2026-1",
      "amount": 8500000,
      "status": "UNPAID",
      "dueDate": "2026-12-15"
    }
  ],
  "warnings": []
}
```
- Finance không phản hồi: `200`, vẫn có thông tin sinh viên
```json
{
  "student": { "...": "..." },
  "tuitions": null,
  "warnings": ["Không lấy được học phí: Finance API không phản hồi"]
}
```
- Finance trả 404: `200`, `tuitions` là `null`, `warnings` có "Sinh viên chưa có khoản học phí".

## 5. Bảng mã trạng thái

| Tình huống | Mã | Ghi chú |
|---|---|---|
| Lấy dữ liệu thành công | 200 | |
| Tạo mới thành công (POST sinh viên) | 201 | |
| Cập nhật thành công (PUT học phí) | 200 | |
| Mã sinh viên sai định dạng | 400 | Portal kiểm tra trước, không gọi API nào |
| Dữ liệu gửi lên thiếu hoặc không hợp lệ | 400 | |
| Trạng thái học phí không phải `PAID`/`UNPAID` | 400 | |
| Không tìm thấy sinh viên hoặc học phí | 404 | |
| POST sinh viên trùng mã | 409 | Nhóm chốt dùng 409 |
| Academic không phản hồi (qua Portal) | 503 | Không có sinh viên thì không hiển thị gì |
| Finance không phản hồi hoặc 404 (qua Portal) | 200 + `warnings` | Suy giảm có kiểm soát |

## 6. Định dạng lỗi chung

Mọi API (Academic, Finance, Portal) trả lỗi theo đúng mẫu này:

```json
{
  "status": 404,
  "error": "NOT_FOUND",
  "message": "Không tìm thấy sinh viên B22DCCN999"
}
```

| `status` | `error` |
|---|---|
| 400 | `BAD_REQUEST` |
| 404 | `NOT_FOUND` |
| 409 | `CONFLICT` |
| 503 | `SERVICE_UNAVAILABLE` |

## 7. Quy tắc cho Portal khi gọi API

- Kiểm tra mã sinh viên bằng regex trước; sai thì trả `400` ngay.
- Gọi Academic trước, sau đó gọi Finance.
- Timeout: connect khoảng 1 giây, read khoảng 3 giây.
- Academic 404 thì Portal trả 404; Academic lỗi hoặc quá timeout thì Portal trả 503.
- Finance lỗi, quá timeout hoặc 404 thì Portal vẫn trả 200, đặt `tuitions = null` và thêm cảnh báo vào `warnings`.
- Ghi log mỗi lần gọi: URL, thời gian phản hồi (ms), mã trả về.

## 8. CORS

- **Portal backend (8080)** phải cho phép nguồn `http://localhost:3000`, vì giao diện React gọi Portal backend từ trình duyệt.
- Academic và Finance chỉ cần cho phép `http://localhost:3000` nếu giao diện gọi trực tiếp (mặc định không gọi, chỉ Portal backend gọi hai API này nên không bị CORS).

## 9. Quy trình thay đổi hợp đồng

1. Người muốn đổi nhắn vào nhóm, nêu lý do và phần bị ảnh hưởng.
2. Cả nhóm đồng ý.
3. Nhóm trưởng cập nhật file này và tăng phiên bản ở bảng đầu file.
4. Sau đó mới sửa code.
