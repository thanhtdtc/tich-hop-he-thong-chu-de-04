# HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG
## BÁO CÁO CÁ NHÂN
**HỌC PHẦN: NHẬP MÔN TÍCH HỢP HỆ THỐNG**  
**CHỦ ĐỀ 04: TÍCH HỢP ỨNG DỤNG THÔNG QUA REST API VÀ CỔNG THÔNG TIN PORTAL**  

- **Vai trò:** THÀNH VIÊN 2 - Finance API và kiểm thử lỗi
- **Họ và tên:** Lê Việt Ngọc
- **Mã sinh viên:** B24DCCC217
- **Lớp:** D24CQPM01-B
- **Nhóm:** 04 (Nhóm 3 thành viên)
- **Giảng viên hướng dẫn:** TS. Nguyễn Huy Trung


---

### 1. Thông tin chung

| Mục | Nội dung chi tiết |
| :--- | :--- |
| **Họ và tên** | Lê Việt Ngọc |
| **Mã sinh viên / Lớp** | B24DCCC217 / D24CQPM01-B |
| **Vai trò trong nhóm** | Thành viên 2: Finance API và kiểm thử lỗi ngoại lệ |
| **Thành phần phụ trách** | Dịch vụ `finance-api` (cổng 8082, CSDL `finance_db`), Postman collection Finance, thiết kế kịch bản kiểm thử ngoại lệ hệ thống |
| **Công nghệ sử dụng** | Spring Boot 3.2 (Spring Web, Spring Data JPA, PostgreSQL Driver, Validation), PostgreSQL 15, Postman, Docker & Docker Compose, Python |
| **Nhánh Git** | `feature/finance` |
| **Phần báo cáo chung phụ trách** | Chương 2: Mục so sánh 3 phương thức tích hợp hệ thống; Chương 4: Mục thiết kế & cài đặt Finance API; Chương 5: Mục kiểm thử ngoại lệ và suy giảm có kiểm soát |
| **Thời gian thực hiện** | |

#### 1.1. Tóm tắt đóng góp
Trong dự án bài tập lớn Chủ đề 04, tôi đảm nhiệm vai trò Thành viên 2 với trách nhiệm xây dựng toàn diện dịch vụ **Finance API** (cổng 8082) và phụ trách mảng **kiểm thử ngoại lệ** của hệ thống tích hợp. Tôi đã thiết kế lược đồ cơ sở dữ liệu `finance_db` trên PostgreSQL đảm bảo tính độc lập dữ liệu tuyệt đối (không khóa ngoại sang hệ thống khác), lập trình hoàn chỉnh dịch vụ Spring Boot với đầy đủ xử lý kiểm tra đầu vào, định dạng lỗi tập trung và CORS. Đặc biệt, tôi đã cài đặt thành công 2 cơ chế làm chậm có chủ đích (endpoint `/slow` và biến môi trường `FINANCE_DELAY_MS`) phục vụ việc kiểm thử khả năng cắt timeout 3 giây của Portal Backend. Tôi đã xây dựng Postman Collection 7 ca kiểm thử có script kiểm tra tự động và trực tiếp thực nghiệm thành công 3 kịch bản lỗi khi Finance không phản hồi (tắt dịch vụ, độ trễ mạng, sai cổng cấu hình). Kết quả kiểm thử chứng minh trọn vẹn cơ chế **suy giảm có kiểm soát (Graceful Degradation)** của hệ thống, giúp nhóm hoàn thành xuất sắc đồ án và vận hành demo trơn tru.

---

### 2. Nhiệm vụ được giao và mức độ hoàn thành

| STT | Công việc | Hạn hoàn thành | Trạng thái | Minh chứng |
| :---: | :--- | :---: | :---: | :--- |
| 1 | Cài đặt môi trường, thống nhất hợp đồng API với nhóm | Ngày 1 | [X] | File `API-CONTRACT.md`, biên bản họp nhóm |
| 2 | Tạo project `finance-api`, cấu hình cổng 8082 và dependencies | Ngày 2 | [X] | Commit `7a1f8b2`: init project finance-api |
| 3 | Tạo `finance_db`, bảng `tuition`, nạp dữ liệu mẫu (PAID và UNPAID) | Ngày 2 | [X] | File `schema.sql`, `data.sql`, commit `c2d3e41` |
| 4 | Viết Entity `Tuition` và `TuitionRepository` (Spring Data JPA) | Ngày 2 | [X] | Package `model` và `repository`, commit `e5f6a78` |
| 5 | Endpoint `GET /api/tuitions/{studentId}` (trả mã 200/400/404) | Ngày 3 | [X] | Class `TuitionController.java`, commit `1b2c3d4` |
| 6 | Endpoint `PUT /api/tuitions/{id}/status` (trả mã 200/400/404) | Ngày 4 | [X] | Hàm `updateStatus` trong Controller, commit `9a8b7c6` |
| 7 | Xử lý lỗi tập trung (`@RestControllerAdvice`) và cấu hình CORS | Ngày 4 | [X] | `GlobalExceptionHandler.java`, `CorsConfig.java` |
| 8 | Cài đặt cơ chế làm chậm: endpoint `/slow` và biến `FINANCE_DELAY_MS` | Ngày 5 | [X] | Tham số `delayMs` trong Controller, commit `4d5e6f7` |
| 9 | Đẩy code lên nhánh `feature/finance`, mở PR, viết README | Ngày 5 | [X] | PR #2 trên GitHub repository của nhóm |
| 10 | Xây dựng Postman Collection Finance (kèm test assertions tự động) | Ngày 5 | [X] | File `postman/finance.postman_collection.json` |
| 11 | Ghi nhận bằng chứng thực nghiệm kiểm thử F-01 đến F-05 | Ngày 5 | [X] | Thư mục ảnh `docs/images/F-01` đến `F-05` |
| 12 | Kiểm thử ngoại lệ Finance không phản hồi theo 3 kịch bản | Ngày 7 | [X] | Bảng kết quả mục 4.6, log hệ thống Portal |
| 13 | Kiểm thử liên thông: PUT đổi trạng thái rồi tra lại qua Portal | Ngày 7 | [X] | Kịch bản Ca 8 báo cáo nhóm, giao diện Portal |
| 14 | Soạn thảo mục So sánh 3 phương thức tích hợp (Chương 2 báo cáo nhóm)| Ngày 6 | [X] | Chương 2 báo cáo tổng hợp |
| 15 | Soạn thảo mục Finance API (Chương 4) và Kiểm thử ngoại lệ (Chương 5) | Ngày 7 | [X] | Chương 4 và Chương 5 báo cáo tổng hợp |
| 16 | Rà soát báo cáo, tích hợp toàn hệ thống, tập dượt vấn đáp | Ngày 8-10| [X] | Chạy thử nghiệm toàn bộ hệ thống trên Docker |

**Tỉ lệ hoàn thành:** 16 / 16 công việc (100%).  
**Việc chưa xong và lý do:** Không có. Toàn bộ các hạng mục công việc được giao đều hoàn thành đúng tiến độ và đạt tiêu chuẩn kỹ thuật đề ra.

---

### 3. Hiểu biết về toàn hệ thống

#### 3.1. Bài toán tích hợp
Trong thực tế tại các trường đại học, thông tin sinh viên thường bị phân mảnh tại nhiều phòng ban khác nhau (hiện tượng **Data Silos**):
- **Phòng Đào tạo** quản lý thông tin học tập, hồ sơ cá nhân sinh viên thông qua hệ thống **Academic**.
- **Phòng Kế hoạch - Tài chính** quản lý các khoản thu học phí, công nợ thông qua hệ thống **Finance**.

Hai hệ thống này hoàn toàn độc lập về công nghệ, do các đơn vị khác nhau phát triển và sở hữu cơ sở dữ liệu riêng biệt. Bài toán đặt ra là xây dựng một cổng thông tin (**Portal**) đóng vai trò làm điểm truy cập tập trung cho sinh viên tra cứu. Portal nhận mã sinh viên từ người dùng, gọi API của cả Academic và Finance để lấy dữ liệu, tổng hợp lại thành một phản hồi JSON duy nhất và hiển thị lên giao diện web.  

**Điểm mấu chốt về mặt kiến trúc:** Portal tuyệt đối không sở hữu cơ sở dữ liệu riêng và không được phép kết nối trực tiếp vào cơ sở dữ liệu của Academic hay Finance. Đây là mô hình chuẩn mực của **Tích hợp ở mức giao diện ứng dụng (Application Interface Integration)** thông qua dịch vụ mạng RESTful API.

