package com.ptit.integration.academic.student;

import java.util.Optional;

public interface StudentRepository {
    Optional<Student> findByStudentId(String studentId);

    Student save(Student student);
}

