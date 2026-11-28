package com.ptit.integration.portal.dto;

public record StudentDto(String studentId, String fullName, String email,
        String className, String major) {
}