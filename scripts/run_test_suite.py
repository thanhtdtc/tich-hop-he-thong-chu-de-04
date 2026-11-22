#!/usr/bin/env python3
"""
PTIT - System Integration - Topic 04
Test Suite for Finance API (Thành viên 2)
Author: Nguyen Thi Anh Ngoc
"""

import sys
import time
import json
import urllib.request
import urllib.error

BASE_URL = "http://localhost:8082"

def make_request(method, path, body=None, timeout=10):
    url = f"{BASE_URL}{path}"
    headers = {"Accept": "application/json"}
    data = None
    if body is not None:
        data = json.dumps(body).encode('utf-8')
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    start_time = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            duration_ms = int((time.time() - start_time) * 1000)
            status_code = response.getcode()
            response_body = response.read().decode('utf-8')
            try:
                parsed_json = json.loads(response_body)
            except Exception:
                parsed_json = response_body
            return {
                "status": status_code,
                "body": parsed_json,
                "duration_ms": duration_ms,
                "error": None
            }
    except urllib.error.HTTPError as e:
        duration_ms = int((time.time() - start_time) * 1000)
        status_code = e.code
        try:
            error_body = json.loads(e.read().decode('utf-8'))
        except Exception:
            error_body = None
        return {
            "status": status_code,
            "body": error_body,
            "duration_ms": duration_ms,
            "error": str(e)
        }
    except Exception as e:
        duration_ms = int((time.time() - start_time) * 1000)
        return {
            "status": 0,
            "body": None,
            "duration_ms": duration_ms,
            "error": str(e)
        }

def run_all_tests():
    print("=" * 70)
    print("PTIT CHỦ ĐỀ 04: KIỂM THỬ FINANCE API (CỔNG 8082)")
    print("=" * 70)

    test_cases = [
        {
            "id": "F1",
            "name": "GET học phí sinh viên B22DCCN001 (Thành công)",
            "method": "GET",
            "path": "/api/tuitions/B22DCCN001",
            "body": None,
            "expected_status": 200,
        },
        {
            "id": "F2",
            "name": "GET học phí sinh viên B22DCCN013 (Chưa có học phí)",
            "method": "GET",
            "path": "/api/tuitions/B22DCCN013",
            "body": None,
            "expected_status": 404,
        },
        {
            "id": "F3",
            "name": "GET học phí mã sinh viên abc123 (Sai định dạng)",
            "method": "GET",
            "path": "/api/tuitions/abc123",
            "body": None,
            "expected_status": 400,
        },
        {
            "id": "F4",
            "name": "PUT cập nhật học phí id=1 sang PAID (Hợp lệ)",
            "method": "PUT",
            "path": "/api/tuitions/1/status",
            "body": {"status": "PAID"},
            "expected_status": 200,
        },
        {
            "id": "F5",
            "name": "PUT cập nhật học phí id=1 trạng thái DONE (Không hợp lệ)",
            "method": "PUT",
            "path": "/api/tuitions/1/status",
            "body": {"status": "DONE"},
            "expected_status": 400,
        },
        {
            "id": "F6",
            "name": "PUT cập nhật học phí id=9999 (Không tồn tại)",
            "method": "PUT",
            "path": "/api/tuitions/9999/status",
            "body": {"status": "PAID"},
            "expected_status": 404,
        },
        {
            "id": "F7",
            "name": "GET /slow?delay=2000 (Kiểm tra cơ chế làm chậm)",
            "method": "GET",
            "path": "/api/tuitions/slow?delay=2000",
            "body": None,
            "expected_status": 200,
        }
    ]

    passed_count = 0

    for tc in test_cases:
        print(f"\n[{tc['id']}] {tc['name']}")
        print(f"       -> Request: {tc['method']} {tc['path']}")
        res = make_request(tc['method'], tc['path'], tc['body'])
        status_ok = res['status'] == tc['expected_status']
        if status_ok:
            passed_count += 1
            status_text = "PASS"
        else:
            status_text = "FAIL"

        print(f"       -> Kết quả: {status_text} | Status: {res['status']} (Kỳ vọng: {tc['expected_status']}) | Thời gian: {res['duration_ms']}ms")
        print(f"       -> Phản hồi: {json.dumps(res['body'], ensure_ascii=False)[:120]}...")

    print("\n" + "=" * 70)
    print(f"KẾT QUẢ KIỂM THỬ: {passed_count}/{len(test_cases)} ca thành công.")
    print("=" * 70)

if __name__ == "__main__":
    run_all_tests()
