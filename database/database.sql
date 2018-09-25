CREATE DATABASE `compose` /*!40100 DEFAULT CHARACTER SET latin1 */;

/* tbl_user  table */

CREATE TABLE `tbl_user` (
  `user_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_username` varchar(45) DEFAULT NULL,
  `user_password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=162 DEFAULT CHARSET=latin1;


/* tbl_user_data  table */

CREATE TABLE `tbl_user_data` (
  `user_username` varchar(45) NOT NULL,
  `address` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `postal_code` varchar(45) DEFAULT NULL,
  `ev_house_orientation` varchar(45) DEFAULT NULL,
  `ev_topografy` varchar(45) DEFAULT NULL,
  `ev_type_of_house` varchar(45) DEFAULT NULL,
  `ev_drought` varchar(45) DEFAULT NULL,
  `nh_access_way` varchar(45) DEFAULT NULL,
  `nh_next_the_house` varchar(45) DEFAULT NULL,
  `nh_water` varchar(45) DEFAULT NULL,
  `nh_high_tension_towers` varchar(45) DEFAULT NULL,
  `nh_fence` varchar(45) DEFAULT NULL,
  `yh_outer_walls` varchar(45) DEFAULT NULL,
  `yh_roof` varchar(45) DEFAULT NULL,
  `yh_waterproof` varchar(45) DEFAULT NULL,
  `yh_accumulation_of_leaves` varchar(45) DEFAULT NULL,
  `yh_barbeque` varchar(45) DEFAULT NULL,
  `yh_water_source` varchar(45) DEFAULT NULL,
  `risk` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`user_username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


/* tbl_user_fire_load  table */

CREATE TABLE `tbl_user_fire_load` (
  `user_username` varchar(45) NOT NULL,
  `area` varchar(45) NOT NULL,
  `activity` varchar(45) DEFAULT NULL,
  `wood` varchar(45) DEFAULT NULL,
  `paperboard` varchar(45) DEFAULT NULL,
  `cereals` varchar(45) DEFAULT NULL,
  `alcohol` varchar(45) DEFAULT NULL,
  `olive` varchar(45) DEFAULT NULL,
  `propane` varchar(45) DEFAULT NULL,
  `total_fire_load` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`user_username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


/* sp_createUser procedure */

DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `sp_createUser`(
    IN p_username VARCHAR(20),
    IN p_password VARCHAR(20)
)
BEGIN
    if ( select exists (select 1 from tbl_user where user_username = p_username) ) THEN
     
        select 'Username Exists !!';
     
    ELSE
     
        insert into tbl_user
        (
            user_username,
            user_password
        )
        values
        (
            p_username,
            p_password
        );
        
        select '';
     
    END IF;
END$$
DELIMITER ;



DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `sp_create_user_data`(
    IN p_username VARCHAR(20),
    IN p_address VARCHAR(45),
    IN p_city VARCHAR(45),
    IN p_postal_code VARCHAR(45),
    IN value1 VARCHAR(20),
    IN value2 VARCHAR(20),
    IN value3 VARCHAR(20),
    IN value4 VARCHAR(20),
    IN value5 VARCHAR(20),
    IN value6 VARCHAR(20),
    IN value7 VARCHAR(20),
    IN value8 VARCHAR(20),
    IN value9 VARCHAR(20),
    IN value10 VARCHAR(20),
    IN value11 VARCHAR(20),
    IN value12 VARCHAR(20),
    IN value13 VARCHAR(20),
    IN value14 VARCHAR(20),
    IN value15 VARCHAR(20),
   IN risk VARCHAR(20)    
)
BEGIN
    if ( select exists (select 1 from tbl_user_data where user_username = p_username) ) THEN
          select 'Already exists a register for this user !!';
 
     
    ELSE
      
       INSERT INTO `compose`.`tbl_user_data`
			(`user_username`,
			`address`,
			`city`,
            `postal_code`,
			`ev_house_orientation`,
			`ev_topografy`,
			`ev_type_of_house`,
			`ev_drought`,
			`nh_access_way`,
			`nh_next_the_house`,
			`nh_water`,
			`nh_high_tension_towers`,
			`nh_fence`,
			`yh_outer_walls`,
			`yh_roof`,
			`yh_waterproof`,
			`yh_accumulation_of_leaves`,
			`yh_barbeque`,
			`yh_water_source`,
            `risk`
            )
			VALUES
            (p_username, p_address, p_city, p_postal_code, value1, value2, value3, value4, value5,
            value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, risk);
        
        select '';
      
     
    END IF;
END$$
DELIMITER ;


DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `sp_create_user_fire_load`(
    IN p_username VARCHAR(20),
    IN area VARCHAR(45), 
    IN activity VARCHAR(45),
    IN wood VARCHAR(45),
    IN paperboard VARCHAR(45),
    IN cereals VARCHAR(20),
    IN alcohol VARCHAR(20),
    IN olive VARCHAR(20),
    IN propane VARCHAR(20),
    IN total_fire_load VARCHAR(20)
)
BEGIN
    if ( select exists (select 1 from tbl_user_fire_load where user_username = p_username) ) THEN
          select 'Already exists a register for this user !!';
 
     
    ELSE
      
   INSERT INTO `compose`.`tbl_user_fire_load`
(`user_username`,
`area`,
`activity`,
`wood`,
`paperboard`,
`cereals`,
`alcohol`,
`olive`,
`propane`,
`total_fire_load`)
VALUES
(
p_username,
area,
activity,
wood,
paperboard,
cereals,
alcohol,
olive,
propane,
total_fire_load);
        
        select '';
      
     
    END IF;
END$$
DELIMITER ;



DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `sp_select_all_user_data`()
BEGIN

    select * from tbl_user_data;      
     
END$$
DELIMITER ;



DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `sp_select__all_user_fire_load`()
BEGIN

SELECT
    *
FROM `compose`.`tbl_user_fire_load`;      
     
END$$
DELIMITER ;



DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `sp_select_user_data`(
    IN p_username VARCHAR(20)
    )
BEGIN

    select * from tbl_user_data where user_username = p_username;      
     
END$$
DELIMITER ;




DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `sp_select_user_fire_load`(
    IN p_username VARCHAR(20)
    )
BEGIN

SELECT
    `tbl_user_fire_load`.`area`,
    `tbl_user_fire_load`.`activity`,
    `tbl_user_fire_load`.`wood`,
    `tbl_user_fire_load`.`paperboard`,
    `tbl_user_fire_load`.`cereals`,
    `tbl_user_fire_load`.`alcohol`,
    `tbl_user_fire_load`.`olive`,
    `tbl_user_fire_load`.`propane`,
    `tbl_user_fire_load`.`total_fire_load`
FROM `compose`.`tbl_user_fire_load` where user_username = p_username;      
     
END$$
DELIMITER ;


DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `sp_update_user_data`(
    IN p_username VARCHAR(20),
    IN p_address VARCHAR(45),
    IN p_city VARCHAR(45),
    IN p_postal_code VARCHAR(45),
    IN value1 VARCHAR(20),
    IN value2 VARCHAR(20),
    IN value3 VARCHAR(20),
    IN value4 VARCHAR(20),
    IN value5 VARCHAR(20),
    IN value6 VARCHAR(20),
    IN value7 VARCHAR(20),
    IN value8 VARCHAR(20),
    IN value9 VARCHAR(20),
    IN value10 VARCHAR(20),
    IN value11 VARCHAR(20),
    IN value12 VARCHAR(20),
    IN value13 VARCHAR(20),
    IN value14 VARCHAR(20),
    IN value15 VARCHAR(20),
    IN risk VARCHAR(20) 
)
BEGIN
    if ( select exists (select 1 from tbl_user_data where user_username = p_username) ) THEN
       update `compose`.`tbl_user_data` set
			`address` = p_address,
			`city` = p_city,
            `postal_code` = p_postal_code, 
			`ev_house_orientation` = value1,
			`ev_topografy` = value2,
			`ev_type_of_house` = value3,
			`ev_drought` = value4,
			`nh_access_way` = value5,
			`nh_next_the_house` = value6,
			`nh_water` = value7,
			`nh_high_tension_towers` = value8,
			`nh_fence` = value9,
			`yh_outer_walls` = value10,
			`yh_roof` = value11,
			`yh_waterproof` = value12,
			`yh_accumulation_of_leaves` = value13,
			`yh_barbeque` = value14,
			`yh_water_source` = value15,
			`risk` = risk    
            where user_username = p_username;
	    
        select '';
 
     
    ELSE
          select 'Does not exist a register for the user !!';
      
      
     
    END IF;
END$$
DELIMITER ;


DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `sp_update_user_fire_load`(
     IN p_username VARCHAR(20),
    IN area VARCHAR(45),
    IN activity VARCHAR(45),
    IN wood VARCHAR(45),
    IN paperboard VARCHAR(45),
    IN cereals VARCHAR(20),
    IN alcohol VARCHAR(20),
    IN olive VARCHAR(20),
    IN propane VARCHAR(20),
    IN total_fire_load VARCHAR(20)
)
BEGIN
    if ( select exists (select 1 from tbl_user_fire_load where user_username = p_username) ) THEN
	   UPDATE `compose`.`tbl_user_fire_load`
			SET
			`area` = area,            
			`activity` = activity,
			`wood` = wood,
			`paperboard` = paperboard,
			`cereals` = cereals,
			`alcohol` = alcohol,
			`olive` = olive,
			`propane` = propane,
			`total_fire_load` = total_fire_load
			WHERE `user_username` = p_username;
	    
        select '';
 
     
    ELSE
          select 'Does not exist a register for the user !!';
      
      
     
    END IF;
END$$
DELIMITER ;


DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `sp_validateLogin`(
IN p_username VARCHAR(20)
)
BEGIN
    select * from tbl_user where user_username = p_username;
END$$
DELIMITER ;
