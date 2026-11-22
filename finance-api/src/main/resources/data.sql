-- data.sql
-- Nạp dữ liệu mẫu ban đầu: Mỗi sinh viên 1 đến 3 khoản học phí, có cả PAID và UNPAID

INSERT INTO tuition (student_id, semester, amount, status, due_date) VALUES
('B22DCCN001', '2026-1', 8500000, 'UNPAID', '2026-12-15'),
('B22DCCN001', '2025-2', 8200000, 'PAID',   '2026-05-15'),
('B22DCCN002', '2026-1', 8500000, 'PAID',   '2026-12-15');