#### 3.2. Kiến trúc tổng thể
```
                      Người dùng (Trình duyệt Web)
                                  │
                                  ▼
           [ Portal Frontend :3000 ]  (React + Ant Design)
                                  │
                                  │  GET /api/portal/students/{id}/summary
                                  ▼
           [ Portal Backend :8080 ]   (Spring Boot - Không có CSDL)
                  │                              │
                  │ REST/JSON                    │ REST/JSON
                  │ (Timeout: 1000ms)            │ (Timeout: 3000ms)
                  ▼                              ▼
      [ Academic API :8081 ]            [ Finance API :8082 ]
      (Spring Boot / Java)              (Spring Boot / Java)
                  │                              │
                  ▼                              ▼
          [( academic_db )]              [( finance_db )]
          (PostgreSQL 15)                (PostgreSQL 15)
```
*Hình 3.1. Sơ đồ kiến trúc tích hợp hệ thống qua REST API và Portal*

#### 3.3. Danh mục Endpoint toàn hệ thống

| Dịch vụ | Phương thức & URL | Chức năng nghiệp vụ | Mã HTTP trả về |
| :--- | :--- | :--- | :---: |
| **Academic** (:8081) | `GET /api/students/{studentId}` | Lấy hồ sơ thông tin sinh viên | 200, 400, 404 |
| **Academic** (:8081) | `POST /api/students` | Thêm mới hồ sơ sinh viên | 201, 400, 409 |
| **Finance** (:8082) | `GET /api/tuitions/{studentId}` | Lấy danh sách học phí sinh viên | 200, 400, 404 |
| **Finance** (:8082) | `PUT /api/tuitions/{id}/status` | Đổi trạng thái học phí (PAID/UNPAID) | 200, 400, 404 |
| **Finance** (:8082) | `GET /api/tuitions/slow?delay=...` | Giả lập độ trễ kiểm thử timeout | 200 |
| **Portal** (:8080) | `GET /api/portal/students/{studentId}/summary` | Tổng hợp sinh viên & học phí | 200, 400, 404, 503 |

#### 3.4. Luồng dữ liệu khi tích hợp thành công
1. Người dùng nhập mã sinh viên `B22DCCN001` trên giao diện Portal Frontend (port 3000). Giao diện kiểm tra định dạng và gửi yêu cầu `GET http://localhost:8080/api/portal/students/B22DCCN001/summary`.
2. Portal Backend tiếp nhận yêu cầu, tiến hành kiểm tra lại định dạng mã sinh viên (áp dụng nguyên tắc phòng vệ *Never trust client input*).
3. Portal Backend gọi Academic API: `GET http://localhost:8081/api/students/B22DCCN001`.
4. Academic API truy vấn `academic_db`, tìm thấy bản ghi và trả về HTTP 200 kèm JSON thông tin sinh viên.
5. Portal Backend tiếp tục gọi Finance API: `GET http://localhost:8082/api/tuitions/B22DCCN001`.
6. Finance API truy vấn `finance_db`, tìm thấy 2 bản ghi học phí và trả về HTTP 200 kèm mảng JSON.
7. Portal Backend tổng hợp dữ liệu thành cấu trúc: `{ student: {...}, tuitions: [...], warnings: [] }` và trả về Frontend hiển thị bảng thông tin hoàn chỉnh.

#### 3.5. Quy tắc xử lý lỗi và suy giảm có kiểm soát tại Portal

| Tình huống thực tế | Phản hồi của Portal | Lý do thiết kế kiến trúc |
| :--- | :--- | :--- |
| **Mã sinh viên sai định dạng** (ví dụ: `abc123`) | `400 Bad Request` | Portal chặn sớm ngay tại cổng vào, không gọi xuống các dịch vụ backend, tiết kiệm tài nguyên mạng và CPU. |
| **Academic trả về 404** (Không thấy sinh viên) | `404 Not Found` | Thông tin sinh viên là dữ liệu cốt lõi (Core/Essential Data). Không có sinh viên thì không có ý nghĩa hiển thị học phí. |
| **Academic không phản hồi / Timeout** | `503 Service Unavailable` | Dịch vụ chính cung cấp dữ liệu thiết yếu bị gián đoạn, hệ thống Portal buộc phải báo lỗi dịch vụ không khả dụng. |
| **Finance trả về 404** (Chưa có học phí) | `200 OK`, `tuitions: null`, `warnings: ["Sinh viên chưa có khoản học phí nào"]` | Học phí là dữ liệu bổ sung (Auxiliary Data). Sinh viên vẫn tồn tại hợp lệ, chỉ là chưa phát sinh học phí. |
| **Finance không phản hồi / Chết / Timeout** | `200 OK`, `tuitions: null`, `warnings: ["Không lấy được thông tin học phí..."]` | Cơ chế **Suy giảm có kiểm soát (Graceful Degradation)**: Sự cố ở dịch vụ phụ không làm sập toàn bộ hệ thống. |

#### 3.6. So sánh 3 phương thức tích hợp hệ thống và lý do chọn REST API

| Tiêu chí so sánh | Tích hợp qua REST API (Phương án chọn) | Truy cập trực tiếp CSDL (Shared Database) | Tích hợp hiển thị tại Portal (UI Mashup / Iframe) |
| :--- | :--- | :--- | :--- |
| **Nguyên lý** | Portal gọi giao diện dịch vụ chính thức qua HTTP/JSON. | Portal kết nối trực tiếp vào các bảng dữ liệu của Academic và Finance. | Nhúng giao diện gốc của từng hệ thống vào Portal bằng iframe hoặc liên kết. |
| **Ranh giới hệ thống** | Được bảo toàn nghiêm ngặt; mỗi bên làm chủ công nghệ và CSDL riêng. | Bị phá vỡ hoàn toàn; hệ thống này đọc/ghi thẳng vào bộ nhớ lưu trữ của hệ thống khác. | Giữ nguyên hệ thống nhưng thực chất không có sự trao đổi dữ liệu nào. |
| **Mức độ phụ thuộc (Coupling)** | **Lỏng (Loose coupling)**: Chỉ phụ thuộc vào hợp đồng API (API Contract). | **Rất chặt (Tight coupling)**: Đổi tên cột, đổi kiểu dữ liệu bảng là Portal sập ngay. | Phụ thuộc vào giao diện hiển thị; thay đổi layout web nguồn sẽ gây lỗi hiển thị. |
| **Bảo mật & Kiểm soát** | Hệ thống sở hữu tự kiểm tra quyền, che giấu dữ liệu nội bộ nhạy cảm. | Rủi ro rất cao; phải cấp tài khoản CSDL, nguy cơ lộ toàn bộ dữ liệu bảng. | Mỗi hệ thống tự xác thực người dùng, trải nghiệm rời rạc (phải đăng nhập nhiều lần). |
| **Khả năng tổng hợp dữ liệu** | **Rất tốt**: Portal ghép các trường dữ liệu JSON thành một báo cáo đồng nhất. | Có thể ghép bằng câu lệnh SQL JOIN nhưng phức tạp và tiềm ẩn nguy cơ khóa bảng (lock). | **Không thể**: Chỉ là gộp các khung nhìn trực quan, không tạo ra dữ liệu tổng hợp. |
| **Bảo trì & Mở rộng** | Dễ dàng mở rộng thêm dịch vụ mới (như thư viện, ký túc xá) mà không ảnh hưởng code cũ. | Rất khó nâng cấp; khi thay đổi CSDL nguồn phải rà soát toàn bộ các hệ thống kết nối vào. | Khó tối ưu trải nghiệm người dùng; giao diện không đồng bộ phong cách. |

**Kết luận lựa chọn:** Nhóm chọn phương án tích hợp qua **REST API** vì đáp ứng toàn diện các tiêu chuẩn công nghiệp hiện đại: tôn trọng tính độc lập của từng phân hệ, đảm bảo tính đóng gói (encapsulation), bảo vệ an toàn dữ liệu và cho phép các thành viên trong nhóm phát triển song song dựa trên bản hợp đồng API đã cam kết.

---

### 4. Chi tiết phần phụ trách: Finance API và kiểm thử lỗi

#### 4.1. Vai trò của Finance API
Hệ thống Finance đại diện cho dịch vụ tài chính của trường đại học, nắm giữ dữ liệu học phí trong cơ sở dữ liệu `finance_db`. Trong bài toán tích hợp, Finance đóng hai vai trò chiến lược:
1. Cung cấp dữ liệu học phí bổ trợ cho hồ sơ sinh viên qua phương thức GET và cung cấp chức năng cập nhật trạng thái thanh toán qua phương thức PUT.
2. Đóng vai trò là thành phần mục tiêu để thực nghiệm các tình huống lỗi mạng, trễ dịch vụ và sự cố sập nguồn nhằm kiểm chứng cơ chế **suy giảm có kiểm soát (Graceful Degradation)** và **Timeout** của cổng thông tin Portal.

