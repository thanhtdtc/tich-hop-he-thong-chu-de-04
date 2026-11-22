package com.ptit.finance.model;

import jakarta.persistence.*;
import java.time.LocalDate;

@Entity
@Table(name = "tuition")
public class Tuition {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "student_id", nullable = false, length = 12)
    private String studentId; // Mã tham chiếu, KHÔNG có khóa ngoại sang academic_db

    @Column(nullable = false, length = 10)
    private String semester;

    @Column(nullable = false)
    private Long amount; // VNĐ, kiểu số nguyên tránh sai số làm tròn

    @Column(nullable = false, length = 10)
    private String status; // PAID | UNPAID

    @Column(name = "due_date")
    private LocalDate dueDate;

    public Tuition() {
    }

    public Tuition(Long id, String studentId, String semester, Long amount, String status, LocalDate dueDate) {
        this.id = id;
        this.studentId = studentId;
        this.semester = semester;
        this.amount = amount;
        this.status = status;
        this.dueDate = dueDate;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getStudentId() {
        return studentId;
    }

    public void setStudentId(String studentId) {
        this.studentId = studentId;
    }

    public String getSemester() {
        return semester;
    }

    public void setSemester(String semester) {
        this.semester = semester;
    }

    public Long getAmount() {
        return amount;
    }

    public void setAmount(Long amount) {
        this.amount = amount;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public LocalDate getDueDate() {
        return dueDate;
    }

    public void setDueDate(LocalDate dueDate) {
        this.dueDate = dueDate;
    }
}
