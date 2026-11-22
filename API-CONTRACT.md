# HỢP ĐỒNG API (API CONTRACT)
## HỌC PHẦN: NHẬP MÔN TÍCH HỢP HỆ THỐNG - CHỦ ĐỀ 04
**Tích hợp ứng dụng thông qua REST API và Cổng thông tin Portal**

---

### 1. Giới thiệu chung
Hệ thống gồm ba dịch vụ độc lập:
1. **Academic API (`http://localhost:8081`)**: Quản lý thông tin hồ sơ sinh viên, sở hữu CSDL `academic_db`.
2. **Finance API (`http://localhost:8082`)**: Quản lý học phí sinh viên, sở hữu CSDL `finance_db`.
3. **Portal Backend (`http://localhost:8080`)**: Tích hợp, tổng hợp dữ liệu từ Academic và Finance, không có CSDL riêng.

---

### 2. Quy chuẩn chung (General Conventions)
- **Định dạng dữ liệu**: `application/json; charset=UTF-8`
- **Mã sinh viên chuẩn PTIT**: Regex `^B\d{2}DC[A-Z]{2}\d{3}$` (Ví dụ: `B22DCCN001`, `B22DCAT015`)
- **Định dạng lỗi chung (Error Response)**:
  ```json
  {
    "status": 400,
    "error": "Bad Request",
    "message": "Chi tiết lỗi",
    "timestamp": "2026-11-22T08:30:00"
  }
  ```

---

### 3. Chi tiết API Finance (`:8082`) - Do Thành viên 2 phụ trách

#### 3.1. Lấy danh sách học phí theo sinh viên
- **Endpoint**: `GET /api/tuitions/{studentId}`
- **Headers**: `Accept: application/json`
- **Path Parameter**: `studentId` (Chuỗi mã sinh viên PTIT)
- **Mã phản hồi**:
  - `200 OK`: Trả về mảng JSON các khoản học phí của sinh viên.
    ```json
    [
      {
        "id": 1,
        "studentId": "B22DCCN001",
        "semester": "2026-1",
        "amount": 8500000,
        "status": "UNPAID",
        "dueDate": "2026-12-15"
      },
      {
        "id": 2,
        "studentId": "B22DCCN001",
        "semester": "2025-2",
        "amount": 8200000,
        "status": "PAID",
        "dueDate": "2026-05-15"
      }
    ]
    ```
  - `400 Bad Request`: Mã sinh viên sai định dạng (ví dụ: `abc123`).
  - `404 Not Found`: Sinh viên đúng mã nhưng chưa có bản ghi học phí.

#### 3.2. Cập nhật trạng thái học phí
- **Endpoint**: `PUT /api/tuitions/{id}/status`
- **Headers**:
  - `Content-Type: application/json`
  - `Accept: application/json`
- **Path Parameter**: `id` (Long - ID khoản học phí)
- **Request Body**:
  ```json
  {
    "status": "PAID"
  }
  ```
  *(Chỉ chấp nhận giá trị `"PAID"` hoặc `"UNPAID"`)*
- **Mã phản hồi**:
  - `200 OK`: Bản ghi học phí sau khi cập nhật thành công.
  - `400 Bad Request`: Trạng thái gửi lên không phải PAID hoặc UNPAID, hoặc thiếu body.
  - `404 Not Found`: Không tìm thấy bản ghi học phí có ID tương ứng.

#### 3.3. Endpoint kiểm thử làm chậm (Test Slow / Timeout)
- **Endpoint**: `GET /api/tuitions/slow?delay={delayMs}`
- **Query Parameter**: `delay` (mili-giây, mặc định 5000)
- **Mã phản hồi**:
  - `200 OK`: Trả về danh sách tất cả học phí sau khi đợi đúng `delay` ms.

---

### 4. Chi tiết API Academic (`:8081`)
- `GET /api/students/{studentId}`: Lấy thông tin sinh viên (200, 400, 404).
- `POST /api/students`: Tạo mới sinh viên (201, 400, 409).

---

### 5. Chi tiết API Portal (`:8080`)
- **Endpoint**: `GET /api/portal/students/{studentId}/summary`
- **Timeout cấu hình**:
  - Academic API: 1000 ms (Dữ liệu thiết yếu)
  - Finance API: 3000 ms (Dữ liệu bổ sung)
- **Mã phản hồi**:
  - `200 OK`: Tổng hợp đầy đủ dữ liệu hoặc suy giảm có kiểm soát (Graceful Degradation).
    ```json
    {
      "student": {
        "studentId": "B22DCCN001",
        "fullName": "Nguyễn Văn An",
        "major": "Công nghệ thông tin",
        "class": "D22CQCN01-B"
      },
      "tuitions": [
        {
          "id": 1,
          "semester": "2026-1",
          "amount": 8500000,
          "status": "UNPAID",
          "dueDate": "2026-12-15"
        }
      ],
      "warnings": []
    }
    ```
    *Khi Finance lỗi hoặc timeout:*
    ```json
    {
      "student": { ... },
      "tuitions": null,
      "warnings": ["Không lấy được học phí do hệ thống Finance không phản hồi"]
    }
    ```
  - `400 Bad Request`: Mã sinh viên sai cú pháp, Portal chặn ngay không gọi Academic hay Finance.
  - `404 Not Found`: Academic trả 404 (Không có sinh viên thì không hiển thị).
  - `503 Service Unavailable`: Academic không phản hồi hoặc timeout (Dữ liệu cốt lõi bị gián đoạn).