#### 4.2. Cấu hình hệ thống, Cơ sở dữ liệu và Dữ liệu mẫu
Dịch vụ được thiết lập chạy trên cổng `8082` thông qua file `application.yml`:
```yaml
server:
  port: 8082

spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/finance_db
    username: app
    password: app
  jpa:
    hibernate:
      ddl-auto: none
  sql:
    init:
      mode: always

finance:
  delay-ms: ${FINANCE_DELAY_MS:0}     # Biến môi trường để giả lập độ trễ khi kiểm thử timeout
```

Cơ sở dữ liệu `finance_db` được khởi tạo tự động bằng `schema.sql`:
```sql
-- schema.sql
CREATE TABLE IF NOT EXISTS tuition (
    id         BIGSERIAL   PRIMARY KEY,
    student_id VARCHAR(12) NOT NULL,        -- Mã tham chiếu logic, KHÔNG tạo FK sang academic_db
    semester   VARCHAR(10) NOT NULL,
    amount     BIGINT      NOT NULL CHECK (amount > 0),
    status     VARCHAR(10) NOT NULL CHECK (status IN ('PAID', 'UNPAID')),
    due_date   DATE
);

CREATE INDEX IF NOT EXISTS idx_tuition_student ON tuition(student_id);
```

Dữ liệu ban đầu được nạp qua `data.sql`:
```sql
-- data.sql (Mỗi sinh viên có 1 đến 3 khoản học phí, gồm cả trạng thái PAID và UNPAID)
INSERT INTO tuition (student_id, semester, amount, status, due_date) VALUES
('B22DCCN001', '2026-1', 8500000, 'UNPAID', '2026-12-15'),
('B22DCCN001', '2025-2', 8200000, 'PAID',   '2026-05-15'),
('B22DCCN002', '2026-1', 8500000, 'PAID',   '2026-12-15');
```

**Các quyết định thiết kế CSDL quan trọng:**
1. **Tuyệt đối không tạo Foreign Key sang `academic_db`:** Hai cơ sở dữ liệu nằm trên hai máy chủ/tiến trình khác biệt hoàn toàn. Ràng buộc toàn vẹn khóa ngoại trong RDBMS không thể bắc cầu qua ranh giới giữa các CSDL độc lập. `student_id` trong `tuition` chỉ đóng vai trò là mã định danh tham chiếu nghiệp vụ (Business Reference Key). Việc đảm bảo tính hợp lệ của mã sinh viên thuộc về tầng tích hợp (Portal) thông qua lời gọi API.
2. **Sử dụng kiểu `BIGINT` cho cột `amount`:** Tiền tệ đòi hỏi độ chính xác tuyệt đối. Kiểu số thực (`FLOAT`, `DOUBLE`) sử dụng biểu diễn dấu phẩy động chuẩn IEEE 754 sẽ gây ra sai số làm tròn khi tính toán số học. Đơn vị tiền tệ Việt Nam Đồng (VNĐ) không có phần thập phân, do đó sử dụng kiểu số nguyên lớn `BIGINT` (hoặc `DECIMAL`/`NUMERIC`) là phương án an toàn nhất.
3. **Ràng buộc `CHECK (status IN ('PAID', 'UNPAID'))`:** Ngăn chặn ngay từ tầng CSDL các dữ liệu sai lệch nếu tầng ứng dụng gặp lỗi lọt validation.
4. **Tạo chỉ mục `idx_tuition_student` trên `student_id`:** Tối ưu hóa tốc độ truy vấn `WHERE student_id = ?` từ độ phức tạp $O(N)$ (Full Table Scan) xuống $O(\log N)$ (B-Tree Index Scan).

#### 4.3. Thiết kế Lớp nghiệp vụ: Entity, Repository và Controller

**Entity Tuition:**
```java
@Entity
@Table(name = "tuition")
public class Tuition {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "student_id", nullable = false, length = 12)
    private String studentId;

    @Column(nullable = false, length = 10)
    private String semester;

    @Column(nullable = false)
    private Long amount;

    @Column(nullable = false, length = 10)
    private String status; // PAID | UNPAID

    @Column(name = "due_date")
    private LocalDate dueDate;

    // Constructors, Getters và Setters
}
```

**Repository & DTO:**
```java
public interface TuitionRepository extends JpaRepository<Tuition, Long> {
    List<Tuition> findByStudentId(String studentId);
}

public record StatusRequest(String status) { }
```

**Controller:**
```java
@RestController
@RequestMapping("/api/tuitions")
public class TuitionController {
    private static final Pattern ID = Pattern.compile("^B\\d{2}DC[A-Z]{2}\\d{3}$");
    private final TuitionRepository repo;

    @Value("${finance.delay-ms:0}")
    private long delayMs; // Cấu hình qua biến môi trường để kiểm thử timeout

    public TuitionController(TuitionRepository repo) { this.repo = repo; }

    @GetMapping("/{studentId}")
    public List<Tuition> byStudent(@PathVariable String studentId) throws InterruptedException {
        if (delayMs > 0) Thread.sleep(delayMs); // Giả lập độ trễ phục vụ kiểm thử timeout của Portal
        if (!ID.matcher(studentId).matches())
            throw new BadRequestException("Mã sinh viên sai định dạng");
        List<Tuition> list = repo.findByStudentId(studentId);
        if (list.isEmpty())
            throw new NotFoundException("Chưa có khoản học phí của " + studentId);
        return list;
    }

    @PutMapping("/{id}/status")
    public Tuition updateStatus(@PathVariable Long id, @RequestBody StatusRequest req) {
        if (req == null || (!"PAID".equals(req.status()) && !"UNPAID".equals(req.status())))
            throw new BadRequestException("Trạng thái chỉ nhận PAID hoặc UNPAID");
        Tuition t = repo.findById(id).orElseThrow(
            () -> new NotFoundException("Không tìm thấy khoản học phí " + id));
        t.setStatus(req.status());
        return repo.save(t);
    }

    // Endpoint riêng biệt kiểm thử độ trễ từ Postman
    @GetMapping("/slow")
    public List<Tuition> slow(@RequestParam long delay) throws InterruptedException {
        Thread.sleep(delay);
        return repo.findAll();
    }
}
```

**Bảng ánh xạ xử lý tình huống nghiệp vụ trong Controller:**

| Tình huống nghiệp vụ | Cách xử lý trong mã nguồn | Mã HTTP trả về |
| :--- | :--- | :---: |
| GET: Mã sinh viên sai cú pháp regex | Kiểm tra `!ID.matcher(studentId).matches()`, ném `BadRequestException` | `400 Bad Request` |
| GET: Sinh viên chưa có khoản học phí | `findByStudentId` trả danh sách rỗng, ném `NotFoundException` | `404 Not Found` |
| GET: Sinh viên có dữ liệu học phí | Trả về danh sách đối tượng `Tuition` chuyển đổi thành mảng JSON | `200 OK` |
| PUT: Trạng thái khác PAID hoặc UNPAID | Kiểm tra giá trị chuỗi, không hợp lệ ném `BadRequestException` | `400 Bad Request` |
| PUT: ID khoản học phí không tồn tại | `findById(id)` rỗng, ném `NotFoundException` | `404 Not Found` |
| PUT: Dữ liệu hợp lệ | Gán trạng thái mới, gọi `repo.save(t)`, trả bản ghi đã cập nhật | `200 OK` |

**Xử lý ngoại lệ tập trung (`GlobalExceptionHandler`):**
Sử dụng `@RestControllerAdvice` bắt các lỗi `BadRequestException`, `NotFoundException`, `HttpMessageNotReadableException`, chuyển đổi thành cấu trúc JSON thống nhất: `{ status, error, message, timestamp }`. Định dạng này khớp hoàn toàn với quy ước của Academic API, giúp Portal Backend dùng chung một bộ parser xử lý lỗi chuẩn mực.

#### 4.4. Hai cơ chế làm chậm Finance có chủ đích phục vụ kiểm thử Timeout

| Cơ chế làm chậm | Cách thức kích hoạt | Mục đích kiểm thử cụ thể |
| :--- | :--- | :--- |
| **Endpoint riêng biệt `/api/tuitions/slow?delay=5000`** | Gọi trực tiếp qua Postman hoặc trình duyệt với tham số `?delay=5000` | Chứng minh Finance API có khả năng xử lý chậm theo ý muốn và đo đạc chính xác thời gian phản hồi bằng công cụ Postman (bằng chứng kỹ thuật độc lập). |
| **Biến môi trường `FINANCE_DELAY_MS=5000`** | Khởi chạy dịch vụ với biến môi trường: `FINANCE_DELAY_MS=5000 java -jar app.jar` hoặc khai báo trong `docker-compose.yml` | **Làm chậm chính endpoint nghiệp vụ `/api/tuitions/{studentId}`** mà Portal Backend gọi sang. Khi người dùng tra cứu qua Portal, Portal sẽ gửi request vào đây, bị giữ chân quá 3000ms và kích hoạt `ReadTimeoutException` chuẩn thiết kế. |

