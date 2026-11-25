package com.ptit.finance;

import com.ptit.finance.controller.TuitionController;
import com.ptit.finance.model.Tuition;
import com.ptit.finance.repository.TuitionRepository;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.test.context.bean.override.mockito.MockitoBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import java.time.LocalDate;
import java.util.Collections;
import java.util.List;
import java.util.Optional;

import static org.mockito.ArgumentMatchers.any;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.put;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(TuitionController.class)
public class TuitionControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockitoBean
    private TuitionRepository repo;

    @Test
    @DisplayName("GET /api/tuitions/B22DCCN001 - Thành công 200 OK")
    void testGetTuitionSuccess() throws Exception {
        Tuition t1 = new Tuition(1L, "B22DCCN001", "2026-1", 8500000L, "UNPAID", LocalDate.of(2026, 12, 15));
        Mockito.when(repo.findByStudentId("B22DCCN001")).thenReturn(List.of(t1));

        mockMvc.perform(get("/api/tuitions/B22DCCN001"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$[0].studentId").value("B22DCCN001"))
                .andExpect(jsonPath("$[0].amount").value(8500000))
                .andExpect(jsonPath("$[0].status").value("UNPAID"));
    }

    @Test
    @DisplayName("GET /api/tuitions/B22DCCN011 - Sinh viên chưa có học phí trả 404 Not Found")
    void testGetTuitionNotFound() throws Exception {
        Mockito.when(repo.findByStudentId("B22DCCN011")).thenReturn(Collections.emptyList());

        mockMvc.perform(get("/api/tuitions/B22DCCN011"))
                .andExpect(status().isNotFound())
                .andExpect(jsonPath("$.status").value(404))
                .andExpect(jsonPath("$.error").value("NOT_FOUND"));
    }

    @Test
    @DisplayName("GET /api/tuitions/abc123 - Mã sinh viên sai định dạng trả 400 Bad Request")
    void testGetTuitionBadRequest() throws Exception {
        mockMvc.perform(get("/api/tuitions/abc123"))
                .andExpect(status().isBadRequest())
                .andExpect(jsonPath("$.status").value(400))
                .andExpect(jsonPath("$.error").value("BAD_REQUEST"))
                .andExpect(jsonPath("$.message").value("Mã sinh viên sai định dạng"));
    }

    @Test
    @DisplayName("PUT /api/tuitions/1/status - Cập nhật PAID thành công 200 OK")
    void testPutStatusSuccess() throws Exception {
        Tuition t1 = new Tuition(1L, "B22DCCN001", "2026-1", 8500000L, "UNPAID", LocalDate.of(2026, 12, 15));
        Tuition updated = new Tuition(1L, "B22DCCN001", "2026-1", 8500000L, "PAID", LocalDate.of(2026, 12, 15));

        Mockito.when(repo.findById(1L)).thenReturn(Optional.of(t1));
        Mockito.when(repo.save(any(Tuition.class))).thenReturn(updated);

        mockMvc.perform(put("/api/tuitions/1/status")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"status\":\"PAID\"}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.status").value("PAID"));
    }

    @Test
    @DisplayName("PUT /api/tuitions/1/status - Trạng thái không hợp lệ trả 400 Bad Request")
    void testPutStatusInvalid() throws Exception {
        mockMvc.perform(put("/api/tuitions/1/status")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"status\":\"DONE\"}"))
                .andExpect(status().isBadRequest())
                .andExpect(jsonPath("$.status").value(400))
                .andExpect(jsonPath("$.error").value("BAD_REQUEST"));
    }

    @Test
    @DisplayName("PUT /api/tuitions/abc/status - ID không phải số trả 400 Bad Request")
    void testPutStatusIdNotNumber() throws Exception {
        mockMvc.perform(put("/api/tuitions/abc/status")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"status\":\"PAID\"}"))
                .andExpect(status().isBadRequest())
                .andExpect(jsonPath("$.status").value(400))
                .andExpect(jsonPath("$.error").value("BAD_REQUEST"));
    }
}
