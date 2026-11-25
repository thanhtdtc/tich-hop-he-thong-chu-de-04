package com.ptit.integration.academic.student;

import org.springframework.dao.DuplicateKeyException;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public class JdbcStudentRepository implements StudentRepository {
    private static final RowMapper<Student> STUDENT_ROW_MAPPER = (rs, rowNum) -> new Student(
            rs.getString("student_id"),
            rs.getString("full_name"),
            rs.getString("email"),
            rs.getString("class_name"),
            rs.getString("major")
    );

    private final JdbcTemplate jdbcTemplate;

    public JdbcStudentRepository(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    @Override
    public Optional<Student> findByStudentId(String studentId) {
        return jdbcTemplate.query(
                "SELECT student_id, full_name, email, class_name, major FROM student WHERE student_id = ?",
                STUDENT_ROW_MAPPER,
                studentId
        ).stream().findFirst();
    }

    @Override
    public Student save(Student student) {
        try {
            jdbcTemplate.update(
                    "INSERT INTO student (student_id, full_name, email, class_name, major) VALUES (?, ?, ?, ?, ?)",
                    student.studentId(), student.fullName(), student.email(), student.className(), student.major()
            );
            return student;
        } catch (DuplicateKeyException exception) {
            throw new StudentAlreadyExistsException(student.studentId());
        }
    }
}

