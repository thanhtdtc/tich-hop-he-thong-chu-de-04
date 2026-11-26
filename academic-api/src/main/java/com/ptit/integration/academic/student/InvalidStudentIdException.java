package com.ptit.integration.academic.student;

public class InvalidStudentIdException extends RuntimeException {
    public InvalidStudentIdException(String studentId) {
        super("Mã sinh viên không đúng định dạng: " + studentId);
    }
}

