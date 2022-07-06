-- sql
SELECT
  id, name
FROM
  cities
WHERE
  state_id IN (SELECT id
    FROM
      cities
    WHERE
      name = 'California' ORDER BY id);
