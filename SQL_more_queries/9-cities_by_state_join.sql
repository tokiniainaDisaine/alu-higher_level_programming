-- commment
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON states.id = cites.states_id
ORDER BY cities.id;