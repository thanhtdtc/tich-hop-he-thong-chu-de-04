package com.ptit.integration.academic.student;

import org.springframework.stereotype.Service;

import java.util.regex.Pattern;

@Service
public class StudentService {
    private static final Pattern STUDENT_ID_PATTERN = Pattern.compile("^B\\d{2}DC[A-Z]{2}\\d{3}$");

    private final StudentRepository studentRepository;

    public StudentService(StudentRepository studentRepository) {
        this.studentRepository = studentRepository;
    }

    public Student getStudent(String studentId) {
        validateStudentId(studentId);
        return studentRepository.findByStudentId(studentId)
                .orElseThrow(() -> new StudentNotFoundException(studentId));
    }

    public Student createStudent(CreateStudentRequest request) {
        validateStudentId(request.studentId());
        return studentRepository.save(new Student(
                request.studentId(), request.fullName().trim(), request.email().trim(),
                request.className().trim(), request.major().trim()
        ));
    }

    private void validateStudentId(String studentId) {
        if (studentId == null || !STUDENT_ID_PATTERN.matcher(studentId).matches()) {
            throw new InvalidStudentIdException(studentId);
        }
    }
}

