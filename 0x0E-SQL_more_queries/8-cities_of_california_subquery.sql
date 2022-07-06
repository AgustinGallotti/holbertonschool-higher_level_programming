-- sql
SELECT
  id, name
FROM
  hbtn_0d_usa.states
WHERE
  name IN (SELECT id
    FROM
      cities
    WHERE
      name = 'California');
