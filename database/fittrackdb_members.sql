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
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `members` (
  `member_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `birthdate` date DEFAULT NULL,
  `height` float DEFAULT NULL,
  `weight` float DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB AUTO_INCREMENT=346 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
INSERT INTO `members` VALUES (272,'hossam alaa','2009-12-12',188,77,'male','01098112345','m.hosam@gmail.com'),(277,'aly hossam','2001-05-12',169,78,'male','01026984456','m.jehad.kh@gmail.com'),(279,'sage healer','1989-12-12',167,66,'female','01029881125','sage@valo.com'),(280,'sky healer','1992-12-12',166,66,'female','01089226734','sky@valo.com'),(281,'brimstone smoker','1978-01-01',189,88,'male','01023448910','smoke.3@hotmail.com'),(283,'Chamber bob','1998-12-12',187,77,'male','01098223456','chamer.chambo@gmail.com'),(284,'Ziad Tarek','1978-06-18',189,70,'male','01090227384','ziad.tr@gmail.com'),(285,'Raed Mohamad','1978-09-29',180,66,'male','01189223452','R.mohamad@live.com'),(286,'Mohamad Jehad','2000-05-12',184,80,'male','01026984456','m.jehad.kh@gmail.com'),(287,'Mohamad ahmad','2002-12-14',178,21,'male','01029998834','ahmad@live.com'),(288,'Mohamad Aly','2001-07-07',178,80,'male','01029998834','m.cham@gmail.com'),(289,'Mohamad ahmad','2000-11-13',178,78,'male','01029998834','ahmad@live.com'),(290,'sky sage','1997-02-19',178,78,'female','0102229937','m.amr.kk@hotmail.com'),(340,'Abo Majed','1996-02-22',188,180,'male','91928998841','m.abo@gmail.com');
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-22  9:06:59
