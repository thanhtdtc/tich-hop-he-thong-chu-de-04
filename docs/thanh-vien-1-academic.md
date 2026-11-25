# Phần báo cáo Thành viên 1: Academic API

Tài liệu này là phần nội dung Thành viên 1 bàn giao để ghép vào báo cáo chung. Có thể dùng các mục 1–3 cho Chương 2 (cơ sở lý thuyết), mục 4 cho Chương 4 (cài đặt) và mục 5 cho Chương 5 (kiểm thử). Khi dàn trang, nhóm cần thống nhất font, cỡ chữ, đánh số hình/bảng và bổ sung ảnh minh họa theo yêu cầu nộp bài.

## Chương 2. Cơ sở lý thuyết liên quan

### 2.1. Tích hợp hệ thống và tích hợp qua giao diện ứng dụng

Tích hợp hệ thống là việc kết nối các ứng dụng hoặc dịch vụ độc lập để chúng có thể trao đổi dữ liệu và phối hợp xử lý một quy trình. Trong bài toán này, thông tin học tập và học phí được quản lý bởi hai dịch vụ khác nhau. Người dùng muốn xem chúng trên một cổng duy nhất, do đó Portal cần lấy dữ liệu từ Academic API và Finance API rồi tổng hợp kết quả.

Nhóm sử dụng **Application Interface Integration**: mỗi ứng dụng công bố một giao diện có hợp đồng rõ ràng, bên tiêu thụ gửi yêu cầu qua giao diện đó và nhận phản hồi theo cấu trúc đã thống nhất. Academic API sở hữu dữ liệu sinh viên; Finance API sở hữu dữ liệu học phí; Portal gọi hai API và không đọc trực tiếp database của hai dịch vụ. Mã sinh viên là khóa nghiệp vụ chung để Portal ghép hồ sơ với các khoản học phí.

Hợp đồng API đóng vai trò thỏa thuận giữa bên cung cấp và bên gọi. Hợp đồng quy định endpoint, phương thức HTTP, trường dữ liệu, kiểu dữ liệu, quy tắc kiểm tra và mã trạng thái. Ví dụ, cả nhóm thống nhất rằng mã sinh viên tuân theo `^B\d{2}DC[A-Z]{2}\d{3}$`, trường JSON dùng camelCase, API Academic chạy ở cổng `8081`, và mã sinh viên trùng khi POST trả `409 Conflict`. Nếu một bên tự đổi `studentId` thành `studentCode` mà không cập nhật hợp đồng và các bên còn lại, Portal có thể không đọc được dữ liệu dù hai ứng dụng vẫn hoạt động riêng.

### 2.2. REST API và tài nguyên

REST là phong cách kiến trúc cho dịch vụ web, trong đó dữ liệu được biểu diễn như các tài nguyên được định danh bằng URI. Academic dùng tài nguyên sinh viên tại `/api/students/{studentId}`. Địa chỉ mô tả tài nguyên; HTTP method mô tả hành động mà client muốn thực hiện.

Academic cung cấp hai thao tác chính:

- `GET /api/students/{studentId}` đọc hồ sơ theo mã sinh viên. Đây là thao tác truy vấn, không thay đổi dữ liệu.
- `POST /api/students` nhận hồ sơ JSON và tạo một sinh viên mới.

Request/response sử dụng HTTP. Client gửi method, URL, header và có thể gửi body; server xử lý rồi trả status code, header và body. Ví dụ, khi Portal gửi GET cho `B22DCCN001`, Academic truy vấn bảng `student` và trả hồ sơ JSON cùng trạng thái `200 OK`.

REST hướng tới giao tiếp không lưu trạng thái phiên xử lý giữa các request: mỗi request mang đủ thông tin cần thiết để server xử lý. Academic không dựa vào phiên đăng nhập nội bộ của Portal trong demo này. Việc tách request theo tài nguyên và method làm cho endpoint dễ hiểu, có thể gọi từ Postman, trình duyệt hoặc một ứng dụng khác.

### 2.3. JSON, HTTP status và xử lý lỗi

JSON là định dạng văn bản biểu diễn dữ liệu theo cặp khóa–giá trị và danh sách. Nó độc lập với ngôn ngữ lập trình nên phù hợp để các thành phần Java trao đổi dữ liệu qua HTTP. Hồ sơ Academic dùng các trường `studentId`, `fullName`, `email`, `className`, `major`. Ví dụ:

```json
{
  "studentId": "B22DCCN001",
  "fullName": "Nguyễn Minh An",
  "email": "AnNM.b22cn001@stu.ptit.edu.vn",
  "className": "D22CQCN01-B",
  "major": "Công nghệ thông tin"
}
```

Các trường được thống nhất ở camelCase để response của Academic khớp với DTO mà Portal dùng. API trả `Content-Type: application/json`; văn bản tiếng Việt được truyền bằng UTF-8. Tên thuộc tính, kiểu dữ liệu và cách biểu diễn ngày/số cần ổn định để client ánh xạ kết quả chính xác.

