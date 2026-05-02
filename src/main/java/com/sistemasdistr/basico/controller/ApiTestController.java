package com.sistemasdistr.basico.controller;

import com.sistemasdistr.basico.service.api.PythonApiService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class ApiTestController {

    private final PythonApiService pythonApiService;

    public ApiTestController(PythonApiService pythonApiService) {
        this.pythonApiService = pythonApiService;
    }

    @GetMapping("/api-test")
    public String apiTest() {
        return "api-test";
    }

    @GetMapping("/api-test/archivo-ok")
    public String archivoOk(Model model) {
        String respuesta = pythonApiService.llamarApiPython("/api/archivo/ok");
        model.addAttribute("respuesta", respuesta);
        return "api-test";
    }

    @GetMapping("/api-test/archivo-error")
    public String archivoError(Model model) {
        String respuesta = pythonApiService.llamarApiPython("/api/archivo/error");
        model.addAttribute("respuesta", respuesta);
        return "api-test";
    }

    @GetMapping("/api-test/db-ok")
    public String dbOk(Model model) {
        String respuesta = pythonApiService.llamarApiPython("/api/db/ok");
        model.addAttribute("respuesta", respuesta);
        return "api-test";
    }

    @GetMapping("/api-test/db-error")
    public String dbError(Model model) {
        String respuesta = pythonApiService.llamarApiPython("/api/db/error");
        model.addAttribute("respuesta", respuesta);
        return "api-test";
    }

    @GetMapping("/api-test/pokemon-ok")
    public String pokemonOk(Model model) {
        String respuesta = pythonApiService.llamarApiPython("/api/pokemon/ok");
        model.addAttribute("respuesta", respuesta);
        return "api-test";
    }

    @GetMapping("/api-test/pokemon-error")
    public String pokemonError(Model model) {
        String respuesta = pythonApiService.llamarApiPython("/api/pokemon/error");
        model.addAttribute("respuesta", respuesta);
        return "api-test";
    }
}