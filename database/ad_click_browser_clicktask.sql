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
-- Table structure for table `browser_clicktask`
--

DROP TABLE IF EXISTS `browser_clicktask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `browser_clicktask` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(500) NOT NULL,
  `url_MD5` varchar(32) NOT NULL COMMENT 'url加上任务发布的时间戳经过md5转换\npython中是haslib库',
  `task_type` smallint(5) unsigned DEFAULT '0' COMMENT '0:CPM\n1:CPC',
  `task_detail` smallint(5) unsigned DEFAULT '0' COMMENT '0:pc\n1:手机\n2:ios\n3:安卓',
  `task_status` smallint(5) unsigned DEFAULT '0' COMMENT '0:未完成\n1:执行中\n2:完成',
  `task_bili` smallint(5) unsigned DEFAULT '0' COMMENT '跳转比例',
  `task_time` date NOT NULL COMMENT '任务执行时间\n',
  `task_area` varchar(255) NOT NULL DEFAULT '0' COMMENT '0:全国\n1:广州',
  `request` smallint(5) unsigned NOT NULL DEFAULT '0' COMMENT '0:requests\n1:browser\n',
  `referer` varchar(500) NOT NULL COMMENT '来源,以逗号分隔\n',
  `create_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `remark` longtext COMMENT '备注\n',
  `bk1` varchar(255) DEFAULT NULL COMMENT '保留字段\n',
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url_MD5` (`url_MD5`),
  KEY `browser_clicktask_user_id_fc2c8473_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `browser_clicktask_user_id_fc2c8473_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `browser_clicktask`
--

LOCK TABLES `browser_clicktask` WRITE;
/*!40000 ALTER TABLE `browser_clicktask` DISABLE KEYS */;
/*!40000 ALTER TABLE `browser_clicktask` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-07-24 14:54:58
