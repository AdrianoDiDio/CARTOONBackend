CREATE TABLE `Camera` (
  `ID` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `Name` VARCHAR(255) DEFAULT NULL,
  `Position` POINT NOT NULL SRID 4326,
  `IPv4` VARCHAR(16) NOT NULL,
  `Port` SMALLINT NOT NULL,
  `StreamName` VARCHAR(512) NOT NULL
) DEFAULT CHARSET=latin1;

#ON ROUTE
INSERT INTO Camera (Name,Position,ipv4,port,StreamName)
	VALUES( "Camera1",ST_SRID(POINT(37.080530,14.224689),4326),'192.168.1.137',8554,"stream.m3u8");
INSERT INTO Camera (Name,Position,ipv4,port,StreamName)
	VALUES( "Camera2",ST_SRID(POINT(37.080245,14.217671),4326),'192.168.1.137',8554,"stream.m3u8");
#OK
INSERT INTO Camera (Name,Position,ipv4,port,StreamName)
	VALUES( "Camera3",ST_SRID(POINT(37.080094,14.217654),4326),'192.168.1.137',8554,"stream.m3u8");
INSERT INTO Camera (Name,Position,ipv4,port,StreamName)
	VALUES( "Camera4",ST_SRID(POINT(37.080815,14.230226),4326),'192.168.1.137',8554,"stream.m3u8");
#OUT ROUTE
INSERT INTO Camera (Name,Position,ipv4,port,StreamName)
	VALUES( "Camera5",ST_SRID(POINT(37.077944,14.232319),4326),'192.168.1.137',8554,"stream.m3u8");
INSERT INTO Camera (Name,Position,ipv4,port,StreamName)
	VALUES( "Camera6",ST_SRID(POINT(37.077578,14.221423),4326),'192.168.1.137',8554,"stream.m3u8");
INSERT INTO Camera (Name,Position,ipv4,port,StreamName)
	VALUES( "Camera7",ST_SRID(POINT(37.075705,14.231834),4326),'192.168.1.137',8554,"stream.m3u8");
#TOLERANCE TEST
INSERT INTO Camera (Name,Position,ipv4,port,StreamName)
	VALUES( "Camera8",ST_SRID(POINT(37.080075,14.217571),4326),'192.168.1.137',8554,"stream.m3u8");
