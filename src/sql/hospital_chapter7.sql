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
-- Table structure for table `chapter7`
--

DROP TABLE IF EXISTS `chapter7`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chapter7` (
  `id` int unsigned NOT NULL,
  `xiehongdanbai` varchar(100) DEFAULT NULL,
  `hongxibaoxue` varchar(100) DEFAULT NULL,
  `hongxibaoyaji` varchar(100) DEFAULT NULL,
  `baixibaoxue` varchar(100) DEFAULT NULL,
  `xiexiaoban` varchar(100) DEFAULT NULL,
  `zhongxinglixibao` varchar(100) DEFAULT NULL,
  `niaodanbai` varchar(100) DEFAULT NULL,
  `guanxing` varchar(100) DEFAULT NULL,
  `hongxibaoniao` varchar(100) DEFAULT NULL,
  `baixibaoniao` varchar(100) DEFAULT NULL,
  `K` varchar(100) DEFAULT NULL,
  `Ca2` varchar(100) DEFAULT NULL,
  `P3` varchar(100) DEFAULT NULL,
  `CO2CP` varchar(100) DEFAULT NULL,
  `GLU` varchar(100) DEFAULT NULL,
  `BUN` varchar(100) DEFAULT NULL,
  `Scr` varchar(100) DEFAULT NULL,
  `UA` varchar(100) DEFAULT NULL,
  `TP` varchar(100) DEFAULT NULL,
  `Alb` varchar(100) DEFAULT NULL,
  `ALT` varchar(100) DEFAULT NULL,
  `AST` varchar(100) DEFAULT NULL,
  `GammaGT` varchar(100) DEFAULT NULL,
  `ALP` varchar(100) DEFAULT NULL,
  `TBIL` varchar(100) DEFAULT NULL,
  `CHO` varchar(100) DEFAULT NULL,
  `TG` varchar(100) DEFAULT NULL,
  `LDL` varchar(100) DEFAULT NULL,
  `INS` varchar(100) DEFAULT NULL,
  `Ctai` varchar(100) DEFAULT NULL,
  `eGFR` varchar(100) DEFAULT NULL,
  `niaobaidanbaijihang` varchar(100) DEFAULT NULL,
  `xiaoshiniaoweiliangbaidanbaipaixielv` varchar(100) DEFAULT NULL,
  `xiaoshiniaodanbaidingliang` varchar(100) DEFAULT NULL,
  `niaoliang` varchar(100) DEFAULT NULL,
  `yaowei` varchar(100) DEFAULT NULL,
  `tanghuaxuehongdanbai` varchar(100) DEFAULT NULL,
  `xindiantu` varchar(100) DEFAULT NULL,
  `chaoshengxindong` varchar(100) DEFAULT NULL,
  `zuoxinshishexuefenshu` varchar(100) DEFAULT NULL,
  `jingdongmaiBchao` varchar(100) DEFAULT NULL,
  `jingneizhongmohouduzuo` varchar(100) DEFAULT NULL,
  `jingneizhongmohouduyou` varchar(100) DEFAULT NULL,
  `yandijiancha` varchar(100) DEFAULT NULL,
  `ectjiancha` varchar(100) DEFAULT NULL,
  `zhaopianlujing` varchar(512) DEFAULT NULL,
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
