
CREATE TABLE `routine` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(100) NOT NULL COMMENT 'name of routine',
	`description` VARCHAR(255) COMMENT 'description of routine',
	`create_datetime` DATETIME NOT NULL,
	`modify_datetime` DATETIME,
	PRIMARY KEY (`id`)
);

CREATE TABLE `exercises` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(100) NOT NULL,
	`is_unilateral` BOOLEAN NOT NULL DEFAULT false,
	`is_bodyweight` BOOLEAN NOT NULL DEFAULT false,
	`details` JSON,
	PRIMARY KEY (`id`)
);

CREATE TABLE `exercise_sets` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`exercise_id` INT NOT NULL,
	`routine_id` INT NOT NULL,
	`display_order` INT NOT NULL,
	`unit` ENUM('repetition', 'time') NOT NULL,
	`count` INT NOT NULL,
	`details` JSON COMMENT 'Contains the rpe, rest, pct1rm, cluster_set info and more',
	PRIMARY KEY (`id`),
	FOREIGN KEY (`exercise_id`) REFERENCES exercises(`id`),
	FOREIGN KEY (`routine_id`) REFERENCES routine(`id`)
);

CREATE TABLE `dashboard_users` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`username` VARCHAR(100) NOT NULL COMMENT 'username',
	`email` VARCHAR(255) NOT NULL COMMENT 'email',
	`password_hash` CHAR(60) NOT NULL COMMENT 'password',
	`create_datetime` DATETIME NOT NULL COMMENT 'date',
	`user_id` CHAR(30) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `routine_user_map` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`routine_id` INT NOT NULL,
	`user_id` INT NOT NULL,
	`config` JSON,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`routine_id`) REFERENCES routine(`id`),
	FOREIGN KEY (`user_id`) REFERENCES dashboard_users(`id`)
);

CREATE TABLE `set_history` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`set_id` INT NOT NULL,
	`unit` ENUM('repetition', 'time') NOT NULL,
	`count` INT NOT NULL COMMENT 'reps',
	`load` INT NOT NULL COMMENT 'lb/kg',
	`record_date` DATETIME NOT NULL,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`set_id`) REFERENCES exercise_sets(`id`)
);

CREATE TABLE `routine_edit_lock` (
	`routine_id` INT NOT NULL,
	`user_id` INT NOT NULL,
	`start_datetime` DATETIME NOT NULL,
	PRIMARY KEY (`routine_id`),
	FOREIGN KEY (`routine_id`) REFERENCES routine(`id`),
	FOREIGN KEY (`user_id`) REFERENCES dashboard_users(`id`)
);

CREATE TABLE `user_configuration` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`user_id` INT NOT NULL,
	`parameter_name` VARCHAR(255) NOT NULL,
	`parameter_value` VARCHAR(255) NOT NULL,
	`modify_datetime` DATETIME NOT NULL,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`user_id`) REFERENCES dashboard_users(`id`)
);
