-- schema.sql
-- Khởi tạo bảng tuition cho hệ thống Finance
-- Lưu ý: Không có khóa ngoại sang academic_db vì hai CSDL độc lập hoàn toàn

CREATE TABLE IF NOT EXISTS tuition (
    id         BIGSERIAL   PRIMARY KEY,
    student_id VARCHAR(12) NOT NULL,
    semester   VARCHAR(10) NOT NULL,
    amount     BIGINT      NOT NULL CHECK (amount > 0),
    status     VARCHAR(10) NOT NULL CHECK (status IN ('PAID', 'UNPAID')),
    due_date   DATE,
    CONSTRAINT uq_tuition UNIQUE (student_id, semester)
);

CREATE INDEX IF NOT EXISTS idx_tuition_student ON tuition(student_id);
