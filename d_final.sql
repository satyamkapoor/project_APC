-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: python_apc
-- ------------------------------------------------------
-- Server version	5.6.34-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `order_no` int(11) NOT NULL,
  `p_id` int(11) DEFAULT NULL,
  `p_quantity` int(11) DEFAULT NULL,
  `item_no` int(11) NOT NULL AUTO_INCREMENT,
  `price` int(11) DEFAULT '0',
  PRIMARY KEY (`item_no`),
  KEY `p_id_idx` (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=160 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (50432,3,4,158,16),(50432,1,2,159,4);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oreder_detail`
--

DROP TABLE IF EXISTS `oreder_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oreder_detail` (
  `order_no` int(11) NOT NULL AUTO_INCREMENT,
  `total` int(11) DEFAULT '0',
  `sucess` int(11) DEFAULT '0',
  `status` int(11) DEFAULT '0',
  PRIMARY KEY (`order_no`)
) ENGINE=InnoDB AUTO_INCREMENT=50433 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oreder_detail`
--

LOCK TABLES `oreder_detail` WRITE;
/*!40000 ALTER TABLE `oreder_detail` DISABLE KEYS */;
INSERT INTO `oreder_detail` VALUES (50432,20,1,1);
/*!40000 ALTER TABLE `oreder_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `p_id` int(11) NOT NULL,
  `p_name` varchar(50) DEFAULT NULL,
  `price_per_unit` int(11) DEFAULT '0',
  `availibility` varchar(45) DEFAULT '1',
  `type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Jupiler',2,'1','beer'),(2,'Leffe',3,'1','beer'),(3,'Chimay',4,'1','beer'),(4,'Orval',5,'1','beer'),(5,'La Chouffe',4,'1','beer'),(6,'Heineken',5,'1','beer'),(7,'Sex on the beach',5,'1','cocktail'),(8,'Cosmopolitan',4,'1','cocktail'),(9,'Mojito',4,'1','cocktail'),(10,'Caipirinha',5,'1','cocktail'),(11,'Cuba libre',5,'1','cocktail'),(12,'Pina colada',5,'1','cocktail'),(13,'One Monkey',4,'1',NULL),(14,'Nuts',1,'1','app'),(15,'Nachos',3,'1','app'),(16,'Pop corn',2,'0','app'),(17,'Hummus',3,'1','app'),(18,'The three monkeys',5,'1','app');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `table01`
--

DROP TABLE IF EXISTS `table01`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `table01` (
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table01`
--

LOCK TABLES `table01` WRITE;
/*!40000 ALTER TABLE `table01` DISABLE KEYS */;
INSERT INTO `table01` VALUES ('Satyam','me@satyamkapoor.com'),('Momin','momin@moni.com'),('Thomai','thomai@gmgmai.com');
/*!40000 ALTER TABLE `table01` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-01-15  4:26:22
