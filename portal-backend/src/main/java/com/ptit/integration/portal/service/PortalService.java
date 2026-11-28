package com.ptit.integration.portal.service;

import com.ptit.integration.portal.dto.*;
import com.ptit.integration.portal.exception.*;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.regex.Pattern;

@Service
public class PortalService {
    private static final Pattern ID = Pattern.compile("^B\\d{2}DC[A-Z]{2}\\d{3}$");

    public SummaryResponse summary(String id) {
        if (!ID.matcher(id).matches())
            throw new BadRequestException("Mã sinh viên sai định dạng");
        if (id.equals("B22DCCN999"))
            throw new NotFoundException("Không tìm thấy sinh viên " + id);
        if (id.equals("B22DCCN503"))
            throw new ServiceUnavailableException("Hệ thống đào tạo không phản hồi");

        StudentDto student = new StudentDto(id, "Nguyen Van A",
                "a@stu.ptit.edu.vn", "D22CQCN01-B", "CNTT");

        if (id.equals("B22DCCN002")) // giả lập Finance lỗi
            return new SummaryResponse(student, null,
                    List.of("Không lấy được học phí: Finance API không phản hồi"));

        List<TuitionDto> tuitions = List.of(
                new TuitionDto(1L, id, "2026-1", 8500000L, "UNPAID", "2026-12-15"),
                new TuitionDto(2L, id, "2025-2", 8200000L, "PAID", "2026-05-15"));
        return new SummaryResponse(student, tuitions, List.of());
    }
}