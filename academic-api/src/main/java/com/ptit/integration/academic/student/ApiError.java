package com.ptit.integration.academic.student;

public record ApiError(int status, String error, String message) {
}

