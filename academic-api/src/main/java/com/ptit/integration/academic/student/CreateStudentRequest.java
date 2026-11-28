package com.ptit.integration.academic.student;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;
import jakarta.validation.constraints.Size;

public record CreateStudentRequest(
        @NotBlank(message = "studentId không được để trống")
        @Pattern(regexp = "^B\\d{2}DC[A-Z]{2}\\d{3}$", message = "studentId không đúng định dạng")
        String studentId,

        @NotBlank(message = "fullName không được để trống")
        @Size(max = 100, message = "fullName tối đa 100 ký tự")
        String fullName,

        @NotBlank(message = "email không được để trống")
        @Email(message = "email không đúng định dạng")
        @Size(max = 100, message = "email tối đa 100 ký tự")
        String email,

        @NotBlank(message = "className không được để trống")
        @Size(max = 50, message = "className tối đa 50 ký tự")
        String className,

        @NotBlank(message = "major không được để trống")
        @Size(max = 50, message = "major tối đa 50 ký tự")
        String major
) {
}