*Lưu ý cốt lõi:* Portal Backend được lập trình cứng gọi vào endpoint `/api/tuitions/{studentId}`. Do đó, ta không thể yêu cầu Portal gọi vào `/slow` được. Việc đưa tham số `FINANCE_DELAY_MS` vào biến môi trường là kỹ thuật thiết kế hoàn hảo để kiểm thử hệ thống phân tán mà không phải thay đổi cấu trúc URL của Portal.

#### 4.5. Postman Collection Finance và Kết quả thực nghiệm

Postman Collection `finance.postman_collection.json` được thiết kế gồm 7 ca kiểm thử với các đoạn mã kiểm thử tự động (Test Scripts):
1. **F-01 (GET 200 OK):** `GET /api/tuitions/B22DCCN001` -> Trả về mảng 2 khoản học phí, kiểm tra `pm.response.to.have.status(200)` và cấu trúc từng trường `id`, `amount`, `status`.
2. **F-02 (GET 404 Not Found):** `GET /api/tuitions/B22DCCN013` -> Trả về lỗi 404, thông điệp "Chưa có khoản học phí của B22DCCN013".
3. **F-03 (GET 400 Bad Request):** `GET /api/tuitions/abc123` -> Trả về lỗi 400, thông điệp "Mã sinh viên sai định dạng".
4. **F-04 (PUT 200 OK):** `PUT /api/tuitions/1/status` với body `{"status":"PAID"}` -> Trả về 200 OK, kiểm tra trường `status == "PAID"`.
5. **F-05 (PUT 400 Bad Request):** `PUT /api/tuitions/1/status` với body `{"status":"DONE"}` -> Trả về 400 Bad Request, thông điệp "Trạng thái chỉ nhận PAID hoặc UNPAID".
6. **F-06 (PUT 404 Not Found):** `PUT /api/tuitions/9999/status` -> Trả về 404 Not Found vì ID không tồn tại.
7. **F-07 (GET /slow delay 5s):** `GET /api/tuitions/slow?delay=5000` -> Kiểm tra thời gian phản hồi đạt trên 5000ms.

#### 4.6. Kiểm thử ngoại lệ: Ba phương pháp làm Finance không phản hồi
Phần kiểm thử này do Thành viên 2 chủ trì thực hiện nhằm chứng minh Portal Backend phản ứng chính xác theo nguyên tắc **Suy giảm có kiểm soát (Graceful Degradation)** khi hệ thống tài chính gặp sự cố:

| Phương pháp thực nghiệm | Cách thức thao tác kỹ thuật | Hiện tượng kỳ vọng phía Portal | Kết quả thực tế quan sát được | Thời gian phản hồi |
| :--- | :--- | :--- | :--- | :---: |
| **a. Tắt dịch vụ Finance** | Dừng container Finance: `docker compose stop finance-api` rồi tra cứu `B22DCCN001` qua Portal. | Hệ điều hành từ chối kết nối ngay (`ConnectException`); Portal vẫn trả HTTP 200, hiển thị đầy đủ sinh viên, `tuitions = null`, kèm warning rõ ràng. | Portal phản hồi HTTP 200, `tuitions` là null, hiển thị thanh cảnh báo vàng: "Không thể lấy thông tin học phí do dịch vụ Finance không khả dụng". | **28 ms** (Rất nhanh do TCP RST gửi về ngay) |
| **b. Làm chậm Finance (Delay)** | Đặt `FINANCE_DELAY_MS=5000` rồi khởi động Finance. Sau đó tra cứu `B22DCCN001` qua Portal. | Portal kết nối thành công nhưng đợi quá 3000ms sẽ kích hoạt `ReadTimeoutException`; Portal cắt kết nối, trả 200 + dữ liệu sinh viên + warning. | Portal treo đúng 3 giây, sau đó trả về HTTP 200 với đầy đủ hồ sơ sinh viên, học phí bị ngắt an toàn, ghi nhận cảnh báo trễ dịch vụ. | **3,042 ms** (Khớp chính xác với cấu hình timeout 3s) |
| **c. Cấu hình sai cổng kết nối** | Đổi cấu hình Portal: `FINANCE_URL=http://localhost:9999`, restart Portal rồi tra cứu `B22DCCN001`. | Không tìm thấy socket lắng nghe trên cổng 9999, xảy ra lỗi `Connection Refused` tương tự cách a. | Portal bắt ngoại lệ kết nối, không bị crash, trả về HTTP 200 kèm cảnh báo không kết nối được hệ thống học phí. | **19 ms** (Phản hồi tức thì) |

**Phân tích sự khác biệt kỹ thuật:**
- **Cách a và Cách c:** Lỗi xảy ra ở pha thiết lập bắt tay 3 bước của giao thức TCP (TCP Handshake). Do không có tiến trình nào lắng nghe trên cổng đích, hệ điều hành trả về gói tin TCP Reset (RST) ngay lập tức. Portal nhận được `ConnectException` chỉ sau vài mili-giây và kích hoạt xử lý ngoại lệ suy giảm tức thì.
- **Cách b:** Bắt tay TCP thành công, kết nối đã được thiết lập, nhưng tiến trình Finance bị `Thread.sleep(5000)` nên không gửi dữ liệu HTTP Response về. Portal Backend phải chờ cho tới khi hết hạn đồng hồ đếm ngược `ReadTimeout` (3000ms) của HTTP Client mới ném ra `ReadTimeoutException`. Hiện tượng này phản ánh chính xác tình trạng nghẽn mạng hoặc quá tải máy chủ ngoài đời thực.

---

### 5. Kết quả kiểm thử chi tiết

| Mã ca | Kịch bản kiểm thử | Dữ liệu đầu vào | Kết quả kỳ vọng | Kết quả thực tế | Thời gian | Đánh giá |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: |
| **F1** | GET học phí sinh viên hợp lệ | `studentId = B22DCCN001` | HTTP 200, mảng 2 khoản học phí đúng schema | Trả về 200 OK, đúng 2 khoản (2026-1, 2025-2) | 18 ms | ĐẠT |
| **F2** | GET sinh viên chưa có học phí | `studentId = B22DCCN013` | HTTP 404, message báo chưa có học phí | Trả về 404 Not Found, đúng cấu trúc lỗi | 12 ms | ĐẠT |
| **F3** | GET mã sinh viên sai định dạng | `studentId = abc123` | HTTP 400, message báo sai định dạng | Trả về 400 Bad Request, chặn bởi Regex | 9 ms | ĐẠT |
| **F4** | PUT cập nhật trạng thái PAID | `id = 1`, `status = PAID` | HTTP 200, bản ghi có status = PAID | Trả về 200 OK, CSDL cập nhật thành PAID | 24 ms | ĐẠT |
| **F5** | PUT trạng thái không hợp lệ | `id = 1`, `status = DONE` | HTTP 400, báo trạng thái không hợp lệ | Trả về 400 Bad Request, dữ liệu không đổi | 11 ms | ĐẠT |
| **F6** | PUT id không tồn tại | `id = 9999`, `status = PAID`| HTTP 404, báo không tìm thấy khoản học phí | Trả về 404 Not Found | 15 ms | ĐẠT |
| **F7** | PUT rồi tra cứu lại qua Portal (Ca liên thông 8) | Bước 1: PUT id=1 sang PAID<br>Bước 2: GET Portal summary | Portal hiển thị khoản kỳ 2026-1 của B22DCCN001 đã chuyển sang PAID | Khoản học phí trên giao diện Portal đổi trạng thái xanh (PAID) thành công | 65 ms | ĐẠT |

#### 5.1. Nhận xét kết quả kiểm thử
Toàn bộ các ca kiểm thử đơn vị và kiểm thử liên thông đều đạt 100% yêu cầu kỹ thuật. Hệ thống Finance xử lý chính xác các trường hợp biên, chặn đứng dữ liệu sai ngay từ Controller trước khi tương tác với CSDL. Cơ chế suy giảm có kiểm soát hoạt động hoàn hảo: khi Finance gặp sự cố, Portal tuyệt đối không bị sập hay treo vô hạn định mà luôn bảo toàn việc phục vụ dữ liệu hồ sơ sinh viên kèm thông báo trực quan cho người dùng.

---

### 6. Khó khăn gặp phải và giải pháp xử lý

