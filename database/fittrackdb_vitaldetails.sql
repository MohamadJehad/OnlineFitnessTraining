CREATE DATABASE  IF NOT EXISTS `fittrackdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `fittrackdb`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: fittrackdb
-- ------------------------------------------------------
-- Server version	8.2.0

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
-- Table structure for table `vitaldetails`
--

DROP TABLE IF EXISTS `vitaldetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vitaldetails` (
  `memberId` int DEFAULT NULL,
  `allergy` varchar(255) DEFAULT NULL,
  `disease` varchar(255) DEFAULT NULL,
  `bodyFatPercentage` decimal(5,2) DEFAULT NULL,
  `fitnessGoals` varchar(255) DEFAULT NULL,
  `medications` varchar(255) DEFAULT NULL,
  KEY `memberId` (`memberId`),
  CONSTRAINT `vitaldetails_ibfk_1` FOREIGN KEY (`memberId`) REFERENCES `members` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vitaldetails`
--

LOCK TABLES `vitaldetails` WRITE;
/*!40000 ALTER TABLE `vitaldetails` DISABLE KEYS */;
INSERT INTO `vitaldetails` VALUES (NULL,'no','no',12.00,'no','no'),(NULL,'no','no',12.00,'no','no'),(NULL,'no','no',18.00,'gain muscle','no'),(NULL,'no','no',18.00,'gain muscle','no'),(272,'no','no',17.00,'weight loss','no'),(277,'allergy','no diseas',18.00,'gain muscle','medication'),(279,'no allegy','no diseas',12.00,'weight loss','no medicaton'),(280,'allergy','no diseas',15.00,'weight loss','no medicaton'),(281,'no allegy','no diseas',30.00,'fat loss','no'),(283,'no allegy','no diseas',20.00,'gain muscle','no medicaton'),(284,'no allegy','no diseas',12.00,'gain muscle','no medicaton'),(285,'no allegy','no diseas',10.00,'fit goal','no medicaton'),(286,'no allegy','no diseas',18.00,'gain muscle','no medicaton'),(287,'no allegy','none',12.00,'weight loss','no medicaton'),(288,'no allegy','no diseas',18.00,'fit goal','no medicaton'),(289,'no allegy','no',10.00,'weight loss','no medicaton'),(290,'no allegy','no diseas',18.00,'weight loss','no medicaton'),(340,'no','no diseas',18.00,'weight loss','no medicaton');
/*!40000 ALTER TABLE `vitaldetails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-22  9:06:58
