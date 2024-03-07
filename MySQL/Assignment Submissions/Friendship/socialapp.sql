CREATE DATABASE  IF NOT EXISTS `socialapp` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `socialapp`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: socialapp
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
-- Table structure for table `friendships`
--

DROP TABLE IF EXISTS `friendships`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `friendships` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `friend_id` int NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_friendships_users_idx` (`user_id`),
  KEY `fk_friendships_users1_idx` (`friend_id`),
  CONSTRAINT `fk_friendships_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `fk_friendships_users1` FOREIGN KEY (`friend_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `friendships`
--

LOCK TABLES `friendships` WRITE;
/*!40000 ALTER TABLE `friendships` DISABLE KEYS */;
INSERT INTO `friendships` VALUES (1,1,4,'2022-06-06 00:00:00','2022-06-06 00:00:00'),(2,1,3,'2022-06-06 00:00:00','2022-06-06 00:00:00'),(3,1,2,'2022-06-06 00:00:00','2022-06-06 00:00:00'),(4,2,1,'2022-06-06 00:00:00','2022-06-06 00:00:00'),(5,3,1,'2022-06-06 00:00:00','2022-06-06 00:00:00'),(6,4,1,'2022-06-06 00:00:00','2022-06-06 00:00:00'),(7,1,2,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(8,2,3,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(9,3,4,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(10,1,2,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(11,2,3,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(12,3,4,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(13,4,5,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(14,5,6,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(15,6,7,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(16,7,8,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(17,8,9,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(18,9,10,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(19,10,11,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(20,11,12,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(21,12,13,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(22,13,14,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(23,14,15,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(24,15,16,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(25,16,17,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(26,17,18,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(27,18,19,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(28,19,20,'2024-02-25 00:00:00','2024-02-25 00:00:00'),(29,20,1,'2024-02-25 00:00:00','2024-02-25 00:00:00');
/*!40000 ALTER TABLE `friendships` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `create_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Chris','Baker','2019-01-20 00:00:00','2019-01-20 00:00:00'),(2,'Diana','Smith','2019-01-20 00:00:00','2019-01-20 00:00:00'),(3,'James','Johnson','2020-04-04 00:00:00','2020-04-04 00:00:00'),(4,'Jessica','Davidson','2022-06-06 00:00:00','2022-06-06 00:00:00'),(5,'Emma','Wilson','2023-01-15 00:00:00','2023-01-15 00:00:00'),(6,'Michael','Brown','2023-02-20 00:00:00','2023-02-20 00:00:00'),(7,'Sophia','Martinez','2023-03-25 00:00:00','2023-03-25 00:00:00'),(8,'Matthew','Jones','2023-04-30 00:00:00','2023-04-30 00:00:00'),(9,'Emma','Wilson','2023-01-15 00:00:00','2023-01-15 00:00:00'),(10,'Michael','Brown','2023-02-20 00:00:00','2023-02-20 00:00:00'),(11,'Sophia','Martinez','2023-03-25 00:00:00','2023-03-25 00:00:00'),(12,'Matthew','Jones','2023-04-30 00:00:00','2023-04-30 00:00:00'),(13,'Olivia','Davis','2023-05-10 00:00:00','2023-05-10 00:00:00'),(14,'Daniel','Garcia','2023-06-15 00:00:00','2023-06-15 00:00:00'),(15,'Isabella','Rodriguez','2023-07-20 00:00:00','2023-07-20 00:00:00'),(16,'Alexander','Miller','2023-08-25 00:00:00','2023-08-25 00:00:00'),(17,'Amelia','Wilson','2023-09-30 00:00:00','2023-09-30 00:00:00'),(18,'William','Taylor','2023-10-05 00:00:00','2023-10-05 00:00:00'),(19,'Mia','Anderson','2023-11-15 00:00:00','2023-11-15 00:00:00'),(20,'Ethan','Thomas','2023-12-20 00:00:00','2023-12-20 00:00:00'),(21,'Charlotte','Jackson','2024-01-25 00:00:00','2024-01-25 00:00:00'),(22,'James','White','2024-02-28 00:00:00','2024-02-28 00:00:00'),(23,'Ava','Harris','2024-03-05 00:00:00','2024-03-05 00:00:00'),(24,'Benjamin','Martin','2024-04-10 00:00:00','2024-04-10 00:00:00'),(25,'Lucas','Thompson','2024-05-15 00:00:00','2024-05-15 00:00:00'),(26,'Harper','Gonzalez','2024-06-20 00:00:00','2024-06-20 00:00:00'),(27,'Evelyn','Lewis','2024-07-25 00:00:00','2024-07-25 00:00:00'),(28,'Jack','Lee','2024-08-30 00:00:00','2024-08-30 00:00:00');
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

-- Dump completed on 2024-02-25  0:29:09
