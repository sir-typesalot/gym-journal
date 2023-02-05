
CREATE TABLE `routine` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(100) NOT NULL COMMENT 'name of routine',
	`description` VARCHAR(255) DEFAULT '' COMMENT 'description of routine',
	`create_datetime` DATETIME(20) NOT NULL,
	`modify_datetime` DATETIME(20),
	PRIMARY KEY (`id`)
);

CREATE TABLE `exercise_sets` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`exercise_id` INT NOT NULL,
	`routine_id` INT NOT NULL,
	`display_order` INT NOT NULL,
	`unit` ENUM('repetition', 'time') NOT NULL,
	`count` INT NOT NULL,
	`rest` INT,
	`rpe` INT,
	`pct_1rm` INT,
	PRIMARY KEY (`id`)
);

CREATE TABLE `exercises` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(100) NOT NULL,
	`is_unilateral` BOOLEAN NOT NULL DEFAULT 'false',
	`is_bodyweight` BOOLEAN NOT NULL DEFAULT 'false',
	`details` JSON,
	PRIMARY KEY (`id`)
);




