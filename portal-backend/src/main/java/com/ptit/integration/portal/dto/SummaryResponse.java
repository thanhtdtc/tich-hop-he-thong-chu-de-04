package com.ptit.integration.portal.dto;

import java.util.List;

public record SummaryResponse(StudentDto student, List<TuitionDto> tuitions,
        List<String> warnings) {
}