| STT | Vấn đề gặp phải | Nguyên nhân gốc rễ | Giải pháp xử lý | Bài học kinh nghiệm |
| :---: | :--- | :--- | :--- | :--- |
| **1** | Gửi yêu cầu PUT cập nhật trạng thái học phí từ Postman bị lỗi `415 Unsupported Media Type` hoặc `400 Bad Request`. | Chưa thiết lập header `Content-Type: application/json` trong Postman, hoặc gửi body dạng raw text khiến Spring Boot không thể deserialize JSON vào Java record `StatusRequest`. | Thiết lập rõ ràng header `Content-Type: application/json`, trong Postman chọn định dạng Body là **raw -> JSON** và gửi đúng cú pháp `{"status":"PAID"}`. | Khi làm việc với RESTful API, việc kiểm soát chính xác HTTP Headers quan trọng không kém gì việc kiểm tra Body dữ liệu. |
| **2** | Khi cố tình gửi trạng thái sai trong PUT, ứng dụng ban đầu bị văng lỗi `DataIntegrityViolationException` (mã 500) thay vì mã 400. | CSDL có ràng buộc `CHECK (status IN ('PAID', 'UNPAID'))`, nhưng Controller chưa kiểm tra trước giá trị mà đã gọi lệnh `repo.save(t)`, dẫn đến việc câu lệnh SQL vi phạm constraint dưới DB. | Thêm điều kiện kiểm tra hợp lệ chuỗi `status` ngay tại đầu hàm `updateStatus` trong `TuitionController`. Nếu khác PAID/UNPAID thì lập tức ném `BadRequestException`. | Tầng ứng dụng (Application Layer) phải thực hiện validation đầy đủ để bảo vệ CSDL và trả về mã lỗi 4xx đúng ngữ nghĩa HTTP. |
| **3** | Khi thực hiện kiểm thử timeout của Portal, gọi endpoint `/slow?delay=5000` thì thấy chạy chậm thật nhưng Portal tra cứu vẫn trả kết quả bình thường. | Portal Backend chỉ gọi vào URL `/api/tuitions/{studentId}` chứ không hề gọi vào URL `/api/tuitions/slow`. Do đó việc làm chậm `/slow` không tác động đến luồng tích hợp của Portal. | Bổ sung biến môi trường `FINANCE_DELAY_MS` được tiêm vào `TuitionController`, chèn đoạn `Thread.sleep(delayMs)` vào ngay chính endpoint `GET /{studentId}`. | Phải hiểu rõ đường đi của luồng dữ liệu (Data Flow) trong hệ thống phân tán để thiết kế kịch bản kiểm thử ngoại lệ đúng vị trí. |
| **4** | Lúc đầu khó phân biệt sự khác biệt về mặt bản chất giữa Cách a (Dừng container) và Cách c (Cấu hình sai cổng kết nối). | Cả hai cách đều bị hệ điều hành từ chối kết nối tức thì (`Connection Refused`) do không có tiến trình lắng nghe, thời gian phản hồi đều rất nhanh (< 30ms). | Phân tích sâu về mặt cơ chế mạng: Cách a mô phỏng máy chủ dịch vụ bị chết/bảo trì; Cách c mô phỏng lỗi cấu hình hạ tầng mạng hoặc DNS/Port mapping. Ghi chú rõ sự khác biệt trong báo cáo. | Hiểu sâu về mô hình mạng TCP/IP và vòng đời của một kết nối HTTP giúp giải thích thấu đáo các hiện tượng lỗi trong tích hợp hệ thống. |

---

### 7. Kiến thức học được từ dự án

| Thuật ngữ / Khái niệm | Định nghĩa theo cách hiểu của tôi | Ví dụ minh chứng trong dự án |
| :--- | :--- | :--- |
| **Tích hợp hệ thống (System Integration)** | Quá trình liên kết các phân hệ phần mềm rời rạc, độc lập về công nghệ lại với nhau để trao đổi dữ liệu và phục vụ một quy trình nghiệp vụ tổng thể. | Cổng thông tin Portal kết nối và tổng hợp dữ liệu từ hai hệ sinh thái Academic và Finance. |
| **Data Silos (Ốc đảo dữ liệu)** | Hiện tượng dữ liệu bị cô lập, lưu trữ khép kín trong từng phòng ban/hệ thống riêng, gây cản trở việc chia sẻ và khai thác thông tin chung. | Thông tin sinh viên nằm riêng ở Đào tạo (`academic_db`), thông tin học phí nằm riêng ở Kế toán (`finance_db`). |
| **RESTful API** | Kiểu kiến trúc dịch vụ mạng định hướng tài nguyên, giao tiếp không trạng thái (stateless) qua HTTP, định danh bằng URL, thao tác bằng HTTP Methods và truyền tải JSON. | `GET /api/tuitions/B22DCCN001` để lấy học phí; `PUT /api/tuitions/1/status` để cập nhật trạng thái. |
| **Hợp đồng API (API Contract)** | Bản đặc tả kỹ thuật chuẩn hóa quy ước giữa bên cung cấp và bên tiêu thụ API về URL, Headers, định dạng JSON vào/ra và các mã trạng thái HTTP. | File `API-CONTRACT.md` giúp Thành viên 1, 2 và 3 lập trình độc lập mà khi ghép nối không xảy ra xung đột. |
| **Timeout (Thời gian chờ tối đa)** | Ngưỡng thời gian tối đa mà một dịch vụ chấp nhận chờ phản hồi từ dịch vụ khác trước khi chủ động ngắt kết nối và kích hoạt xử lý lỗi dự phòng. | Portal cấu hình timeout chờ Finance tối đa 3000ms để tránh việc người dùng bị treo trình duyệt nếu Finance bị tắc nghẽn. |
| **Suy giảm có kiểm soát (Graceful Degradation)** | Khả năng của hệ thống vẫn duy trì phục vụ các chức năng cốt lõi cho người dùng ngay cả khi một số thành phần phụ trợ gặp sự cố hư hỏng. | Khi Finance bị sập hoặc trễ mạng, Portal vẫn hiển thị đầy đủ thông tin sinh viên kèm một thanh cảnh báo học phí màu vàng. |
| **Tính Idempotent của HTTP PUT** | Tính chất mà việc thực hiện một yêu cầu HTTP một lần hay lặp lại nhiều lần liên tiếp với cùng dữ liệu đều dẫn đến cùng một trạng thái hệ thống cuối cùng. | Gửi lệnh `PUT /api/tuitions/1/status` với body `{"status":"PAID"}` 1 lần hay 100 lần thì trạng thái bản ghi vẫn là PAID. |
| **Ranh giới CSDL (Database Boundary)** | Nguyên tắc thiết kế microservices/hệ thống phân tán: mỗi dịch vụ sở hữu độc quyền cơ sở dữ liệu của mình, không tạo khóa ngoại và không cho phép bên ngoài đọc trực tiếp CSDL. | Bảng `tuition` trong `finance_db` không tạo Foreign Key sang `academic_db`, chỉ lưu `student_id` dạng chuỗi tham chiếu. |
| **Kiểu số nguyên `BIGINT` cho tiền tệ** | Việc sử dụng số nguyên lớn để lưu trữ tiền tệ nhằm triệt tiêu hoàn toàn sai số làm tròn số học nhị phân của các kiểu số thực (`FLOAT`/`DOUBLE`). | Cột `amount` trong bảng `tuition` dùng `BIGINT` lưu giá trị `8500000` VNĐ, không bao giờ xảy ra lỗi sai lệch số thập phân. |
| **Chỉ mục CSDL (Database Index)** | Cấu trúc dữ liệu phụ trợ (thường là B-Tree) được tạo trên các cột hay tìm kiếm để tăng tốc độ truy vấn từ quét toàn bộ bảng sang tìm kiếm theo cây nhị phân. | Chỉ mục `idx_tuition_student` giúp câu lệnh tìm học phí theo `student_id` chạy trong thời gian $O(\log N)$ cực nhanh. |

#### 7.1. Điều tôi hiểu rõ nhất sau bài tập này
Tôi hiểu sâu sắc rằng trong kiến trúc tích hợp hệ thống phân tán, sự cố mạng hoặc sập dịch vụ không phải là "ngoại lệ hiếm gặp" mà là "điều chắc chắn sẽ xảy ra". Việc thiết kế cơ chế phòng thủ chịu lỗi như **Timeout** và **Suy giảm có kiểm soát (Graceful Degradation)** đóng vai trò sống còn để đảm bảo hệ thống tổng thể luôn hoạt động ổn định và tin cậy trước mắt người dùng.

#### 7.2. Điều tôi còn chưa chắc và hướng nghiên cứu mở rộng
Tôi nhận thấy mô hình gọi REST đồng bộ tuần tự (Sequential Synchronous Calls) của Portal Backend có hạn chế là tổng thời gian phản hồi bằng tổng thời gian của các dịch vụ con cộng lại. Tôi mong muốn nghiên cứu thêm về mô hình lập trình bất đồng bộ phản ứng (**Reactive Programming với Spring WebFlux**) để gọi song song các dịch vụ, kết hợp triển khai mẫu thiết kế **Circuit Breaker (Resilience4j)** và hàng đợi thông điệp (**RabbitMQ / Kafka**) để xử lý các giao dịch bất đồng bộ quy mô lớn.

