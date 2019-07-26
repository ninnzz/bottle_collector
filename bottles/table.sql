CREATE TABLE `user`(
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `address` varchar(128) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `gender` varchar(4) DEFAULT NULL,
  -- `rfid` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `bottles` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(64) DEFAULT NULL,
  `type` INT DEFAULT NULL,
  `points` INT DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `transactions` (
  `id` INT(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_name` INT NOT NULL,
  `location_id` INT NOT NULL,
  `bottle_type` INT NOT NULL,
  `date` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `location` (
  `id` INT(11) unsigned NOT NULL AUTO_INCREMENT,
  `location_name` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;



