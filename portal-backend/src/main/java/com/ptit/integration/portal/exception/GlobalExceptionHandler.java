package com.ptit.integration.portal.exception;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(BadRequestException.class)
    public ResponseEntity<ApiError> badRequest(BadRequestException e) {
        return build(400, "BAD_REQUEST", e.getMessage());
    }

    @ExceptionHandler(NotFoundException.class)
    public ResponseEntity<ApiError> notFound(NotFoundException e) {
        return build(404, "NOT_FOUND", e.getMessage());
    }

    @ExceptionHandler(ServiceUnavailableException.class)
    public ResponseEntity<ApiError> unavailable(ServiceUnavailableException e) {
        return build(503, "SERVICE_UNAVAILABLE", e.getMessage());
    }

    private ResponseEntity<ApiError> build(int status, String error, String message) {
        return ResponseEntity.status(status).body(new ApiError(status, error, message));
    }
}