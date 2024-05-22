-- lists states in california
-- SELECT id, name FROM cities
-- WHERE states.id IN (SELECT id FROM states WHERE name = 'California')
-- ORDER BY id;
SELECT id, name FROM cities WHERE state_id IN (SELECT id FROM states WHERE name = "California") ORDER BY id;