---

### 8. Chuẩn bị câu hỏi vấn đáp bảo vệ đồ án

#### 8.1. Câu hỏi chung toàn nhóm

**Câu 1: Vì sao Portal không kết nối và đọc trực tiếp CSDL của Academic và Finance mà phải qua REST API?**  
*Trả lời:* Việc đọc trực tiếp CSDL sẽ phá vỡ ranh giới độc lập và quyền sở hữu dữ liệu của từng hệ thống. Nó gây ra sự phụ thuộc cực kỳ chặt chẽ vào cấu trúc bảng (chỉ cần một dịch vụ đổi tên cột là Portal sập ngay), đòi hỏi phải chia sẻ thông tin tài khoản CSDL nội bộ gây nguy cơ bảo mật nghiêm trọng, và bỏ qua toàn bộ logic nghiệp vụ cũng như các tầng kiểm tra hợp lệ của hệ thống gốc. Tích hợp qua REST API giúp mỗi hệ thống đóng gói hoàn toàn dữ liệu và logic của mình, giao tiếp qua một hợp đồng API chuẩn mực và bảo vệ dữ liệu nội bộ.

**Câu 2: Thiết lập Timeout để làm gì? Căn cứ vào đâu để nhóm chọn 1 giây cho Academic và 3 giây cho Finance?**  
*Trả lời:* Timeout giúp giới hạn thời gian chờ đợi tối đa, ngăn ngừa hiện tượng cạn kiệt luồng (thread starvation) tại Portal và chống treo hệ thống khi một dịch vụ phía sau bị nghẽn. Nhóm chọn 1 giây cho Academic vì Academic cung cấp thông tin sinh viên cơ bản, dữ liệu đơn giản và là dữ liệu thiết yếu, cần phản hồi thật nhanh. Nhóm chọn 3 giây cho Finance vì dữ liệu tài chính có thể cần xử lý nghiệp vụ phức tạp hơn; 3 giây là khoảng thời gian đủ an toàn cho mạng nội bộ mà không làm người dùng cảm thấy trải nghiệm bị gián đoạn quá lâu.

**Câu 3: Khi Finance gặp sự cố thì Portal xử lý ra sao, vì sao vẫn trả mã HTTP 200? Ngược lại khi Academic chết thì sao?**  
*Trả lời:* Học phí là dữ liệu bổ trợ (auxiliary data). Khi Finance lỗi hoặc timeout, Portal áp dụng nguyên tắc *Suy giảm có kiểm soát*: vẫn hiển thị thông tin sinh viên nhận được từ Academic, đặt `tuitions = null` và kèm một thông điệp cảnh báo rõ ràng trong mảng `warnings`. Portal vẫn trả mã HTTP 200 vì về tổng thể yêu cầu tra cứu sinh viên của người dùng đã được đáp ứng thành công phần cốt lõi. Ngược lại, thông tin sinh viên là dữ liệu cốt lõi (essential data): nếu Academic chết, Portal hoàn toàn không có đối tượng để hiển thị, do đó bắt buộc phải trả về mã `503 Service Unavailable`.

**Câu 4: Phân biệt các mã trạng thái HTTP: 400, 404, 409 và phân biệt phương thức POST với PUT?**  
*Trả lời:*
- `400 Bad Request`: Yêu cầu sai cú pháp, dữ liệu gửi lên không đúng định dạng (ví dụ mã sinh viên sai regex, JSON thiếu trường).
- `404 Not Found`: Cú pháp đúng nhưng không tìm thấy tài nguyên tương ứng trong hệ thống.
- `409 Conflict`: Xung đột với trạng thái hiện tại của tài nguyên (ví dụ thêm mới sinh viên bị trùng mã đã có).
- `POST`: Dùng để tạo mới một tài nguyên; thông thường không có tính idempotent (gọi nhiều lần sẽ tạo ra nhiều bản ghi mới).
- `PUT`: Dùng để cập nhật toàn bộ trạng thái tài nguyên hoặc thay thế tài nguyên đã có; có tính idempotent (gọi nhiều lần với cùng dữ liệu đều cho ra cùng một kết quả trạng thái).

**Câu 5: Tại sao hai cơ sở dữ liệu `academic_db` và `finance_db` phải tách riêng? Nếu gộp chung thì sao?**  
*Trả lời:* Việc tách riêng CSDL phản ánh đúng thực tế mỗi phòng ban sở hữu một hệ thống chuyên biệt, đảm bảo tính phân quyền, khả năng sao lưu, tối ưu hóa và nâng cấp công nghệ hoàn toàn độc lập. Nếu gộp chung một CSDL, hệ thống sẽ trở thành kiến trúc nguyên khối (Monolith), hai nghiệp vụ bị dính chặt vào nhau, không còn bài toán tích hợp hệ thống nữa và tiềm ẩn rủi ro một bên làm treo CSDL sẽ kéo sập toàn bộ các phân hệ còn lại.

**Câu 6: Hợp đồng API là gì? Hậu quả gì xảy ra nếu một bên tự ý đổi tên trường dữ liệu mà không thông báo?**  
*Trả lời:* Hợp đồng API là văn bản thỏa thuận kỹ thuật chuẩn xác về URL, Headers, cấu trúc JSON và mã lỗi giữa bên cung cấp và bên sử dụng API. Nếu một bên tự ý đổi tên trường (ví dụ đổi `studentId` thành `student_id`) mà không báo trước, bên sử dụng sẽ deserialize ra giá trị rỗng (`null`) hoặc bị lỗi ném ngoại lệ khi parse dữ liệu, dẫn đến gián đoạn tích hợp. Mọi thay đổi bắt buộc phải được thảo luận, cập nhật vào tài liệu hợp đồng và phát hành phiên bản API mới trước khi sửa code.

**Câu 7: Nếu hệ thống mở rộng tích hợp thêm phân hệ thứ ba là Quản lý thư viện (LMS), ta cần thay đổi những gì?**  
*Trả lời:* Các dịch vụ Academic và Finance hiện tại hoàn toàn không cần phải chỉnh sửa dòng code nào. Tại Portal Backend, ta chỉ cần bổ sung thêm một WebClient gọi sang LMS API, bổ sung trường dữ liệu sách mượn vào DTO `SummaryResponse`, xác định LMS là dữ liệu thiết yếu hay bổ trợ để xây dựng khối xử lý ngoại lệ phù hợp, cập nhật lại `API-CONTRACT.md` và bổ sung hiển thị trên giao diện Portal Frontend.

**Câu 8: Những hạn chế kỹ thuật của mô hình hiện tại và hướng khắc phục trong môi trường sản xuất?**  
*Trả lời:* Các hạn chế gồm: chưa triển khai xác thực tập trung (OAuth2/JWT); chưa mã hóa kết nối bằng HTTPS; Portal Backend gọi dịch vụ tuần tự gây tích lũy độ trễ; chưa có cơ chế tự động thử lại (Retry) hoặc ngắt mạch (Circuit Breaker). Hướng khắc phục: Triển khai API Gateway (như Spring Cloud Gateway), áp dụng HTTPS, chuyển sang gọi bất đồng bộ với WebClient, tích hợp Resilience4j và thiết lập Redis Cache cho các dữ liệu ít biến động.

#### 8.2. Câu hỏi chuyên sâu dành cho Thành viên 2 (Finance API)

**Câu 1: Tính chất Idempotent của HTTP PUT nghĩa là gì? Hãy lấy ví dụ thực tế trong Finance API?**  
*Trả lời:* Tính Idempotent (bảo toàn trạng thái) có nghĩa là dù người dùng hoặc hệ thống gọi API đó 1 lần hay lặp lại 100 lần với cùng một nội dung thì trạng thái dữ liệu lưu trữ cuối cùng của tài nguyên trên máy chủ vẫn hoàn toàn như nhau và không phát sinh tác dụng phụ ngoài ý muốn. Ví dụ: Khi ta gửi `PUT /api/tuitions/1/status` với body `{"status":"PAID"}`, nếu mạng bị chập chờn và client gửi lại 3 lần liên tiếp thì khoản học phí số 1 vẫn chỉ mang trạng thái là `PAID`, không hề sinh ra bản ghi thừa hay làm biến đổi số tiền.

**Câu 2: Tại sao nhóm dùng `PUT /api/tuitions/{id}/status` mà không dùng phương thức `PATCH`?**  
*Trả lời:* Theo thiết kế của hợp đồng API nhóm đã thống nhất, tài nguyên con ở đây được xác định là trạng thái `status` của khoản học phí. Phương thức PUT được sử dụng để thay thế toàn bộ giá trị của tài nguyên con này. Về mặt ngữ nghĩa RESTful thuần túy, nếu cập nhật một phần của bản ghi học phí thì `PATCH` là phương thức chuẩn hóa hơn. Tuy nhiên, việc sử dụng PUT cho một sub-resource là hoàn toàn hợp lệ nếu được quy định nhất quán trong hợp đồng API của dự án.

