-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: carrental
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `car`
--

DROP TABLE IF EXISTS `car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car` (
  `idC` int NOT NULL AUTO_INCREMENT,
  `marque` varchar(45) NOT NULL,
  `modele` varchar(45) NOT NULL,
  `image` blob,
  `categorie` varchar(45) DEFAULT NULL,
  `typeCarburant` varchar(45) DEFAULT NULL,
  `nombrePlace` int NOT NULL,
  `transmition` varchar(45) DEFAULT NULL,
  `prixJour` float NOT NULL,
  `Disponibilite` varchar(45) NOT NULL,
  `dateReserv` date DEFAULT NULL,
  `dateRetrieve` date DEFAULT NULL,
  `client` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idC`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES (3,'ferari','2011',_binary 'gh','vide','44',3,'for',789,'',NULL,NULL,NULL),(4,'ford','modele',_binary 'd.jpg','sports car','5 cylinders',4,'Manuele',500,'Non Disponible','2023-05-04','2023-05-11',NULL),(5,'DACIA','2013',_binary 'JHNK','HatchBack','5 cylinders',4,'Manuele',200,'Non disponible','2023-05-05','2023-05-12',NULL),(6,'tug','456',_binary 'd.jpg','sports car','5 cylinders',3,'Manuele',56,'Non Disponible','2023-05-04','2023-05-11',NULL);
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carburant`
--

DROP TABLE IF EXISTS `carburant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carburant` (
  `idC` int NOT NULL AUTO_INCREMENT,
  `carburant` varchar(45) NOT NULL,
  PRIMARY KEY (`idC`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carburant`
--

LOCK TABLES `carburant` WRITE;
/*!40000 ALTER TABLE `carburant` DISABLE KEYS */;
INSERT INTO `carburant` VALUES (1,'5 cylinders'),(2,'4cc'),(3,'sport'),(6,'4cylinders'),(7,'4 cylinders');
/*!40000 ALTER TABLE `carburant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categorie`
--

DROP TABLE IF EXISTS `categorie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorie` (
  `idCategorie` int NOT NULL AUTO_INCREMENT,
  `Cname` varchar(40) NOT NULL,
  PRIMARY KEY (`idCategorie`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorie`
--

LOCK TABLES `categorie` WRITE;
/*!40000 ALTER TABLE `categorie` DISABLE KEYS */;
INSERT INTO `categorie` VALUES (1,'sports car'),(7,'4*4'),(8,'SUV'),(9,'Minivan'),(13,'HatchBack'),(14,'Sedan');
/*!40000 ALTER TABLE `categorie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `disponibilite`
--

DROP TABLE IF EXISTS `disponibilite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disponibilite` (
  `id` int NOT NULL AUTO_INCREMENT,
  `disponibilite` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disponibilite`
--

LOCK TABLES `disponibilite` WRITE;
/*!40000 ALTER TABLE `disponibilite` DISABLE KEYS */;
INSERT INTO `disponibilite` VALUES (1,'Non Disponible'),(2,'Disponible');
/*!40000 ALTER TABLE `disponibilite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transmition`
--

DROP TABLE IF EXISTS `transmition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transmition` (
  `idT` int NOT NULL AUTO_INCREMENT,
  `typeTransmition` varchar(45) NOT NULL,
  PRIMARY KEY (`idT`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transmition`
--

LOCK TABLES `transmition` WRITE;
/*!40000 ALTER TABLE `transmition` DISABLE KEYS */;
INSERT INTO `transmition` VALUES (1,'Manuele'),(2,'Automatic');
/*!40000 ALTER TABLE `transmition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nomP` varchar(40) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nomP_UNIQUE` (`nomP`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'admin','housamrazine@gmail.com','admin','admin'),(4,'yahia','yahia@gmail.com','123',NULL),(5,'Ahmad','ahmad@gmail.com','999',NULL),(6,'hawerd','hawerd@gmail.com','12',NULL),(7,'rana','eana@gmail.com','12',NULL),(8,'ranaa','rana@gmail.com','555',NULL),(9,'aymane','houssam@gmail.com','123',NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-05 23:43:41
