package com.ptit.integration.portal.dto;

public record TuitionDto(Long id, String studentId, String semester,
        Long amount, String status, String dueDate) {
}