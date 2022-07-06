-- sql
SELECT
  cities
FROM
  hbtn_0d_usa.states
WHERE
  name IN (SELECT name
    FROM
      cities
    WHERE
      name = 'California');
