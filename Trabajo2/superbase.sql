-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-10-2025 a las 21:27:23
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `superbase`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `arriendos`
--

CREATE TABLE `arriendos` (
  `num_arriendo` int(11) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_entrega` date NOT NULL,
  `costo_total` int(11) NOT NULL,
  `run_cliente` varchar(15) DEFAULT NULL,
  `codigo_empleado` int(11) DEFAULT NULL,
  `patente_vehiculo` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `run` varchar(15) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `codigo` int(11) NOT NULL,
  `run` varchar(15) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `cargo` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`codigo`, `run`, `nombre`, `apellido`, `cargo`, `password`) VALUES
(1, '22206401-5', 'Matias', 'Flores', 'admin', '$2b$12$3V11whxZprgMPTCX/8jJLOgCAs3tANamVu.8AgtlyZOnpOeYMWTbW');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculos`
--

CREATE TABLE `vehiculos` (
  `patente` varchar(10) NOT NULL,
  `marca` varchar(50) NOT NULL,
  `modelo` varchar(50) NOT NULL,
  `anio` int(11) NOT NULL,
  `precio` float NOT NULL,
  `disponible` enum('SI','NO') DEFAULT 'SI'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

ALTER TABLE vehiculos MODIFY disponible BOOLEAN DEFAULT TRUE;
--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `arriendos`
--
ALTER TABLE `arriendos`
  ADD PRIMARY KEY (`num_arriendo`),
  ADD KEY `run_cliente` (`run_cliente`),
  ADD KEY `codigo_empleado` (`codigo_empleado`),
  ADD KEY `patente_vehiculo` (`patente_vehiculo`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`run`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`codigo`),
  ADD UNIQUE KEY `run` (`run`);

--
-- Indices de la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD PRIMARY KEY (`patente`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `arriendos`
--
ALTER TABLE `arriendos`
  MODIFY `num_arriendo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `arriendos`
--
ALTER TABLE `arriendos`
  ADD CONSTRAINT `arriendos_ibfk_1` FOREIGN KEY (`run_cliente`) REFERENCES `clientes` (`run`),
  ADD CONSTRAINT `arriendos_ibfk_2` FOREIGN KEY (`codigo_empleado`) REFERENCES `empleados` (`codigo`),
  ADD CONSTRAINT `arriendos_ibfk_3` FOREIGN KEY (`patente_vehiculo`) REFERENCES `vehiculos` (`patente`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
