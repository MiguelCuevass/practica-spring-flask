package com.sistemasdistr.basico.config;

import com.sistemasdistr.basico.model.Role;
import com.sistemasdistr.basico.model.User;
import com.sistemasdistr.basico.repository.RoleRepository;
import com.sistemasdistr.basico.repository.UserRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

import java.time.LocalDateTime;

@Component
public class DataInitializer implements CommandLineRunner {

    private final UserRepository userRepository;
    private final RoleRepository roleRepository;
    private final PasswordEncoder passwordEncoder;

    public DataInitializer(UserRepository userRepository,
                           RoleRepository roleRepository,
                           PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.roleRepository = roleRepository;
        this.passwordEncoder = passwordEncoder;
    }

    @Override
    public void run(String... args) {

        User usuarioAdmin = userRepository.findUserByUsername("admin");

        if (usuarioAdmin == null) {

            Role rolAdmin = new Role();
            rolAdmin.setRoleName("ROLE_ADMIN");
            rolAdmin.setShowOnCreate(1);
            rolAdmin = roleRepository.save(rolAdmin);

            User admin = new User();
            admin.setUsername("admin");
            admin.setEmailuser("admin@admin.com");
            admin.setNombreUsuario("Administrador");
            admin.setPassword(passwordEncoder.encode("admin"));
            admin.setPublickey(null);
            admin.setFechaUltimoAcceso(LocalDateTime.now());
            admin.setUserRole(rolAdmin);

            userRepository.save(admin);

            System.out.println("Usuario admin creado en la base de datos");
        }
    }
}