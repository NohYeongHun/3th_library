CREATE TABLE `rent` (
  `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `book_id` int NOT NULL,
  `book_info_id` int NOT NULL,
  `user_id` varchar(20) NOT NULL,
  `rent_date` date  NOT NULL DEFAULT(CURRENT_DATE),
  `due_date` date NOT NULL DEFAULT(CURRENT_DATE+7),
  `return_date` datetime,
  `book_return` boolean NOT NULL DEFAULT FALSE
);

ALTER TABLE `rent` ADD FOREIGN KEY (`book_id`) REFERENCES `inventory` (`id`);
ALTER TABLE `rent` ADD FOREIGN KEY (`book_info_id`) REFERENCES `book` (`id`);

ALTER TABLE `rent` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

