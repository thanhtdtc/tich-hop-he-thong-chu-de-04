package com.ptit.integration.portal.exception;

public record ApiError(int status, String error, String message) {
}