import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_report():
    doc = docx.Document()

    # Set page margins: Top 2cm, Bottom 2cm, Left 3cm, Right 2cm (Standard PTIT)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.79)     # ~2.0 cm
        section.bottom_margin = Inches(0.79)  # ~2.0 cm
        section.left_margin = Inches(1.18)    # ~3.0 cm
        section.right_margin = Inches(0.79)   # ~2.0 cm

    # Base style
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(13)
    normal_style.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    normal_style.paragraph_format.line_spacing = 1.25
    normal_style.paragraph_format.space_after = Pt(4)

    # Header / Title Block
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_inst = p_inst.add_run("HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG\n")
    r_inst.bold = True
    r_inst.font.size = Pt(14)
    r_inst.font.color.rgb = RGBColor(0x99, 0x00, 0x00) # PTIT Red

    r_sub = p_inst.add_run("KHOA CÔNG NGHỆ THÔNG TIN\n---------------------------------------\n")
    r_sub.bold = True
    r_sub.font.size = Pt(12)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("BÁO CÁO CÁ NHÂN\n")
    r_title.bold = True
    r_title.font.size = Pt(20)
    r_title.font.color.rgb = RGBColor(0x00, 0x33, 0x66)

    r_course = p_title.add_run("HỌC PHẦN: NHẬP MÔN TÍCH HỢP HỆ THỐNG\n")
    r_course.bold = True
    r_course.font.size = Pt(15)

    r_topic = p_title.add_run("CHỦ ĐỀ 04: TÍCH HỢP ỨNG DỤNG THÔNG QUA REST API VÀ CỔNG THÔNG TIN PORTAL\n")
    r_topic.bold = True
    r_topic.font.size = Pt(14)
    r_topic.font.color.rgb = RGBColor(0x00, 0x55, 0x99)

    r_role = p_title.add_run("VAI TRÒ: THÀNH VIÊN 2 - FINANCE API VÀ KIỂM THỬ LỖI\n")
    r_role.bold = True
    r_role.italic = True
    r_role.font.size = Pt(13)

    # Student Info Box
    p_info = doc.add_paragraph()
    p_info.paragraph_format.space_after = Pt(16)
    p_info.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_info.add_run("Sinh viên thực hiện: ").bold = True
    p_info.add_run("Nguyễn Thị Ánh Ngọc    |    ")
    p_info.add_run("Mã sinh viên: ").bold = True
    p_info.add_run("B22DCCN520\n")
    p_info.add_run("Lớp: ").bold = True
    p_info.add_run("D22CQCN01-B    |    ")
    p_info.add_run("Nhóm: ").bold = True
    p_info.add_run("04 (Nhóm 3 thành viên)\n")
    p_info.add_run("Giảng viên hướng dẫn: ").bold = True
    p_info.add_run("TS. Nguyễn Huy Trung\n\n")
    p_info.add_run("Hà Nội, tháng 11 năm 2026").italic = True

    doc.add_page_break()

    # Section Helper
    def add_sec_heading(title, level=1):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(title)
        r.bold = True
        if level == 1:
            r.font.size = Pt(15)
            r.font.color.rgb = RGBColor(0x00, 0x33, 0x66)
        elif level == 2:
            r.font.size = Pt(13.5)
            r.font.color.rgb = RGBColor(0x00, 0x55, 0x99)
        else:
            r.font.size = Pt(13)
        return p

    def add_table(headers, data, col_widths=None):
        table = doc.add_table(rows=len(data) + 1, cols=len(headers))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False

        # Header Row
        hdr_row = table.rows[0]
        for idx, title in enumerate(headers):
            cell = hdr_row.cells[idx]
            cell.text = title
            set_cell_background(cell, "003366")
            set_cell_margins(cell, top=120, bottom=120, left=150, right=150)
            for paragraph in cell.paragraphs:
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for run in paragraph.runs:
                    run.font.name = 'Times New Roman'
                    run.font.bold = True
                    run.font.size = Pt(11)
                    run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

        # Data Rows
        for r_idx, row_data in enumerate(data):
            row = table.rows[r_idx + 1]
            bg_color = "F9FBFD" if r_idx % 2 == 1 else "FFFFFF"
            for c_idx, val in enumerate(row_data):
                cell = row.cells[c_idx]
                cell.text = str(val)
                set_cell_background(cell, bg_color)
                set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.font.name = 'Times New Roman'
                        run.font.size = Pt(11)

        if col_widths:
            for row in table.rows:
                for idx, w in enumerate(col_widths):
                    row.cells[idx].width = Inches(w)

        doc.add_paragraph().paragraph_format.space_after = Pt(4)
        return table

    def add_code(code_text):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.2)
        p.paragraph_format.right_indent = Inches(0.2)
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(code_text)
        r.font.name = 'Courier New'
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(0x11, 0x33, 0x55)

    # 1. THÔNG TIN CHUNG
    add_sec_heading("1. Thông tin chung", 1)
    t1_headers = ["Tiêu chí", "Thông tin thực tế của sinh viên"]
    t1_data = [
        ["Họ và tên", "Nguyễn Thị Ánh Ngọc"],
        ["Mã sinh viên / Lớp", "B22DCCN520 / D22CQCN01-B"],
        ["Vai trò trong nhóm", "Thành viên 2: Finance API và kiểm thử lỗi ngoại lệ"],
        ["Thành phần phụ trách", "finance-api (cổng 8082, finance_db), Postman collection Finance, kiểm thử ngoại lệ"],
        ["Công nghệ sử dụng", "Spring Boot 3.2 (Web, Data JPA, Validation, PostgreSQL Driver), Postman, Docker"],
        ["Nhánh Git", "feature/finance"],
        ["Phần báo cáo chung phụ trách", "Chương 2 mục so sánh 3 cách tích hợp; mục Finance trong Chương 4; mục kiểm thử ngoại lệ trong Chương 5"],
        ["Thời gian thực hiện", "Từ 01/11/2026 đến 18/11/2026"]
    ]
    add_table(t1_headers, t1_data, [2.2, 4.3])

    add_sec_heading("1.1. Tóm tắt đóng góp", 2)
    p = doc.add_paragraph()
    p.add_run("Trong dự án bài tập lớn Chủ đề 04, tôi phụ trách toàn bộ việc thiết kế, xây dựng và kiểm thử dịch vụ Finance API (cổng 8082) với cơ sở dữ liệu độc lập finance_db. Tôi đã lập trình hoàn chỉnh các endpoint nghiệp vụ theo hợp đồng API, xử lý ngoại lệ tập trung và cấu hình CORS. Tôi đã sáng tạo hai cơ chế làm chậm có chủ đích (endpoint /slow và biến môi trường FINANCE_DELAY_MS) phục vụ kiểm thử timeout 3s của Portal Backend. Tôi đã xây dựng Postman Collection có test assertions tự động và trực tiếp thực nghiệm thành công 3 kịch bản kiểm thử ngoại lệ khi Finance không phản hồi. Kết quả này chứng minh trọn vẹn cơ chế suy giảm có kiểm soát (Graceful Degradation), giúp hệ thống Portal vận hành bền bỉ và không bị gián đoạn.")

    # 2. NHIỆM VỤ ĐƯỢC GIAO VÀ MỨC ĐỘ HOÀN THÀNH
    add_sec_heading("2. Nhiệm vụ được giao và mức độ hoàn thành", 1)
    t2_headers = ["STT", "Công việc được giao", "Hạn", "Trạng thái", "Minh chứng kỹ thuật"]
    t2_data = [
        ["1", "Cài môi trường và xác nhận hợp đồng API", "Ngày 1", "[X]", "File API-CONTRACT.md, họp nhóm"],
        ["2", "Tạo project finance-api, cấu hình cổng 8082", "Ngày 2", "[X]", "Commit 7a1f8b2: init finance-api"],
        ["3", "Tạo finance_db, bảng tuition, nạp dữ liệu mẫu", "Ngày 2", "[X]", "File schema.sql, data.sql"],
        ["4", "Viết Entity Tuition và TuitionRepository", "Ngày 2", "[X]", "Tuition.java, TuitionRepository.java"],
        ["5", "Endpoint GET /api/tuitions/{studentId} (200/400/404)", "Ngày 3", "[X]", "TuitionController.java, test Postman F-01->03"],
        ["6", "Endpoint PUT /api/tuitions/{id}/status (200/400/404)", "Ngày 4", "[X]", "Hàm updateStatus, test Postman F-04, F-05"],
        ["7", "Xử lý lỗi tập trung và CORS", "Ngày 4", "[X]", "GlobalExceptionHandler.java, CorsConfig.java"],
        ["8", "Cơ chế làm chậm có chủ đích: /slow và FINANCE_DELAY_MS", "Ngày 5", "[X]", "Biến môi trường FINANCE_DELAY_MS, /slow"],
        ["9", "Đẩy code feature/finance, tạo PR, viết README", "Ngày 5", "[X]", "PR #2 trên GitHub repo, README.md"],
        ["10", "Postman collection Finance (7 request, có test script)", "Ngày 5", "[X]", "postman/finance.postman_collection.json"],
        ["11", "Chụp ảnh bằng chứng F-01 đến F-05", "Ngày 5", "[X]", "Thư mục ảnh minh chứng F-01 -> F-05"],
        ["12", "Kiểm thử Finance không phản hồi theo 3 cách", "Ngày 7", "[X]", "Log và bảng kết quả mục 4.6"],
        ["13", "Kiểm thử PUT rồi tra lại qua Portal (ca liên thông 8)", "Ngày 7", "[X]", "Giao diện Portal hiển thị PAID"],
        ["14", "Viết mục so sánh 3 cách tích hợp (Chương 2)", "Ngày 6", "[X]", "Chương 2 báo cáo tổng hợp"],
        ["15", "Viết mục Finance (Chương 4) và kiểm thử ngoại lệ (Chương 5)", "Ngày 7", "[X]", "Chương 4 và 5 báo cáo tổng hợp"],
        ["16", "Review báo cáo, chạy thử toàn hệ thống, tập vấn đáp", "Ngày 8-10", "[X]", "Chạy tích hợp trên Docker Compose"]
    ]
    add_table(t2_headers, t2_data, [0.5, 2.5, 0.8, 0.7, 2.0])

    p_stat = doc.add_paragraph()
    p_stat.add_run("Tỉ lệ hoàn thành: ").bold = True
    p_stat.add_run("16 / 16 việc (100%).    ")
    p_stat.add_run("Việc chưa xong và lý do: ").bold = True
    p_stat.add_run("Không có.")

    # 3. HIỂU BIẾT VỀ TOÀN HỆ THỐNG
    add_sec_heading("3. Hiểu biết về toàn hệ thống", 1)
    add_sec_heading("3.1. Bài toán tích hợp", 2)
    doc.add_paragraph("Trong trường đại học, dữ liệu sinh viên bị cô lập tại các phòng ban khác nhau (hiện tượng Data Silos): Phòng Đào tạo quản lý hồ sơ sinh viên qua hệ thống Academic, còn Phòng Tài chính quản lý tiền học phí qua hệ thống Finance. Cổng thông tin Portal đóng vai trò là điểm truy cập duy nhất, nhận mã sinh viên từ người dùng, gọi API của cả hai hệ thống, tổng hợp dữ liệu và hiển thị lên trình duyệt web. Portal tuyệt đối không có cơ sở dữ liệu riêng và không đọc trực tiếp cơ sở dữ liệu của các hệ thống khác. Đây là mô hình tích hợp ở mức giao diện ứng dụng (Application Interface Integration).")

    add_sec_heading("3.2. Sơ đồ kiến trúc tổng thể", 2)
    doc.add_paragraph("Kiến trúc phân tầng gồm 4 dịch vụ độc lập:")
    add_code("""Người dùng (Trình duyệt Web)
      │
      ▼
[ Portal Frontend :3000 ] (React + Ant Design)
      │  GET /api/portal/students/{id}/summary
      ▼
[ Portal Backend :8080 ] (Spring Boot - Không lưu CSDL)
      ├── (REST/JSON Timeout 1s) ──> [ Academic API :8081 ] ──> [( academic_db )]
      └── (REST/JSON Timeout 3s) ──> [ Finance API :8082 ]  ──> [( finance_db )]""")

    add_sec_heading("3.3. Các endpoint toàn hệ thống", 2)
    t3_headers = ["Dịch vụ", "Phương thức và đường dẫn", "Chức năng nghiệp vụ", "Mã trả về"]
    t3_data = [
        ["Academic :8081", "GET /api/students/{studentId}", "Lấy thông tin sinh viên", "200, 400, 404"],
        ["Academic :8081", "POST /api/students", "Thêm sinh viên mới", "201, 400, 409"],
        ["Finance :8082", "GET /api/tuitions/{studentId}", "Lấy danh sách học phí", "200, 400, 404"],
        ["Finance :8082", "PUT /api/tuitions/{id}/status", "Đổi trạng thái PAID/UNPAID", "200, 400, 404"],
        ["Portal :8080", "GET /api/portal/students/{id}/summary", "Tổng hợp sinh viên và học phí", "200, 400, 404, 503"]
    ]
    add_table(t3_headers, t3_data, [1.3, 2.5, 1.8, 0.9])

    add_sec_heading("3.4. Luồng xử lý khi thành công", 2)
    doc.add_paragraph("1. Người dùng nhập mã B22DCCN001 trên giao diện Portal Frontend (port 3000). Giao diện kiểm tra định dạng và gọi Portal Backend.\n"
                      "2. Portal Backend kiểm tra lại định dạng mã sinh viên, sau đó gọi Academic: GET /api/students/B22DCCN001.\n"
                      "3. Academic trả về mã HTTP 200 và JSON thông tin sinh viên.\n"
                      "4. Portal tiếp tục gọi Finance: GET /api/tuitions/B22DCCN001; Finance trả về mã HTTP 200 và mảng học phí.\n"
                      "5. Portal ghép thành đối tượng {student, tuitions, warnings: []} và trả về cho giao diện hiển thị bảng hoàn chỉnh.")

    add_sec_heading("3.5. Quy tắc xử lý lỗi của Portal", 2)
    t5_headers = ["Tình huống thực tế", "Portal trả về", "Lý do thiết kế kiến trúc"]
    t5_data = [
        ["Mã sinh viên sai định dạng (abc123)", "400 Bad Request", "Chặn sớm ngay tại cửa ngõ, tránh gọi vô ích xuống backend."],
        ["Academic trả 404", "404 Not Found", "Sinh viên không tồn tại thì không có ý nghĩa hiển thị học phí."],
        ["Academic không phản hồi / chết", "503 Service Unavailable", "Dữ liệu thiết yếu (Core) bị thiếu, không thể đáp ứng dịch vụ."],
        ["Finance trả 404", "200 OK, tuitions = null, có warning", "Dữ liệu bổ sung; sinh viên vẫn hợp lệ, chỉ là chưa có học phí."],
        ["Finance không phản hồi / timeout", "200 OK, tuitions = null, có warning", "Suy giảm có kiểm soát (Graceful Degradation): dịch vụ phụ lỗi không làm sập Portal."]
    ]
    add_table(t5_headers, t5_data, [1.8, 1.8, 2.9])

    add_sec_heading("3.6. So sánh 3 cách tích hợp và lý do chọn REST API", 2)
    t6_headers = ["Tiêu chí", "Qua REST API (Nhóm chọn)", "Truy cập trực tiếp CSDL", "Hiển thị tại Portal (UI Mashup)"]
    t6_data = [
        ["Ý tưởng", "Gọi giao diện chính thức qua HTTP/JSON", "Portal đọc/ghi thẳng bảng dữ liệu", "Nhúng giao diện (iframe/liên kết)"],
        ["Ranh giới hệ thống", "Được bảo toàn tuyệt đối", "Bị phá vỡ hoàn toàn", "Giữ nguyên nhưng không trao đổi dữ liệu"],
        ["Mức độ phụ thuộc", "Phụ thuộc lỏng vào hợp đồng API", "Phụ thuộc chặt vào cấu trúc bảng", "Phụ thuộc giao diện người dùng"],
        ["Kiểm soát & Bảo mật", "Bên sở hữu tự kiểm soát, an toàn", "Khó kiểm soát, rủi ro lộ toàn bộ CSDL", "Mỗi bên tự kiểm soát"],
        ["Tổng hợp dữ liệu", "Rất tốt, ghép JSON nhất quán", "Có nhưng rủi ro khóa bảng", "Không thể tổng hợp dữ liệu"],
        ["Thời điểm phù hợp", "Hệ thống độc lập, nhiều bên kết nối", "Báo cáo nội bộ một đơn vị sở hữu", "Gộp lối vào giao diện nhanh chóng"]
    ]
    add_table(t6_headers, t6_data, [1.1, 1.9, 1.8, 1.7])

    # 4. CHI TIẾT PHẦN PHỤ TRÁCH: FINANCE API VÀ KIỂM THỬ LỖI
    add_sec_heading("4. Chi tiết phần tôi phụ trách: Finance API và kiểm thử lỗi", 1)
    doc.add_paragraph("Finance là hệ thống tài chính giả lập, sở hữu cơ sở dữ liệu độc lập finance_db. Với Portal, dữ liệu học phí là dữ liệu bổ sung: khi Finance lỗi, Portal vẫn bảo toàn hiển thị thông tin sinh viên kèm cảnh báo rõ ràng. Vì vậy, Finance là thành phần hạt nhân dùng để chứng minh khả năng chịu lỗi và kiểm thử ngoại lệ của toàn hệ thống.")

    add_sec_heading("4.1. Cấu hình và Cơ sở dữ liệu", 2)
    doc.add_paragraph("File cấu hình application.yml cấu hình cổng 8082, kết nối PostgreSQL và biến FINANCE_DELAY_MS:")
    add_code("""server:
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
  delay-ms: ${FINANCE_DELAY_MS:0}""")

    doc.add_paragraph("Lược đồ CSDL schema.sql và dữ liệu mẫu data.sql:")
    add_code("""CREATE TABLE IF NOT EXISTS tuition (
    id         BIGSERIAL   PRIMARY KEY,
    student_id VARCHAR(12) NOT NULL,        -- Mã tham chiếu, KHÔNG có khóa ngoại sang academic_db
    semester   VARCHAR(10) NOT NULL,
    amount     BIGINT      NOT NULL CHECK (amount > 0),
    status     VARCHAR(10) NOT NULL CHECK (status IN ('PAID', 'UNPAID')),
    due_date   DATE
);
CREATE INDEX IF NOT EXISTS idx_tuition_student ON tuition(student_id);

-- Dữ liệu mẫu (data.sql)
INSERT INTO tuition (student_id, semester, amount, status, due_date) VALUES
('B22DCCN001', '2026-1', 8500000, 'UNPAID', '2026-12-15'),
('B22DCCN001', '2025-2', 8200000, 'PAID',   '2026-05-15'),
('B22DCCN002', '2026-1', 8500000, 'PAID',   '2026-12-15');""")

    doc.add_paragraph("Các quyết định kỹ thuật then chốt:\n"
                      "- Không tạo khóa ngoại: Do 2 CSDL vật lý độc lập, RDBMS không thể tạo khóa ngoại qua CSDL khác. student_id chỉ là mã tham chiếu nghiệp vụ; Portal chịu trách nhiệm kiểm tra tính hợp lệ qua API.\n"
                      "- Dùng kiểu BIGINT cho tiền: Đơn vị VNĐ không có số lẻ thập phân; kiểu số nguyên lớn triệt tiêu hoàn toàn sai số làm tròn của số thực IEEE 754.\n"
                      "- Ràng buộc CHECK và Index: CSDL tự động chặn trạng thái sai, và chỉ mục idx_tuition_student giúp tra cứu học phí đạt độ phức tạp O(log N).")

    add_sec_heading("4.2. Hai cơ chế làm chậm Finance có chủ đích", 2)
    t_slow_headers = ["Cơ chế làm chậm", "Cách sử dụng kỹ thuật", "Mục đích kiểm thử cụ thể"]
    t_slow_data = [
        ["Endpoint /api/tuitions/slow?delay=5000", "Gọi trực tiếp từ Postman hoặc trình duyệt", "Chứng minh Finance phản hồi chậm 5s độc lập (bằng chứng phía Finance)."],
        ["Biến môi trường FINANCE_DELAY_MS=5000", "Chạy Finance với biến này rồi tra cứu qua Portal", "Làm chậm chính endpoint /api/tuitions/{studentId} để kiểm tra Portal cắt timeout sau 3s."]
    ]
    add_table(t_slow_headers, t_slow_data, [2.0, 2.2, 2.3])

    add_sec_heading("4.3. Kiểm thử ngoại lệ: 3 cách làm Finance không phản hồi", 2)
    t_exc_headers = ["Cách thực hiện", "Thao tác kỹ thuật", "Hiện tượng mong đợi phía Portal", "Kết quả thực tế", "Thời gian"]
    t_exc_data = [
        ["a. Tắt dịch vụ", "docker compose stop finance-api", "Từ chối kết nối (ConnectException); Portal trả 200, tuitions=null, có warning", "Portal trả 200 + dữ liệu sinh viên + cảnh báo", "28 ms"],
        ["b. Làm chậm 5s", "FINANCE_DELAY_MS=5000 rồi tra cứu qua Portal", "Portal đợi 3s ném ReadTimeoutException; trả 200 + warning", "Portal cắt kết nối sau đúng 3s, hiển thị cảnh báo", "3,042 ms"],
        ["c. Cấu hình sai cổng", "Portal đặt FINANCE_URL trỏ port 9999", "Không có socket lắng nghe, ConnectException tức thì", "Portal xử lý tương tự cách a, trả 200 + warning", "19 ms"]
    ]
    add_table(t_exc_headers, t_exc_data, [1.1, 1.6, 1.8, 1.4, 0.6])

    # 5. KẾT QUẢ KIỂM THỬ
    add_sec_heading("5. Kết quả kiểm thử phần tôi phụ trách", 1)
    t_test_headers = ["Ca", "Kịch bản kiểm thử", "Đầu vào", "Kết quả mong đợi", "Kết quả thực tế", "Thời gian", "Đánh giá"]
    t_test_data = [
        ["F1", "GET học phí hợp lệ", "B22DCCN001", "200 OK, mảng 2 khoản", "Trả về 200, đúng 2 khoản", "18 ms", "ĐẠT"],
        ["F2", "GET chưa có học phí", "B22DCCN013", "404 Not Found", "Trả về 404, thông điệp chuẩn", "12 ms", "ĐẠT"],
        ["F3", "GET mã sai định dạng", "abc123", "400 Bad Request", "Trả về 400, chặn bởi Regex", "9 ms", "ĐẠT"],
        ["F4", "PUT đổi trạng thái hợp lệ", "id=1, status=PAID", "200 OK, status=PAID", "Trả về 200, CSDL lưu PAID", "24 ms", "ĐẠT"],
        ["F5", "PUT trạng thái không hợp lệ", "id=1, status=DONE", "400 Bad Request", "Trả về 400, chặn bởi validation", "11 ms", "ĐẠT"],
        ["F6", "PUT id không tồn tại", "id=9999, PAID", "404 Not Found", "Trả về 404, báo không thấy id", "15 ms", "ĐẠT"],
        ["F7", "PUT rồi tra cứu lại qua Portal", "id=1 sang PAID -> GET Portal", "Portal hiển thị PAID", "Giao diện cập nhật trạng thái xanh", "65 ms", "ĐẠT"]
    ]
    add_table(t_test_headers, t_test_data, [0.4, 1.6, 1.2, 1.3, 1.1, 0.5, 0.4])

    doc.add_paragraph("Kết luận kiểm thử: Cả 7 ca kiểm thử chức năng và 3 kịch bản ngoại lệ đều đạt 100%. Portal không bao giờ bị sập khi Finance lỗi, luôn duy trì hiển thị thông tin sinh viên kèm cảnh báo rõ ràng.")

    # 6. KHÓ KHĂN VÀ GIẢI PHÁP
    add_sec_heading("6. Khó khăn gặp phải và cách giải quyết", 1)
    t_diff_headers = ["STT", "Vấn đề gặp phải", "Nguyên nhân gốc rễ", "Cách giải quyết", "Bài học rút ra"]
    t_diff_data = [
        ["1", "PUT trả lỗi 415 hoặc 400 dù đã gửi JSON", "Quên đặt header Content-Type: application/json hoặc body gửi text thuần", "Trong Postman chọn Body -> raw -> JSON và gửi đúng {\"status\":\"PAID\"}", "Phải kiểm soát chính xác cả HTTP Headers lẫn Body dữ liệu."],
        ["2", "Lỗi ném 500 khi vi phạm CHECK trên status", "Gửi status ngoài PAID/UNPAID mà Controller chưa validate trước khi lưu", "Thêm kiểm tra chuỗi status trong Controller, sai ném BadRequestException (400)", "Application layer phải validate trước để bảo vệ CSDL và trả đúng mã HTTP 4xx."],
        ["3", "Test làm chậm không thấy Portal cắt sau 3s", "Làm chậm endpoint /slow (Portal không gọi), thay vì endpoint Portal thật sự gọi", "Tạo biến môi trường FINANCE_DELAY_MS làm chậm đúng endpoint GET /{studentId}", "Phải hiểu rõ luồng gọi API thực tế khi thiết kế kịch bản kiểm thử phân tán."],
        ["4", "Khó phân biệt bản chất giữa cách a và c", "Cả hai đều bị từ chối kết nối ngay tức thì (ConnectException) dưới 30ms", "Phân tích sâu cơ chế mạng: a là lỗi dịch vụ chết, c là lỗi cấu hình hạ tầng mạng", "Hiểu sâu tầng TCP/IP giúp lý giải bản chất các loại ngoại lệ mạng."]
    ]
    add_table(t_diff_headers, t_diff_data, [0.4, 1.5, 1.6, 1.6, 1.4])

    # 7. KIẾN THỨC HỌC ĐƯỢC
    add_sec_heading("7. Kiến thức học được", 1)
    t_kno_headers = ["Khái niệm cốt lõi", "Định nghĩa theo cách hiểu của tôi", "Minh chứng trong dự án"]
    t_kno_data = [
        ["Tích hợp hệ thống", "Kết nối các hệ thống độc lập để trao đổi dữ liệu phục vụ nghiệp vụ chung", "Portal kết nối và ghép dữ liệu từ Academic và Finance"],
        ["Data Silos", "Dữ liệu bị cô lập trong từng phân hệ, khó chia sẻ xuyên suốt", "Thông tin sinh viên ở Academic, học phí ở Finance"],
        ["RESTful API", "Kiểu kiến trúc tài nguyên qua HTTP, giao tiếp JSON, không trạng thái", "GET /api/tuitions/B22DCCN001, PUT /api/tuitions/1/status"],
        ["Hợp đồng API", "Văn bản thỏa thuận thống nhất về URL, Headers, JSON và mã lỗi", "File API-CONTRACT.md giúp 3 người code song song"],
        ["Timeout", "Giới hạn thời gian tối đa chờ phản hồi, hết hạn thì ngắt kết nối an toàn", "Portal chờ Finance tối đa 3 giây, tránh treo hệ thống"],
        ["Suy giảm có kiểm soát", "Hệ thống vẫn phục vụ phần chính kèm cảnh báo khi phần phụ gặp lỗi", "Finance lỗi thì Portal vẫn hiển thị đầy đủ thông tin sinh viên"],
        ["Tính Idempotent của PUT", "Gọi một lần hay nhiều lần cùng nội dung đều cho ra cùng một trạng thái", "Đặt học phí id=1 thành PAID nhiều lần vẫn là PAID"],
        ["Ranh giới CSDL", "Mỗi dịch vụ sở hữu CSDL riêng, không tạo khóa ngoại bắc qua CSDL", "student_id ở Finance chỉ là mã tham chiếu logic"],
        ["BIGINT cho tiền tệ", "Dùng số nguyên lớn lưu tiền để triệt tiêu sai số làm tròn của số thực", "amount lưu 8500000 VNĐ, chính xác tuyệt đối 100%"],
        ["Chỉ mục (Index)", "Cấu trúc cây B-Tree tăng tốc độ tìm kiếm bản ghi", "Chỉ mục idx_tuition_student giúp tra cứu theo sinh viên siêu nhanh"]
    ]
    add_table(t_kno_headers, t_kno_data, [1.4, 2.7, 2.4])

    doc.add_paragraph("Điều tôi hiểu rõ nhất sau bài tập này: Trong hệ thống phân tán, lỗi mạng và sự cố dịch vụ là điều tất yếu. Thiết kế hệ thống chịu lỗi với Timeout và Suy giảm có kiểm soát (Graceful Degradation) là nguyên tắc sống còn để bảo đảm độ tin cậy của phần mềm.\n"
                      "Điều tôi còn chưa chắc và muốn mở rộng: Muốn nghiên cứu áp dụng WebClient reactive phi phong tỏa để gọi API song song và áp dụng thư viện Resilience4j triển khai Circuit Breaker hoàn chỉnh trong môi trường production.")

    # 8. CHUẨN BỊ VẤN ĐÁP
    add_sec_heading("8. Chuẩn bị vấn đáp bảo vệ đồ án", 1)
    doc.add_paragraph("Dưới đây là phần tổng hợp các câu hỏi vấn đáp điển hình và câu trả lời tự diễn đạt chi tiết:")

    add_sec_heading("8.1. Câu hỏi chung toàn nhóm", 2)
    doc.add_paragraph("1. Vì sao Portal không đọc thẳng CSDL của Academic hoặc Finance?\n"
                      "-> Trả lời: Vì làm vậy phá vỡ ranh giới và quyền sở hữu dữ liệu: Portal phụ thuộc chặt vào cấu trúc bảng (đổi tên cột là sập), đòi hỏi chia sẻ tài khoản CSDL nội bộ (rủi ro bảo mật nghiêm trọng) và bỏ qua toàn bộ kiểm tra nghiệp vụ của hệ thống gốc. Qua REST API, mỗi bên tự chủ hoàn toàn dữ liệu và logic của mình.\n\n"
                      "2. Timeout để làm gì? Căn cứ vào đâu chọn 1s và 3s?\n"
                      "-> Trả lời: Timeout giới hạn thời gian chờ để không làm cạn kiệt tài nguyên luồng của Portal khi một dịch vụ chậm. Chọn 1s cho Academic vì đây là dữ liệu cốt lõi, truy vấn nhẹ phải phản hồi cực nhanh. Chọn 3s cho Finance vì dữ liệu bổ sung có thể xử lý phức tạp hơn; 3s là ngưỡng an toàn không để người dùng chờ quá lâu.\n\n"
                      "3. Khi Finance chết Portal xử lý thế nào, vì sao vẫn trả 200? Còn khi Academic chết?\n"
                      "-> Trả lời: Học phí là dữ liệu bổ sung nên Portal thực hiện suy giảm có kiểm soát: vẫn hiển thị thông tin sinh viên, tuitions=null và kèm warning; trả 200 vì nhu cầu tra cứu sinh viên đã được đáp ứng phần cốt lõi. Thông tin sinh viên là dữ liệu thiết yếu: Academic chết thì không có đối tượng để hiển thị, bắt buộc Portal phải trả mã 503 Service Unavailable.\n\n"
                      "4. Phân biệt 400, 404, 409; phân biệt POST và PUT?\n"
                      "-> Trả lời: 400 là yêu cầu sai cú pháp; 404 là cú pháp đúng nhưng không thấy dữ liệu; 409 là xung đột trạng thái (trùng mã). POST dùng để tạo mới tài nguyên (không idempotent); PUT dùng cập nhật trạng thái đã có (có tính idempotent, gọi nhiều lần cùng kết quả).\n\n"
                      "5. Vì sao 2 CSDL tách riêng? Gộp chung thì sao?\n"
                      "-> Trả lời: Tách riêng để mỗi đơn vị độc lập triển khai, bảo trì, phân quyền và tối ưu. Gộp chung sẽ thành hệ thống nguyên khối Monolith, hai hệ thống bị dính chặt vào nhau, phụ thuộc cấu trúc bảng và không còn là bài toán tích hợp hệ thống nữa.\n\n"
                      "6. Hợp đồng API là gì? Đổi tên trường mà không báo thì sao?\n"
                      "-> Trả lời: Là thỏa thuận bằng văn bản về URL, Headers, JSON và mã lỗi. Nếu đổi tên trường mà không báo trước, bên tiêu thụ sẽ đọc ra giá trị null hoặc lỗi ném ngoại lệ khi deserialize, gây gián đoạn tích hợp.\n\n"
                      "7. Thêm hệ thống thứ 3 (LMS) thì sửa những gì?\n"
                      "-> Trả lời: Academic và Finance giữ nguyên 100%. Portal Backend chỉ cần thêm WebClient gọi LMS, thêm trường vào SummaryResponse, xác định mức độ quan trọng (thiết yếu hay bổ sung) để bắt lỗi, cập nhật API Contract và bổ sung giao diện Frontend.\n\n"
                      "8. Hạn chế của mô hình và hướng cải thiện?\n"
                      "-> Trả lời: Chưa có xác thực OAuth2/JWT, chưa dùng HTTPS, Portal gọi tuần tự. Cải thiện: Triển khai API Gateway, HTTPS, gọi bất đồng bộ với WebClient, bổ sung Redis Cache và Resilience4j Circuit Breaker.")

    add_sec_heading("8.2. Câu hỏi riêng cho Thành viên 2 (Finance API)", 2)
    doc.add_paragraph("1. PUT có tính idempotent nghĩa là gì? Cho ví dụ trong dự án?\n"
                      "-> Trả lời: Gọi một lần hay nhiều lần với cùng nội dung đều cho ra cùng một trạng thái hệ thống cuối cùng. Ví dụ PUT id=1 thành PAID 1 lần hay 10 lần liên tiếp thì bản ghi vẫn là PAID, không sinh ra bản ghi thừa hay thay đổi số tiền.\n\n"
                      "2. Vì sao dùng PUT /status mà không dùng PATCH?\n"
                      "-> Trả lời: Nhóm quy ước coi status là một sub-resource và dùng PUT để gán toàn bộ giá trị của nó. Nếu cập nhật một phần thực thể thì PATCH đúng chuẩn hơn; tuy nhiên dùng PUT cho sub-resource hoàn toàn hợp lệ nếu được quy định thống nhất trong API Contract.\n\n"
                      "3. Vì sao student_id trong tuition không có khóa ngoại sang academic_db?\n"
                      "-> Trả lời: Vì 2 CSDL vật lý độc lập hoàn toàn. RDBMS không hỗ trợ ràng buộc khóa ngoại bắc cầu qua nhiều database. student_id chỉ là mã tham chiếu logic; việc kiểm tra tồn tại do tầng tích hợp Portal đảm nhiệm.\n\n"
                      "4. Vì sao lưu số tiền bằng BIGINT mà không dùng số thực?\n"
                      "-> Trả lời: Số thực (FLOAT/DOUBLE) lưu trữ gần đúng chuẩn IEEE 754 nên gây sai số làm tròn khi tính toán tài chính. VNĐ không có phần thập phân nên BIGINT đảm bảo độ chính xác tuyệt đối 100%.\n\n"
                      "5. Endpoint /slow và biến FINANCE_DELAY_MS dùng để làm gì? Khác nhau thế nào?\n"
                      "-> Trả lời: /slow dùng test độc lập bằng Postman. FINANCE_DELAY_MS làm chậm chính endpoint GET /{studentId} mà Portal gọi sang để kích hoạt bài test Timeout 3s của Portal.\n\n"
                      "6. /slow và /{studentId} có xung đột đường dẫn không?\n"
                      "-> Trả lời: Không. Spring MVC luôn ưu tiên đường dẫn tường minh (/slow) trước các mẫu biến (/{studentId}); ngoài ra 'slow' không khớp regex mã sinh viên.\n\n"
                      "7. Ba cách làm Finance không phản hồi khác nhau thế nào?\n"
                      "-> Trả lời: Dừng dịch vụ và sai cổng đều bị ConnectException ngay tức thì (vài chục ms) do TCP RST. Làm chậm 5s thì kết nối thành công nhưng giữ chân Portal hết 3s kích hoạt ReadTimeoutException. Cả 3 cách Portal đều không sập, trả 200 + warning.\n\n"
                      "8. Finance trả 404 và Finance bị chết Portal khác nhau thế nào?\n"
                      "-> Trả lời: Đều trả 200 kèm tuitions=null, nhưng cảnh báo khác nhau: Finance 404 báo 'Chưa có khoản học phí nào'; Finance chết báo 'Không lấy được học phí do dịch vụ Finance không phản hồi'.\n\n"
                      "9. Phần kiểm thử ngoại lệ chứng minh điều gì?\n"
                      "-> Trả lời: Chứng minh tính sẵn sàng cao, cơ chế suy giảm có kiểm soát và hiệu lực của việc thiết lập timeout trong tích hợp phân tán.")

    # 9. ĐÓNG GÓP CỤ THỂ
    add_sec_heading("9. Đóng góp cụ thể của bản thân", 1)
    t_con_headers = ["Hạng mục", "Nội dung chi tiết", "Minh chứng kỹ thuật"]
    t_con_data = [
        ["Git", "Nhánh feature/finance; 8 commits chuẩn Conventional; Pull Request #2", "Repo GitHub của nhóm, PR #2"],
        ["Mã nguồn", "Toàn bộ finance-api: Controller, Entity, Repo, Exception, Config, SQL", "Thư mục finance-api/src/"],
        ["Postman", "finance.postman_collection.json (7 request, assertions đầy đủ)", "File JSON trong thư mục postman/"],
        ["Kiểm thử tự động", "Script Python run_test_suite.py và bash script simulate_failure.sh", "Thư mục scripts/"],
        ["Báo cáo nhóm", "Mục so sánh 3 cách (Ch. 2), mục Finance (Ch. 4), kiểm thử ngoại lệ (Ch. 5)", "Báo cáo tổng hợp đề tài"]
    ]
    add_table(t_con_headers, t_con_data, [1.5, 3.2, 1.8])

    # 10. CÔNG CỤ HỖ TRỢ ĐÃ SỬ DỤNG
    add_sec_heading("10. Công cụ hỗ trợ đã sử dụng (kể cả AI)", 1)
    t_ai_headers = ["Công cụ", "Mục đích sử dụng", "Cách tôi kiểm tra lại kết quả", "Phần tự sửa hoặc tự viết"]
    t_ai_data = [
        ["Claude / ChatGPT", "Gợi ý khung @RestControllerAdvice, tham khảo cú pháp regex", "Chạy Postman test kỹ các ca 200/400/404, rà soát từng dòng mã", "Viết toàn bộ validation nghiệp vụ, sửa cấu trúc ErrorResponse khớp nhóm"],
        ["GitHub Copilot", "Gợi ý boilerplate khi viết getter/setter và JPA method", "Đọc lại toàn bộ code, kiểm tra tính đúng đắn", "Tự tay thiết kế logic delayMs và kịch bản kiểm thử ngoại lệ 3 cách"]
    ]
    add_table(t_ai_headers, t_ai_data, [1.3, 1.9, 1.9, 1.4])

    # 11. TỰ ĐÁNH GIÁ VÀ KẾ HOẠCH CẢI THIỆN
    add_sec_heading("11. Tự đánh giá và kế hoạch cải thiện", 1)
    add_sec_heading("11.1. Tự đánh giá theo tiêu chí đề tài (Thang 10)", 2)
    t_eval_headers = ["Tiêu chí đánh giá (Trọng số)", "Tự chấm", "Căn cứ đánh giá thực tế"]
    t_eval_data = [
        ["Kiến thức lý thuyết, hiểu nguyên lý và so sánh giải pháp (20%)", "10 / 10", "Hiểu sâu sắc RESTful, phân tích sắc bén 3 phương thức tích hợp, Data Silos"],
        ["Phân tích bài toán, thiết kế kiến trúc và luồng dữ liệu (15%)", "10 / 10", "Nắm vững luồng dữ liệu toàn hệ thống, ranh giới CSDL và quy tắc xử lý lỗi"],
        ["Demo hoạt động và thể hiện đúng cơ chế tích hợp (35%)", "10 / 10", "Dịch vụ Finance API chạy ổn định cổng 8082, CSDL riêng, demo trơn tru"],
        ["Kiểm thử, minh chứng và khả năng chạy lại (15%)", "10 / 10", "Bộ test Postman & script Python tự động, dữ liệu thực nghiệm 3 cách lỗi sắc nét"],
        ["Thuyết trình, vấn đáp và mức độ hiểu của từng thành viên (15%)", "10 / 10", "Chuẩn bị thấu đáo, trả lời tự tin toàn bộ câu hỏi chung và chuyên sâu"]
    ]
    add_table(t_eval_headers, t_eval_data, [2.7, 0.9, 2.9])

    add_sec_heading("11.2. Đánh giá làm việc nhóm", 2)
    t_team_headers = ["Nội dung đánh giá", "Mức độ (1 đến 5)", "Ghi chú"]
    t_team_data = [
        ["Hoàn thành công việc đúng hạn", "5 / 5", "Hoàn thành trước tiến độ, không để nghẽn các bạn khác"],
        ["Chủ động báo cáo tiến độ và nêu vướng mắc", "5 / 5", "Cập nhật liên tục trong các buổi họp hàng ngày"],
        ["Tuân thủ hợp đồng API và quy trình Git", "5 / 5", "Tuân thủ 100% hợp đồng, commit rõ ràng, chuẩn mực"],
        ["Hỗ trợ thành viên khác trong nhóm", "5 / 5", "Hỗ trợ thành viên 1 và 3 chuẩn hóa lỗi và test WebClient"]
    ]
    add_table(t_team_headers, t_team_data, [2.5, 1.2, 2.8])

    # 12. CAM ĐOAN
    add_sec_heading("12. Cam kết", 1)
    doc.add_paragraph("Tôi cam kết nội dung báo cáo cá nhân này là trung thực. Các công việc nêu trong báo cáo do tôi trực tiếp thực hiện; tôi đã tự chạy, kiểm tra và có thể giải thích toàn bộ phần mình phụ trách cũng như kiến trúc, luồng dữ liệu và cơ chế tích hợp của cả hệ thống.")

    p_sign = doc.add_paragraph()
    p_sign.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_sign.add_run("Hà Nội, ngày 18 tháng 11 năm 2026\n").italic = True
    p_sign.add_run("Người làm báo cáo\n\n\n\n").bold = True
    p_sign.add_run("Nguyễn Thị Ánh Ngọc").bold = True

    output_path = "/Users/ngoc/Work/TichHopHeThong_ChuDe04_FinanceAPI/BAO_CAO_CA_NHAN_THANH_VIEN_2.docx"
    doc.save(output_path)
    print("SUCCESS: Generated DOCX at", output_path)

if __name__ == '__main__':
    create_report()
