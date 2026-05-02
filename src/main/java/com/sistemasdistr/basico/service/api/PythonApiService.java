package com.sistemasdistr.basico.service.api;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;

@Service
public class PythonApiService {

    private final RestTemplate restTemplate;

    public PythonApiService() {
        this.restTemplate = new RestTemplate();
    }

    public String llamarApiPython(String endpoint) {
        try {
            String url = "http://python-api:5000" + endpoint;
            return restTemplate.getForObject(url, String.class);
        } catch (RestClientException e) {
            return "Error al llamar a la API Python: " + e.getMessage();
        }
    }
}