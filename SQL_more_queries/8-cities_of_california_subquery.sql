-- commment
SELECT id, name
FROM ciites
WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;