HTTP status diễn tả kết quả ở mức giao thức:

| Mã | Cách dùng trong Academic | Ý nghĩa |
|---:|---|---|
| 200 | GET tìm được hồ sơ | Request được xử lý thành công |
| 201 | POST tạo hồ sơ mới | Tài nguyên mới đã được tạo |
| 400 | Mã sai định dạng hoặc body không hợp lệ | Client cần sửa dữ liệu gửi lên |
| 404 | Mã đúng định dạng nhưng không có trong database | Tài nguyên được yêu cầu không tồn tại |
| 409 | POST với mã đã tồn tại | Request xung đột với dữ liệu hiện tại |

Academic dùng một cấu trúc JSON chung cho lỗi: `status`, `error`, `message`. Ví dụ mã không tồn tại trả `{"status":404,"error":"NOT_FOUND","message":"Không tìm thấy sinh viên B22DCCN999"}`. Client có thể dựa vào status để quyết định xử lý, đồng thời dùng message để hiển thị giải thích cho người dùng. Cần phân biệt `400` với `404`: mã sai định dạng bị từ chối trước khi truy vấn; mã đúng định dạng nhưng không có bản ghi mới là `404`.

### 2.4. Kiểm tra dữ liệu và tính toàn vẹn

Kiểm tra dữ liệu được thực hiện ở tầng API trước khi ghi xuống database. Mã sinh viên phải khớp quy tắc đã thống nhất; các trường bắt buộc không được để trống; email phải có định dạng hợp lệ và không vượt quá giới hạn cột. Việc kiểm tra ở API trả lỗi dễ hiểu cho client. Ràng buộc khóa chính trong PostgreSQL vẫn là lớp bảo vệ cuối cùng khi nhiều request cùng tạo một mã.

Khi mã đã tồn tại, API trả `409 Conflict` thay vì `400`, bởi dữ liệu gửi lên có định dạng hợp lệ nhưng trạng thái tài nguyên hiện tại không cho phép tạo trùng. Repository bắt xung đột khóa chính và chuyển thành lỗi nghiệp vụ để controller advice trả đúng error schema. Cách này giữ lỗi database ở bên trong dịch vụ và không để lộ chi tiết SQL cho client.

### 2.5. Lựa chọn cơ chế tích hợp

| Cách tích hợp | Ý tưởng | Ưu điểm | Hạn chế/rủi ro |
|---|---|---|---|
| Qua API (cách nhóm chọn) | Portal gọi endpoint của Academic và Finance | Ranh giới dịch vụ rõ; database có thể thay đổi nội bộ; có kiểm soát validation và mã lỗi | Phụ thuộc mạng, endpoint và độ sẵn sàng của dịch vụ; cần timeout và xử lý lỗi |
| Đọc trực tiếp database của dịch vụ khác | Portal kết nối vào `academic_db`/`finance_db` và truy vấn bảng | Ít lớp trung gian, có thể thuận tiện cho truy vấn nội bộ nhỏ | Ghép chặt với schema; phải chia sẻ quyền truy cập database; dễ vi phạm sở hữu dữ liệu và khó thay đổi |
| Tích hợp hiển thị tại Portal | Portal tập hợp dữ liệu từ các nguồn rồi trình bày một giao diện | Người dùng có một nơi tra cứu; giảm thao tác giữa nhiều hệ thống | Portal cần gọi nhiều nguồn, quyết định cách xử lý dữ liệu thiếu và không được biến thành nơi lưu bản sao tùy tiện |

Portal là lớp trình bày/tổng hợp, còn kênh trao đổi dữ liệu giữa các dịch vụ vẫn là API. Vì Academic và Finance sở hữu dữ liệu khác nhau, nhóm giữ database riêng và dùng API để bảo toàn ranh giới. Trong demo quy mô nhỏ, chưa cần API Gateway hay message broker; nếu hệ thống lớn hơn, có thể cân nhắc các thành phần này để quản lý xác thực, định tuyến, giới hạn tải và quan sát tập trung.

## Chương 4. Cài đặt Academic API

### 4.1. Thành phần và cấu trúc mã nguồn

Academic API dùng Spring Boot, Spring WebMVC, Spring JDBC, Jakarta Validation và PostgreSQL JDBC driver. Dịch vụ chạy cổng `8081`, database tên `academic_db`. Spring JDBC được dùng để truy vấn bảng trực tiếp bằng tham số hóa SQL; dữ liệu không được ghép chuỗi vào câu truy vấn.

```text
academic-api/
├── src/main/java/com/ptit/integration/academic/
│   ├── AcademicApiApplication.java
│   └── student/
│       ├── StudentController.java
│       ├── StudentService.java
│       ├── StudentRepository.java
│       ├── JdbcStudentRepository.java
│       ├── Student.java
│       ├── CreateStudentRequest.java
│       ├── GlobalExceptionHandler.java
│       └── *Exception.java, ApiError.java
└── src/main/resources/
    ├── application.yaml
    ├── schema.sql
    └── data.sql
```

