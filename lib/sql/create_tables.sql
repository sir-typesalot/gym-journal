
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

CREATE TABLE `routine_user_map` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`routine_id` INT NOT NULL DEFAULT '',
	`user_id` INT NOT NULL DEFAULT '',
	`config` JSON,
	PRIMARY KEY (`id`)
);

CREATE TABLE `dashboard_users` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`username` VARCHAR(100) NOT NULL DEFAULT '' COMMENT 'username',
	`email` VARCHAR(255) NOT NULL DEFAULT '' COMMENT 'email',
	`password_hash` CHAR NOT NULL COMMENT 'password',
	`create_datetime` DATETIME NOT NULL COMMENT 'date',
	PRIMARY KEY (`id`)
);

CREATE TABLE `set_history` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`set_id` INT NOT NULL DEFAULT '',
	`unit` ENUM NOT NULL,
	`count` INT NOT NULL COMMENT 'reps',
	`load` INT NOT NULL COMMENT 'lb/kg',
	`record_date` DATETIME NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `routine_edit_lock` (
	`routine_id` INT NOT NULL DEFAULT '',
	`user_id` INT NOT NULL DEFAULT '',
	`start_datetime` DATETIME NOT NULL,
	PRIMARY KEY (`routine_id`)
);

CREATE TABLE `user_configuration` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`user_id` INT NOT NULL DEFAULT '',
	`parameter_name` VARCHAR(255) NOT NULL,
	`parameter_value` VARCHAR(255) NOT NULL,
	`modify_datetime` DATETIME NOT NULL,
	PRIMARY KEY (`id`)
);
