CREATE TRIGGER test_trigger BEFORE INSERT ON `rent` 
FOR EACH ROW SET
    NEW.rent_date = IFNULL(NEW.rent_date, NOW()),
    NEW.due_date = TIMESTAMPADD(DAY, 14, NEW.rent_date);