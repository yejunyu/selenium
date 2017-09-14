-- MySQL dump 10.13  Distrib 5.7.18, for Linux (x86_64)
--
-- Host: 114.215.103.154    Database: ad_click
-- ------------------------------------------------------
-- Server version	5.7.18-0ubuntu0.16.04.1-log

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
-- Table structure for table `browser_taskcount`
--

DROP TABLE IF EXISTS `browser_taskcount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `browser_taskcount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url_MD5` varchar(32) NOT NULL,
  `finish_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '任务完成数\n',
  `task_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '任务数\n',
  `task_status` smallint(5) unsigned NOT NULL,
  `create_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `bk1` varchar(255) DEFAULT NULL,
  `task_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url_MD5` (`url_MD5`),
  KEY `browser_taskcount_task_id_id_7f532ee9_fk_browser_clicktask_id` (`task_id_id`),
  CONSTRAINT `browser_taskcount_task_id_id_7f532ee9_fk_browser_clicktask_id` FOREIGN KEY (`task_id_id`) REFERENCES `browser_clicktask` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `browser_taskcount`
--

LOCK TABLES `browser_taskcount` WRITE;
/*!40000 ALTER TABLE `browser_taskcount` DISABLE KEYS */;
/*!40000 ALTER TABLE `browser_taskcount` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-07-24 14:54:57
