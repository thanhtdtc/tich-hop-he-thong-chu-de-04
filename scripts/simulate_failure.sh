#!/usr/bin/env bash
# Script minh họa 3 kịch bản kiểm thử Finance không phản hồi
# Tác giả: Thành viên 2 (Finance API và kiểm thử lỗi)

echo "======================================================================"
echo "PTIT CHỦ ĐỀ 04: KIỂM THỬ NGOẠI LỆ FINANCE KHÔNG PHẢN HỒI (3 CÁCH)"
echo "======================================================================"

echo ""
echo "--- CÁCH A: Dừng dịch vụ finance-api ---"
echo "Lệnh: docker compose stop finance-api"
echo "Hiện tượng Portal: Kết nối bị từ chối ngay (ConnectException);"
echo "Portal không sập, trả về HTTP 200, tuitions = null, warnings = ['Không lấy được học phí']"
echo "Thời gian phản hồi: Rất nhanh (~10-30ms)"

echo ""
echo "--- CÁCH B: Làm chậm Finance 5 giây (FINANCE_DELAY_MS=5000) ---"
echo "Lệnh: FINANCE_DELAY_MS=5000 docker compose up -d finance-api"
echo "Hiện tượng Portal: Chờ khoảng 3000ms thì xảy ra ReadTimeoutException;"
echo "Portal suy giảm có kiểm soát (graceful degradation), trả 200, tuitions = null, có warning"
echo "Thời gian phản hồi: Khoảng 3000 - 3050ms (đúng ngưỡng timeout thiết lập)"

echo ""
echo "--- CÁCH C: Cấu hình Portal trỏ sai cổng Finance (ví dụ: port 9999) ---"
echo "Lệnh: Cấu hình FINANCE_URL=http://localhost:9999 trong Portal Backend"
echo "Hiện tượng Portal: Bị từ chối kết nối ngay lập tức (Connection Refused);"
echo "Portal xử lý tương tự Cách a, trả 200, tuitions = null, có warning"
echo "Thời gian phản hồi: Rất nhanh (~15ms)"

echo ""
echo "======================================================================"
echo "KẾT LUẬN: Cả 3 cách đều chứng minh cơ chế Graceful Degradation của Portal"
echo "======================================================================"
