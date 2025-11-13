-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-11-2025 a las 21:27:51
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
  `costo_total_uf` float NOT NULL,
  `run_cliente` varchar(15) NOT NULL,
  `codigo_empleado` int(11) NOT NULL,
  `patente_vehiculo` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `arriendos`
--

INSERT INTO `arriendos` (`num_arriendo`, `fecha_inicio`, `fecha_entrega`, `costo_total_uf`, `run_cliente`, `codigo_empleado`, `patente_vehiculo`) VALUES
(1, '2025-11-13', '2026-01-10', 1000, '22317589-9', 1, 'ABCD-23');

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

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`run`, `nombre`, `apellido`, `direccion`, `telefono`) VALUES
('22317589-9', 'Isabel', 'Araya', 'Fernando lazcano 1249', '951858542');

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
(1, '22206401-5', 'Matias', 'Flores', 'admin', '$2b$12$3V11whxZprgMPTCX/8jJLOgCAs3tANamVu.8AgtlyZOnpOeYMWTbW'),
(2, '22153790-4', 'Vicente', 'Ponce', 'Admin', '$2a$12$iIp8C6YYdDZqgHmzgxKzweBGd5BmjwtXNBVKO7Dqi6IpP6PbcGSiG');

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
  `disponible` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `vehiculos`
--

INSERT INTO `vehiculos` (`patente`, `marca`, `modelo`, `anio`, `precio`, `disponible`) VALUES
('ABCD-23', 'Toyota', 'Corolla', 2022, 35000, 1),
('BBCC-77', 'Mazda', 'CX-5', 2023, 50000, 1),
('CCDD-65', 'Ford', 'Focus', 2020, 32000, 1),
('EEFF-34', 'Peugeot', '208', 2021, 31000, 1),
('GGHH-98', 'Honda', 'Civic', 2023, 48000, 1),
('JKLP-45', 'Hyundai', 'Tucson', 2021, 42000, 1),
('MNOP-89', 'Kia', 'Rio', 2020, 30000, 1),
('QRST-56', 'Chevrolet', 'Tracker', 2023, 45000, 1),
('UVWX-12', 'Suzuki', 'Swift', 2019, 28000, 1),
('YZAA-90', 'Nissan', 'X-Trail', 2022, 47000, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `arriendos`
--
ALTER TABLE `arriendos`
  ADD PRIMARY KEY (`num_arriendo`),
  ADD KEY `fk_cliente` (`run_cliente`),
  ADD KEY `fk_empleado` (`codigo_empleado`),
  ADD KEY `fk_vehiculo` (`patente_vehiculo`);

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
  MODIFY `num_arriendo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `arriendos`
--
ALTER TABLE `arriendos`
  ADD CONSTRAINT `fk_cliente` FOREIGN KEY (`run_cliente`) REFERENCES `clientes` (`run`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_empleado` FOREIGN KEY (`codigo_empleado`) REFERENCES `empleados` (`codigo`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_vehiculo` FOREIGN KEY (`patente_vehiculo`) REFERENCES `vehiculos` (`patente`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