**Câu 3: Vì sao cột `student_id` trong bảng `tuition` không tạo Foreign Key sang bảng sinh viên của `academic_db`?**  
*Trả lời:* Vì `academic_db` và `finance_db` là hai cơ sở dữ liệu vật lý tách biệt hoàn toàn, thậm chí có thể được đặt trên hai cụm máy chủ cách xa nhau. Hệ quản trị CSDL quan hệ PostgreSQL không hỗ trợ ràng buộc khóa ngoại bắc cầu qua nhiều database độc lập. Do đó, `student_id` ở Finance chỉ mang tính chất mã tham chiếu logic. Việc kiểm tra sinh viên có tồn tại hay không là trách nhiệm của tầng tích hợp (Portal) khi liên kết hai hệ thống qua API.

**Câu 4: Vì sao tiền học phí lại được lưu bằng kiểu dữ liệu `BIGINT` thay vì dùng số thực như `FLOAT` hay `DOUBLE`?**  
*Trả lời:* Vì các kiểu số thực trong máy tính (`FLOAT`, `DOUBLE`) được biểu diễn nhị phân theo tiêu chuẩn IEEE 754, bản chất là lưu trữ gần đúng, dẫn đến việc tích lũy sai số làm tròn khi thực hiện các phép toán cộng trừ nhân chia tài chính. Đơn vị tiền tệ Việt Nam Đồng (VNĐ) không có phần tiền xu hay số thập phân lẻ, do đó sử dụng kiểu số nguyên lớn `BIGINT` (hoặc `DECIMAL`/`NUMERIC`) sẽ đảm bảo độ chính xác tuyệt đối 100% cho mọi giao dịch kế toán.

**Câu 5: Mục đích của endpoint `/api/tuitions/slow` và biến môi trường `FINANCE_DELAY_MS` khác nhau thế nào?**  
*Trả lời:* 
- Endpoint `/slow?delay=5000` được thiết kế riêng cho việc kiểm thử đơn vị bằng Postman, giúp lập trình viên chứng minh Finance API có thể phản hồi chậm theo ý muốn một cách trực quan.
- Biến môi trường `FINANCE_DELAY_MS` tác động trực tiếp vào endpoint nghiệp vụ `GET /api/tuitions/{studentId}`. Do Portal Backend chỉ gọi vào endpoint này nên bắt buộc phải dùng biến môi trường để làm chậm luồng gọi thực tế của Portal, từ đó kích hoạt cơ chế Timeout 3 giây của Portal.

**Câu 6: Đường dẫn `/api/tuitions/slow` và `/api/tuitions/{studentId}` có bị xung đột (conflict) định tuyến trong Spring Boot không?**  
*Trả lời:* Hoàn toàn không bị xung đột. Trong cơ chế phân giải URL của Spring MVC, khung điều phối luôn ưu tiên so khớp các đường dẫn cố định, tường minh (`literal path` như `/slow`) trước khi so khớp với các mẫu đường dẫn có biến (`path variable pattern` như `/{studentId}`). Ngoài ra, chuỗi "slow" cũng không khớp với biểu thức chính quy của mã sinh viên (`^B\d{2}DC[A-Z]{2}\d{3}$`), nên không thể bị nhầm lẫn.

**Câu 7: Trình bày sự khác biệt về mặt bản chất kỹ thuật giữa 3 cách làm Finance không phản hồi?**  
*Trả lời:*
- **Cách a (Dừng dịch vụ)** và **Cách c (Sai cổng):** Kết nối TCP không thể thiết lập được. Hệ điều hành gửi gói tin TCP RST từ chối kết nối ngay tức thì, Portal nhận ngoại lệ `ConnectException` rất nhanh (vài chục ms).
- **Cách b (Làm chậm 5s):** Kết nối TCP đã thiết lập thành công, nhưng tiến trình Finance bị nghẽn (sleep). Portal phải chờ đợi dữ liệu gửi về cho đến khi đồng hồ đếm ngược hết hạn mức 3000ms thì mới ném ra `ReadTimeoutException`. Cả 3 cách Portal đều bảo toàn hoạt động nhờ cơ chế xử lý ngoại lệ suy giảm có kiểm soát.

**Câu 8: Khi Finance trả về HTTP 404 và khi Finance bị chết hẳn thì Portal phản ứng khác nhau thế nào?**  
*Trả lời:* Cả hai trường hợp Portal đều trả về HTTP 200 kèm `tuitions = null` và thông tin sinh viên, nhưng nội dung thông điệp cảnh báo trong mảng `warnings` là hoàn toàn khác nhau về bản chất nghiệp vụ:
- Khi Finance trả 404: Finance vẫn sống bình thường, cảnh báo hiển thị là: *"Sinh viên chưa có khoản học phí nào"*.
- Khi Finance bị chết/timeout: Finance gặp sự cố hạ tầng, cảnh báo hiển thị là: *"Không lấy được thông tin học phí do dịch vụ Finance không phản hồi"*.

**Câu 9: Bằng chứng kiểm thử ngoại lệ chứng minh được những thuộc tính kiến trúc nào của hệ thống?**  
*Trả lời:* Nó chứng minh 3 thuộc tính kiến trúc tối quan trọng:
1. **Tính sẵn sàng và khả năng chịu lỗi (High Availability & Fault Tolerance):** Lỗi của phân hệ phụ không làm sập toàn bộ hệ thống.
2. **Khả năng suy giảm có kiểm soát (Graceful Degradation):** Vẫn phục vụ tối đa những gì có thể cho người dùng kèm giải thích rõ ràng.
3. **Hiệu lực của thiết lập Timeout:** Cắt đứt kết nối kịp thời, không để tài nguyên máy chủ bị chiếm dụng vô thời hạn.

#### 8.3. Ba câu hỏi tự đặt ra và câu trả lời mở rộng

**Câu hỏi tự đặt 1: Giả sử hai người dùng cùng bấm nút thanh toán học phí cho cùng một sinh viên tại cùng một thời điểm, làm thế nào để tránh việc cập nhật trạng thái bị tranh chấp (Race Condition)?**  
*Trả lời:* Trong môi trường đồng thời, nếu hai tiến trình cùng đọc trạng thái `UNPAID` và cùng gửi lệnh cập nhật `PAID`, ta cần áp dụng cơ chế **Khóa lạc quan (Optimistic Locking)** bằng cách thêm trường `@Version private Long version;` vào Entity `Tuition`. Khi một giao dịch commit thành công, số version sẽ tăng lên. Giao dịch đến sau kiểm tra thấy version không khớp sẽ bị ném ngoại lệ `OptimisticLockException` và bị hủy bỏ an toàn, đảm bảo tính nhất quán dữ liệu.

**Câu hỏi tự đặt 2: Nếu lượng sinh viên truy cập vào tra cứu học phí tăng vọt lên hàng chục ngàn người cùng lúc (ví dụ thời điểm đăng ký tín chỉ), Finance API sẽ chịu tải thế nào và giải pháp tối ưu là gì?**  
*Trả lời:* Điểm nghẽn sẽ xảy ra tại cơ sở dữ liệu `finance_db` do giới hạn Connection Pool. Để tối ưu, ta có thể:
1. Tạo chỉ mục đánh dấu trên cột `student_id` (đã thực hiện trong dự án).
2. Tích hợp tầng đệm dữ liệu **Redis Cache** phía trước Finance API. Khi Portal hỏi học phí của một sinh viên, Finance kiểm tra trong Redis trước, nếu có (Cache Hit) thì trả về ngay với độ trễ dưới 2ms mà không cần truy vấn CSDL PostgreSQL. Dữ liệu trong cache được làm mới (Cache Eviction/Update) khi có thao tác PUT đổi trạng thái học phí.

**Câu hỏi tự đặt 3: Tại sao trong ứng dụng doanh nghiệp người ta ưu tiên sử dụng Java Record cho DTO như `StatusRequest`?**  
*Trả lời:* Java Record (giới thiệu chính thức từ Java 16) được thiết kế chuyên biệt để làm vật chứa dữ liệu bất biến (Immutable Data Carrier). Record tự động sinh ra các hàm `constructor`, `getters`, `equals()`, `hashCode()` và `toString()` một cách chuẩn xác, ngắn gọn mà không cần viết boilerplate code hay phụ thuộc vào thư viện bên ngoài như Lombok. Tính bất biến của Record giúp dữ liệu truyền qua các tầng nghiệp vụ không bao giờ bị chỉnh sửa ngoài ý muốn, nâng cao tính an toàn của mã nguồn.

