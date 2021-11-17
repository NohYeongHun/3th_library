
CREATE TABLE `comment` (
  `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `user_id` varchar(20) NOT NULL,
  `book_id` int NOT NULL,
  `comment` varchar(255),
  `rating` int
);

ALTER TABLE `comment` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
ALTER TABLE `comment` ADD FOREIGN KEY (`book_id`) REFERENCES `book` (`id`);