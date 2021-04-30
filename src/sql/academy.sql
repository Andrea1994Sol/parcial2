-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         5.6.51-log - MySQL Community Server (GPL)
-- SO del servidor:              Win64
-- HeidiSQL Versión:             10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para academy
CREATE DATABASE IF NOT EXISTS `academy` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `academy`;

-- Volcando estructura para tabla academy.courses
CREATE TABLE IF NOT EXISTS `courses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `semester` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla academy.courses: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
REPLACE INTO `courses` (`id`, `name`, `semester`) VALUES
	(1, 'Base de datos II', '9'),
	(2, 'Redes I', '10'),
	(3, 'Electiva Profesiona I', '10'),
	(4, 'Calculo Diferencial', '8');
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;

-- Volcando estructura para tabla academy.course_student
CREATE TABLE IF NOT EXISTS `course_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_course` int(11) DEFAULT NULL,
  `id_student` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla academy.course_student: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `course_student` DISABLE KEYS */;
/*!40000 ALTER TABLE `course_student` ENABLE KEYS */;

-- Volcando estructura para tabla academy.session
CREATE TABLE IF NOT EXISTS `session` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `course` varchar(45) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `start_time` time DEFAULT NULL,
  `end_time` time DEFAULT NULL,
  `assistance` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla academy.session: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `session` DISABLE KEYS */;
REPLACE INTO `session` (`id`, `course`, `date`, `start_time`, `end_time`, `assistance`) VALUES
	(3, 'Base de datos II', '2021-04-30', '06:30:00', '07:30:00', NULL),
	(4, 'Redes I', '2021-04-28', '09:45:00', '10:45:00', NULL),
	(5, 'Base de datos II', '2021-04-29', '06:30:00', '08:45:00', NULL),
	(6, 'Electiva Profesiona I', '2021-05-01', '07:30:00', '09:45:00', NULL);
/*!40000 ALTER TABLE `session` ENABLE KEYS */;

-- Volcando estructura para tabla academy.students
CREATE TABLE IF NOT EXISTS `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(45) DEFAULT NULL,
  `names` varchar(45) DEFAULT NULL,
  `lastnames` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `semester` int(11) DEFAULT NULL,
  `course` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla academy.students: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
REPLACE INTO `students` (`id`, `uid`, `names`, `lastnames`, `phone`, `email`, `semester`, `course`) VALUES
	(38, NULL, 'Camila', 'Lozano', '3203876543', 'camila_lozano95@gmail.com', 10, '1'),
	(39, NULL, 'Mark', 'Baeza', '3224567895', 'markbaezae@gmail.com', 10, '2'),
	(40, NULL, 'Thiago', 'Gozzu', '3145678913', 'thiagobaezam@gmail.com', 9, '1');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
