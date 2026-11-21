package com.ptit.integration.portal.controller;

import com.ptit.integration.portal.dto.SummaryResponse;
import com.ptit.integration.portal.service.PortalService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/portal")
public class PortalController {

    private final PortalService service;

    public PortalController(PortalService service) {
        this.service = service;
    }

    @GetMapping("/students/{studentId}/summary")
    public SummaryResponse summary(@PathVariable String studentId) {
        return service.summary(studentId);
    }
}