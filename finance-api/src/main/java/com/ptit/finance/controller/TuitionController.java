package com.ptit.finance.controller;

import com.ptit.finance.dto.StatusRequest;
import com.ptit.finance.exception.BadRequestException;
import com.ptit.finance.exception.NotFoundException;
import com.ptit.finance.model.Tuition;
import com.ptit.finance.repository.TuitionRepository;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.regex.Pattern;

@RestController
@RequestMapping("/api/tuitions")
public class TuitionController {

    // Regex kiểm tra định dạng mã sinh viên PTIT (ví dụ: B22DCCN001)
    private static final Pattern ID_PATTERN = Pattern.compile("^B\\d{2}DC[A-Z]{2}\\d{3}$");

    private final TuitionRepository repo;

    @Value("${finance.delay-ms:0}")
    private long delayMs; // 0 = bình thường; đặt 5000 để giả lập Finance phản hồi chậm phục vụ kiểm thử timeout của Portal

    public TuitionController(TuitionRepository repo) {
        this.repo = repo;
    }

    /**
     * Lấy danh sách học phí theo mã sinh viên
     * GET /api/tuitions/{studentId}
     * Mã trả về: 200 (thành công), 400 (mã sai định dạng), 404 (chưa có học phí)
     */
    @GetMapping("/{studentId}")
    public List<Tuition> byStudent(@PathVariable String studentId) throws InterruptedException {
        if (delayMs > 0) {
            Thread.sleep(delayMs); // Giả lập độ trễ kiểm thử timeout phía Portal (3 giây)
        }

        if (studentId == null || !ID_PATTERN.matcher(studentId).matches()) {
            throw new BadRequestException("Mã sinh viên sai định dạng");
        }

        List<Tuition> list = repo.findByStudentId(studentId);
        if (list.isEmpty()) {
            throw new NotFoundException("Chưa có khoản học phí của " + studentId);
        }

        return list;
    }

    /**
     * Cập nhật trạng thái khoản học phí
     * PUT /api/tuitions/{id}/status
     * Body: {"status": "PAID"} hoặc {"status": "UNPAID"}
     * Mã trả về: 200 (cập nhật thành công), 400 (status không hợp lệ), 404 (không tìm thấy id)
     */
    @PutMapping("/{id}/status")
    public Tuition updateStatus(@PathVariable Long id, @RequestBody(required = false) StatusRequest req) {
        if (req == null || req.status() == null || (!"PAID".equals(req.status()) && !"UNPAID".equals(req.status()))) {
            throw new BadRequestException("Trạng thái chỉ nhận PAID hoặc UNPAID");
        }

        Tuition t = repo.findById(id).orElseThrow(
                () -> new NotFoundException("Không tìm thấy khoản học phí " + id)
        );

        t.setStatus(req.status());
        return repo.save(t);
    }

    /**
     * Endpoint kiểm thử làm chậm có chủ đích
     * GET /api/tuitions/slow?delay=5000
     * Chỉ dùng kiểm thử Postman, không dùng trong luồng nghiệp vụ chính
     */
    @GetMapping("/slow")
    public List<Tuition> slow(@RequestParam(defaultValue = "5000") long delay) throws InterruptedException {
        Thread.sleep(delay);
        return repo.findAll();
    }
}
