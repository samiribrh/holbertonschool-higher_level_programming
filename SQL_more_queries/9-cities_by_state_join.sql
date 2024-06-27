-- A script that lists all cities contained in the database hbtn_0d_usa.
SELECT
    cities.id,
    cities.name,
    states.name
FROM
    cities c
INNER JOIN
    states s
ON
    s.id = c.state_id
ORDER BY
    cities.id ASC;