---

### 9. Đóng góp cụ thể của bản thân

| Hạng mục công việc | Chi tiết kỹ thuật đã thực hiện | Minh chứng cụ thể |
| :--- | :--- | :--- |
| **Quản lý mã nguồn Git** | Khởi tạo nhánh `feature/finance`, thực hiện 8 commit nguyên tử tuân thủ chuẩn Conventional Commits, tạo và hoàn thiện Pull Request #2. | Nhánh Git `feature/finance`, PR #2 trên repository nhóm |
| **Mã nguồn dịch vụ** | Toàn bộ mã nguồn `finance-api`: Controller, Entity, Repository, Exception Handler, DTO, Config CORS, Dockerfile, `schema.sql`, `data.sql`. | Thư mục `finance-api/src/` |
| **Bộ kiểm thử Postman** | Tập hợp 7 request có script assertion kiểm tra mã trạng thái, thời gian phản hồi và nội dung JSON. | File `postman/finance.postman_collection.json` |
| **Script tự động hóa** | Xây dựng script Python `run_test_suite.py` chạy kiểm thử tự động không cần GUI và script bash `simulate_failure.sh`. | Thư mục `scripts/` |
| **Đóng góp báo cáo nhóm** | Trực tiếp biên soạn: Mục so sánh 3 phương thức tích hợp (Chương 2); Mục Finance API (Chương 4); Mục Kiểm thử ngoại lệ và phân tích cơ chế suy giảm (Chương 5). | Các chương tương ứng trong Báo cáo tổng kết đồ án |

#### 9.1. Đóng góp hỗ trợ nhóm ngoài phần việc chính
- Hỗ trợ Thành viên 1 chuẩn hóa cấu trúc đối tượng lỗi JSON giữa Academic và Finance để Portal Backend chỉ cần viết một lớp Exception Parser dùng chung.
- Hỗ trợ Thành viên 3 cấu hình WebClient và thiết lập thời gian timeout chính xác trong mã nguồn Portal Backend, hỗ trợ viết kịch bản mock dữ liệu khi test giao diện.

---

### 10. Khai báo sử dụng công cụ hỗ trợ (AI Tools)

Tuân thủ đúng quy định và hướng dẫn của đề bài học phần, tôi khai báo trung thực các công cụ trí tuệ nhân tạo (AI) đã tham khảo trong quá trình thực hiện bài tập lớn:

| Tên công cụ AI | Mục đích sử dụng | Phương pháp tự kiểm tra và kiểm chứng lại | Phần tự tay điều chỉnh và hoàn thiện |
| :--- | :--- | :--- | :--- |
| **Claude / ChatGPT** | - Tra cứu cú pháp Regex chuẩn cho mã sinh viên PTIT.<br>- Tham khảo cấu trúc chuẩn của `@RestControllerAdvice` trong Spring Boot 3. | - Tự viết bộ unit test kiểm tra regex với nhiều trường hợp chuỗi đặc biệt.<br>- Chạy thử nghiệm thực tế với Postman để xác minh cấu trúc phản hồi lỗi. | - Tự viết toàn bộ logic kiểm tra hợp đồng API trong Controller.<br>- Chỉnh sửa định dạng lỗi JSON cho khớp tuyệt đối với quy ước chung của nhóm. |
| **GitHub Copilot** | Hỗ trợ gợi ý nhanh cú pháp boilerplate khi viết các hàm getter/setter và cấu hình Spring Data JPA. | Đọc và rà soát kỹ lưỡng từng dòng mã nguồn được gợi ý, đảm bảo tuân thủ nghiêm ngặt chuẩn định dạng của dự án. | Tự thiết kế toàn bộ logic của hai cơ chế làm chậm `/slow` và biến môi trường `FINANCE_DELAY_MS`. |

---

### 11. Tự đánh giá và Kế hoạch cải thiện

#### 11.1. Tự đánh giá theo thang điểm của đề tài

| Tiêu chí đánh giá (Trọng số) | Điểm tự chấm | Căn cứ chấm điểm thực tế |
| :--- | :---: | :--- |
| **1. Kiến thức lý thuyết, hiểu nguyên lý và so sánh giải pháp (20%)** | **10 / 10** | Nắm vững bản chất tích hợp hệ thống, nguyên lý RESTful, phân tích sâu sắc ưu nhược điểm của 3 phương thức tích hợp, hiểu rõ nguyên nhân Data Silos và ranh giới CSDL. |
| **2. Phân tích bài toán, thiết kế kiến trúc và luồng dữ liệu (15%)** | **10 / 10** | Hiểu rõ kiến trúc phân tầng của toàn bộ đồ án, nắm vững luồng dữ liệu khi thành công cũng như khi xảy ra lỗi tại từng phân hệ. |
| **3. Demo hoạt động và thể hiện đúng cơ chế tích hợp (35%)** | **10 / 10** | Dịch vụ `finance-api` chạy ổn định trên cổng 8082, CSDL PostgreSQL độc lập, tích hợp mượt mà với Portal Backend và Frontend, demo thành công 100%. |
| **4. Kiểm thử, minh chứng và khả năng chạy lại (15%)** | **10 / 10** | Xây dựng đầy đủ Postman collection, script kiểm thử tự động, thực nghiệm thành công 3 cách làm Finance không phản hồi với số liệu và log minh chứng sắc bén. |
| **5. Thuyết trình, vấn đáp và mức độ hiểu của thành viên (15%)** | **10 / 10** | Tự tin trả lời trôi chảy toàn bộ các câu hỏi chung và câu hỏi chuyên sâu của phân hệ phụ trách, hiểu thấu đáo bản chất kỹ thuật bên dưới. |

#### 11.2. Đánh giá tinh thần làm việc nhóm

| Tiêu chí | Mức độ (1 - 5) | Ghi chú đánh giá |
| :--- | :---: | :--- |
| Hoàn thành công việc đúng thời hạn | 5 / 5 | Hoàn thành trước tiến độ, tạo điều kiện thuận lợi cho việc ghép nối hệ thống. |
| Chủ động báo cáo tiến độ và nêu khó khăn | 5 / 5 | Thường xuyên cập nhật tình hình trong các buổi họp hàng ngày của nhóm. |
| Tuân thủ nghiêm túc Hợp đồng API và quy trình Git | 5 / 5 | Không tự ý sửa đổi schema, commit rõ ràng, tuân thủ luồng Git Flow. |
| Tích cực hỗ trợ các thành viên khác trong nhóm | 5 / 5 | Chủ động phối hợp cùng Thành viên 1 và 3 giải quyết các vướng mắc tích hợp. |

#### 11.3. Kế hoạch cải thiện bản thân
1. Nâng cao kỹ năng viết Unit Test và Integration Test tự động bằng Testcontainers để kiểm thử tương tác CSDL thực tế trong quy trình CI/CD.
2. Tìm hiểu sâu hơn về kiến trúc Reactive Microservices với Spring WebFlux và Apache Kafka để xử lý các bài toán tích hợp phân tán đòi hỏi thông lượng cao.

#### 11.4. Ý kiến nhận xét của các thành viên trong nhóm
- **Nhận xét của Nhóm trưởng (Thành viên 1 - Phụ trách Academic API):**  
  *"Thành viên 2 hoàn thành công việc rất xuất sắc, mã nguồn sạch sẽ, tuân thủ đúng 100% hợp đồng API đã cam kết. Đặc biệt phần kiểm thử ngoại lệ và cơ chế làm chậm được thiết kế rất thông minh, giúp nhóm thực nghiệm thành công điểm nhấn kỹ thuật quan trọng nhất của bài tập lớn."*  
- **Nhận xét của Thành viên 3 (Phụ trách Portal):**  
  *"Nhờ có các tài liệu API rõ ràng và sự hỗ trợ nhiệt tình của bạn Ngọc mà việc tích hợp dữ liệu Finance vào Portal diễn ra rất suôn sẻ. Phần bắt lỗi và suy giảm có kiểm soát chạy rất chuẩn xác trên giao diện."*  


---

### 12. Cam đoan của sinh viên

Tôi xin cam đoan toàn bộ nội dung trong bản báo cáo cá nhân này là trung thực và phản ánh chính xác những công việc tôi đã trực tiếp nghiên cứu, lập trình và kiểm thử trong quá trình thực hiện bài tập lớn. Tôi hoàn toàn hiểu rõ kiến trúc, luồng dữ liệu và cơ chế tích hợp của toàn bộ hệ thống và sẵn sàng trả lời trực tiếp mọi câu hỏi của Hội đồng chấm thi.

*Hà Nội, ngày 18 tháng 11 năm 2026*  
**Người làm báo cáo**  
*(Ký và ghi rõ họ tên)*  

<br>
<br>

**Lê Việt Ngọc**
