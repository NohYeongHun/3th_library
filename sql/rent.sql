CREATE TABLE `rent` (
  `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `book_id` int NOT NULL,
  `user_id` varchar(20) NOT NULL,
  `rent_date` datetime NOT NULL ,
  `due_date` datetime NOT NULL ,
  `return_date` datetime NOT NULL ,
  `book_return` boolean NOT NULL 
);

ALTER TABLE `rent` ADD FOREIGN KEY (`book_id`) REFERENCES `book` (`id`);
ALTER TABLE `rent` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