`application.yaml` nhận URL, username, password từ biến môi trường `ACADEMIC_DB_URL`, `ACADEMIC_DB_USERNAME`, `ACADEMIC_DB_PASSWORD`; mặc định dùng localhost cổng 5432 và database `academic_db`. Khi khởi động, Spring chạy `schema.sql` và `data.sql`. Bảng `student` có `student_id` làm khóa chính; `data.sql` nạp 12 sinh viên giả từ `B22DCCN001` đến `B22DCCN012`. Email giả theo mẫu của nhóm và ngành ghi đầy đủ là Công nghệ thông tin, tương ứng tiền tố `CN` trong mã.

### 4.2. Luồng GET

1. Client gửi `GET /api/students/{studentId}`.
2. `StudentController` chuyển mã cho `StudentService`.
3. Service kiểm tra regex mã sinh viên; nếu sai thì ném lỗi nghiệp vụ `400`.
4. `JdbcStudentRepository` truy vấn theo tham số `student_id = ?`.
5. Nếu tìm được, API trả DTO `Student` với `200`; nếu không, exception handler trả `404` cùng error schema.

### 4.3. Luồng POST

1. Client gửi JSON tới `POST /api/students`.
2. Jakarta Validation kiểm tra trường bắt buộc, email và giới hạn độ dài.
3. Service xác thực lại mã theo contract và chuẩn hóa khoảng trắng đầu/cuối.
4. Repository insert bản ghi vào PostgreSQL.
5. Nếu insert thành công, controller trả `201` và bản ghi vừa tạo; nếu khóa chính đã tồn tại, lỗi được ánh xạ thành `409`.

Các response mẫu:

```http
GET /api/students/B22DCCN001 -> 200
POST /api/students          -> 201
GET /api/students/abc123    -> 400
GET /api/students/B22DCCN999 -> 404
POST mã đã tồn tại          -> 409
```

## Chương 5. Kiểm thử Academic API

Collection Postman nằm trong `postman/academic.postman_collection.json`; bản v3 YAML do Postman Local Mode tạo cũng nằm trong thư mục `postman/Academic API - Chu de 04/`. Các request có script kiểm tra status và một số trường response. API được chạy tại localhost:8081 và kết nối PostgreSQL cục bộ.

| # | Request/đầu vào | Kết quả mong đợi | Kết quả ghi nhận |
|---:|---|---|---|
| 1 | GET `B22DCCN001` | 200 và đủ 5 trường hồ sơ | Đạt; response có thông tin sinh viên |
| 2 | GET `B22DCCN999` | 404, `NOT_FOUND` | Đạt theo lần chạy Postman của thành viên |
| 3 | GET `abc123` | 400, `BAD_REQUEST` | Đạt theo lần chạy Postman của thành viên |
| 4 | POST tạo `B22DCCN013` | 201 và trả bản ghi vừa tạo | Đạt; Postman hiển thị `201` |
| 5 | POST email sai định dạng | 400, `BAD_REQUEST` | Đạt theo lần chạy Postman của thành viên |
| 6 | POST lại `B22DCCN013` | 409, `CONFLICT` | Đạt; response nêu mã đã tồn tại |
| 7 | GET `B22DCCN013` sau khi tạo | 200 và trả hồ sơ đã lưu | Đạt theo lần chạy của thành viên |

Các ca 1, 4 và 6 có response được xác nhận bằng ảnh chụp màn hình trong quá trình làm việc. Nhóm có thể lưu ảnh kiểm thử theo quy ước `A-01-success.png` đến `A-06-duplicate.png` tại `docs/evidence/academic/` nếu cần đưa bằng chứng ảnh vào báo cáo. Ca 7 chứng minh POST ghi dữ liệu vào PostgreSQL và GET đọc lại được từ nguồn lưu trữ, không chỉ trả dữ liệu giả từ bộ nhớ.

### 5.1. Nhận xét

Các endpoint phân biệt được lỗi đầu vào, không tìm thấy tài nguyên và xung đột khóa. PostgreSQL giữ tính duy nhất của mã sinh viên; Portal và các client dùng một định dạng lỗi nhất quán. Bộ dữ liệu giả được nạp lại khi khởi động mà không nhân bản bản ghi do seed dùng `ON CONFLICT (student_id) DO NOTHING`.

Phần kiểm thử tích hợp GET sinh viên mới qua Portal cần chạy sau khi Portal backend triển khai endpoint summary và các thành viên ghép hệ thống. Kiểm thử Academic trực tiếp đã xác nhận việc tạo và đọc lại mã mới; kiểm thử qua Portal là ca phối hợp liên thành phần, không thể kết luận chỉ từ các request Academic.
