CREATE TABLE `inventory` (
  `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `book_id` int NOT NULL ,
  `exist_check` boolean NOT NULL DEFAULT 1
);

ALTER TABLE `inventory` ADD FOREIGN KEY (`book_id`) REFERENCES `book` (`id`);