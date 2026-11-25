-- Du lieu sinh vien gia lap cho demo Academic API (UTF-8).
-- B22: khoa nhap hoc 2022; DC: ma co dinh; CN: Cong nghe;
-- 001-012: so thu tu trong danh sach lop.
-- Email theo mau: Ten + chu cai dau ho/ten dem + ma sinh vien.
-- ON CONFLICT giup co the nap lai file ma khong tao ban ghi trung.
INSERT INTO student (student_id, full_name, email, class_name, major) VALUES
    ('B22DCCN001', 'Nguyễn Minh An',     'AnNM.b22cn001@stu.ptit.edu.vn',     'D22CQCN01-B', 'Công nghệ thông tin'),
    ('B22DCCN002', 'Trần Gia Bảo',       'BaoTG.b22cn002@stu.ptit.edu.vn',   'D22CQCN01-B', 'Công nghệ thông tin'),
    ('B22DCCN003', 'Lê Hoàng Chi',       'ChiLH.b22cn003@stu.ptit.edu.vn',    'D22CQCN01-B', 'Công nghệ thông tin'),
    ('B22DCCN004', 'Phạm Đức Duy',       'DuyPD.b22cn004@stu.ptit.edu.vn',    'D22CQCN02-B', 'Công nghệ thông tin'),
    ('B22DCCN005', 'Võ Khánh Giang',     'GiangVK.b22cn005@stu.ptit.edu.vn',  'D22CQCN02-B', 'Công nghệ thông tin'),
    ('B22DCCN006', 'Đặng Quốc Huy',      'HuyDQ.b22cn006@stu.ptit.edu.vn',    'D22CQCN02-B', 'Công nghệ thông tin'),
    ('B22DCCN007', 'Bùi Thảo Linh',      'LinhBT.b22cn007@stu.ptit.edu.vn',   'D22CQCN03-B', 'Công nghệ thông tin'),
    ('B22DCCN008', 'Đỗ Thành Nam',       'NamDT.b22cn008@stu.ptit.edu.vn',    'D22CQCN03-B', 'Công nghệ thông tin'),
    ('B22DCCN009', 'Hoàng Ngọc Phúc',    'PhucHN.b22cn009@stu.ptit.edu.vn',   'D22CQCN03-B', 'Công nghệ thông tin'),
    ('B22DCCN010', 'Vũ Mai Quỳnh',       'QuynhVM.b22cn010@stu.ptit.edu.vn',  'D22CQCN04-B', 'Công nghệ thông tin'),
    ('B22DCCN011', 'Nguyễn Tuấn Kiệt',   'KietNT.b22cn011@stu.ptit.edu.vn',   'D22CQCN04-B', 'Công nghệ thông tin'),
    ('B22DCCN012', 'Phạm Yến Nhi',       'NhiPY.b22cn012@stu.ptit.edu.vn',    'D22CQCN04-B', 'Công nghệ thông tin')
ON CONFLICT (student_id) DO NOTHING;
