-- commment
SELECT id, name
FROM cites
WHERE state_id IN (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;