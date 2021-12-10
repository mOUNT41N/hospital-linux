-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: hospital
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `chapter1`
--

DROP TABLE IF EXISTS `chapter1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chapter1` (
  `id` int unsigned NOT NULL,
  `xinxichenshuzhe` varchar(100) DEFAULT NULL,
  `yuhuanzheguanxi` varchar(100) DEFAULT NULL,
  `xinxikekaochengdu` varchar(100) DEFAULT NULL,
  `xingming` varchar(100) DEFAULT NULL,
  `xingbie` int DEFAULT NULL,
  `chushengriqi` date DEFAULT NULL,
  `nianling` varchar(100) DEFAULT NULL,
  `minzu` int DEFAULT NULL,
  `shenfenzhenghao` varchar(100) DEFAULT NULL,
  `xuexing` int DEFAULT NULL,
  `jiatingzhuzhi` varchar(100) DEFAULT NULL,
  `gudingdianhua` varchar(100) DEFAULT NULL,
  `shouji1` varchar(100) DEFAULT NULL,
  `shouji2` varchar(100) DEFAULT NULL,
  `zhiye` int DEFAULT NULL,
  `jiaoyuchengdu` int DEFAULT NULL,
  `feiyongleibie` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-28 12:43:12
