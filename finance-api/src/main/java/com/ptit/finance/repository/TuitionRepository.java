package com.ptit.finance.repository;

import com.ptit.finance.model.Tuition;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface TuitionRepository extends JpaRepository<Tuition, Long> {
    List<Tuition> findByStudentId(String studentId);
}
