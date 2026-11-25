CREATE TABLE IF NOT EXISTS student (
    student_id VARCHAR(12) PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    class_name VARCHAR(50) NOT NULL,
    major VARCHAR(50) NOT NULL,
    CONSTRAINT chk_student_id_format
        CHECK (student_id ~ '^B[0-9]{2}DC[A-Z]{2}[0-9]{3}$')
);
