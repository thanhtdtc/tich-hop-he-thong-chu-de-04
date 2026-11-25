package com.ptit.integration.academic.student;

public class StudentAlreadyExistsException extends RuntimeException {
    public StudentAlreadyExistsException(String studentId) {
        super("Mã sinh viên đã tồn tại: " + studentId);
    }
}

