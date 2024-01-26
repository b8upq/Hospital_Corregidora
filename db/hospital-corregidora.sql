CREATE database hospital_corregidora;

use hospital_corregidora;


CREATE TABLE `personas` (
    `PersonaID` int NOT NULL AUTO_INCREMENT,
    `Nombre` varchar(255) DEFAULT NULL,
    `ApellidoPaterno` varchar(255) DEFAULT NULL,
    `ApellidoMaterno` varchar(255) DEFAULT NULL,
    `Edad` int DEFAULT NULL,
    `Sexo` char DEFAULT NULL,
    PRIMARY KEY (`PersonaID`)
)

CREATE TABLE `pacientes` (
    `PacienteID` int NOT NULL AUTO_INCREMENT,
    `PersonaID` int NOT NULL,
    PRIMARY KEY (`PacienteID`),
    FOREIGN KEY (`PersonaID`) REFERENCES `personas` (`PersonaID`)
)

CREATE TABLE `consultorios` (
    `ConsultorioID` int NOT NULL AUTO_INCREMENT,
    `NombreConsultorio` varchar(255) DEFAULT NULL,
    PRIMARY KEY (`ConsultorioID`)
)

CREATE TABLE `medicos` (
    `MedicoID` int NOT NULL AUTO_INCREMENT,
    `PersonaID` int NOT NULL,
    `consultorioID` int NOT NULL,
    PRIMARY KEY (`MedicoID`),
    FOREIGN KEY (`PersonaID`) REFERENCES `personas` (`PersonaID`),
    FOREIGN KEY (`consultorioID`) REFERENCES `consultorios` (`ConsultorioID`)
)

CREATE TABLE `diagnosticos` (
    `DiagnosticoID` int NOT NULL AUTO_INCREMENT,
    `PacienteID` int NOT NULL,
    `MedicoID` int NOT NULL,
    `FechaConsulta` date DEFAULT NULL,
    `Enfermedad` varchar(255) DEFAULT NULL,
    `Descripcion` varchar(255) DEFAULT NULL,
    PRIMARY KEY (`DiagnosticoID`),
    FOREIGN KEY (`PacienteID`) REFERENCES `pacientes` (`PacienteID`),
    FOREIGN KEY (`MedicoID`) REFERENCES `medicos` (`MedicoID`)
)

-- Inserciones a la base de datos

INSERT INTO `consultorios` (`NombreConsultorio`) 
VALUES ('Consultorio 1'), ('Consultorio 2'), ('Consultorio 3');

INSERT INTO `personas` (`Nombre`, `ApellidoPaterno`, `ApellidoMaterno`, `Edad`, `Sexo`)
VALUES ('Juan', 'Perez', 'Lopez', 25, 'M'), ('Maria', 'Gonzalez', 'Garcia', 30, 'F'), ('Pedro', 'Gomez', 'Gonzalez', 35, 'M');

INSERT INTO `medicos` (`PersonaID`, `consultorioID`)
VALUES (1, 1), (2, 2), (3, 3);