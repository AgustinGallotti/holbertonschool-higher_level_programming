-- sql
SELECT
  id, name
FROM
  cities
WHERE
  state_id IN(SELECT id
    FROM
      state.cities
    WHERE
      name = 'California' ORDER BY cities.id);
