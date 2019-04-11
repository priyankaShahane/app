-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: inventory_management
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `location_table`
--

DROP TABLE IF EXISTS `location_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `location_table` (
  `locationID` int(11) NOT NULL,
  `locationName` varchar(50) DEFAULT NULL,
  `store` varchar(50) DEFAULT NULL,
  `productID` int(11) DEFAULT NULL,
  PRIMARY KEY (`locationID`),
  KEY `productID` (`productID`),
  CONSTRAINT `location_table_ibfk_1` FOREIGN KEY (`productID`) REFERENCES `product_table` (`productID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location_table`
--

LOCK TABLES `location_table` WRITE;
/*!40000 ALTER TABLE `location_table` DISABLE KEYS */;
INSERT INTO `location_table` VALUES (101,'Aurangabad','shop',1),(102,'Hydrabad','store',2),(103,'Pune','shop',3),(104,'Nanded','store1',4),(105,'Hydrabad',' ',1),(106,'Nanded',' ',3),(107,'Hydrabad',' ',1),(108,'Pune',' ',2),(109,'Pune',' ',2),(110,'Nanded',' ',3),(111,'Pune',' ',4),(112,'Pune',' ',1),(113,'Pune',' ',1),(114,'Nanded',' ',2),(115,'Hydrabad',' ',3),(116,'Hydrabad',' ',1);
/*!40000 ALTER TABLE `location_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_balance`
--

DROP TABLE IF EXISTS `product_balance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `product_balance` (
  `pbID` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(50) DEFAULT NULL,
  `location_name` varchar(50) DEFAULT NULL,
  `Quantity` int(11) DEFAULT NULL,
  `productID` int(11) DEFAULT NULL,
  PRIMARY KEY (`pbID`),
  KEY `productID` (`productID`),
  CONSTRAINT `product_balance_ibfk_1` FOREIGN KEY (`productID`) REFERENCES `product_table` (`productID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_balance`
--

LOCK TABLES `product_balance` WRITE;
/*!40000 ALTER TABLE `product_balance` DISABLE KEYS */;
INSERT INTO `product_balance` VALUES (1,'Laptop','Aurangabad',1,1),(2,'Laptop','Hydrabad',3,1),(3,'Computer','Hydrabad',1,2),(4,'Computer','Pune',2,2),(5,'Fridge','Pune',0,3),(6,'Fridge','Nanded',3,3),(7,'AC','Nanded',4,4),(8,'AC','Pune',4,4),(9,'Laptop','Pune',1,1),(10,'Computer','Nanded',1,2),(11,'Fridge','Hydrabad',3,3);
/*!40000 ALTER TABLE `product_balance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_movement`
--

DROP TABLE IF EXISTS `product_movement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `product_movement` (
  `movementID` int(11) NOT NULL,
  `fromLocation` varchar(50) DEFAULT NULL,
  `toLocation` varchar(50) DEFAULT NULL,
  `productID` int(11) DEFAULT NULL,
  `Quantity` int(11) DEFAULT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`movementID`),
  KEY `productID` (`productID`),
  CONSTRAINT `product_movement_ibfk_1` FOREIGN KEY (`productID`) REFERENCES `product_table` (`productID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_movement`
--

LOCK TABLES `product_movement` WRITE;
/*!40000 ALTER TABLE `product_movement` DISABLE KEYS */;
INSERT INTO `product_movement` VALUES (1001,'Aurangabad',NULL,1,2,'2019-04-09 19:58:29'),(1002,NULL,'Hydrabad',1,3,'2019-04-09 19:58:29'),(1003,'Hydrabad',NULL,2,2,'2019-04-09 20:09:57'),(1004,NULL,'Pune',2,2,'2019-04-09 20:09:57'),(1005,'Pune',NULL,3,3,'2019-04-09 20:10:48'),(1006,NULL,'Nanded',3,3,'2019-04-09 20:10:48'),(1007,'Nanded',NULL,4,4,'2019-04-09 20:11:53'),(1008,NULL,'Pune',4,4,'2019-04-09 20:11:53'),(1009,'Aurangabad',NULL,1,1,'2019-04-09 20:37:35'),(1010,NULL,'Pune',1,1,'2019-04-09 20:37:35'),(1011,'Hydrabad',NULL,2,1,'2019-04-09 20:38:46'),(1012,NULL,'Nanded',2,1,'2019-04-09 20:38:46'),(1013,'Pune',NULL,3,0,'2019-04-09 20:41:16'),(1014,NULL,'Hydrabad',3,3,'2019-04-09 20:41:16');
/*!40000 ALTER TABLE `product_movement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_table`
--

DROP TABLE IF EXISTS `product_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `product_table` (
  `productID` int(11) NOT NULL,
  `productName` varchar(50) DEFAULT NULL,
  `Quantity` int(11) DEFAULT NULL,
  `cost` float DEFAULT NULL,
  PRIMARY KEY (`productID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_table`
--

LOCK TABLES `product_table` WRITE;
/*!40000 ALTER TABLE `product_table` DISABLE KEYS */;
INSERT INTO `product_table` VALUES (1,'Laptop',5,3000000),(2,'Computer',4,2000000),(3,'Fridge',6,4000000),(4,'AC',8,90000000),(5,'Music Player',9,50000);
/*!40000 ALTER TABLE `product_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `users` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'nil','nil','$5$rounds=535000$P8IKyzS3fOdNMbFb$G5QWy8Dwp4D.wu8Cf/eyK8.aYdVdk31VilIflw3dj1D'),(2,'nil','nil','$5$rounds=535000$24g5a86elqcT8kfw$fCq8FW2rx/uhoNGhZp0AgwG95P7ghprYu8xJFctlds6'),(3,'nil','nil','$5$rounds=535000$Y2NW9KRvA2dD0Oss$FysaB7KeROrE9dO2hBdp4ALLwvaGYTdcEe2fCifc1MD'),(4,'admin','admin','$5$rounds=535000$BdWDyXwBGk9eqEgc$LbpIex.C8CIPKaJ6hqqbvgxvpgIElhmvP6Bu/./e6K5'),(5,'vijaya shahane','vijaya','$5$rounds=535000$FwWEVZjJZoks1IsH$3hk4bbdXiP70E3iTw4Rm45deUdpQcIb48YMXHDCoikA');
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

-- Dump completed on 2019-04-11 11:57:04
