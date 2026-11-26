package com.ptit.integration.academic.student;

public class StudentNotFoundException extends RuntimeException {
    public StudentNotFoundException(String studentId) {
        super("Không tìm thấy sinh viên " + studentId);
    }
}

