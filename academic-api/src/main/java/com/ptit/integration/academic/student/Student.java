package com.ptit.integration.academic.student;

public record Student(
        String studentId,
        String fullName,
        String email,
        String className,
        String major
) {
}

