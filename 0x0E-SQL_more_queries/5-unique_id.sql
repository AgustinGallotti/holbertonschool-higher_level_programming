-- sql
CREATE TABLE IF NOT EXISTS unique_id (
  id INT,
  name VARCHAR(256)
);
ALTER TABLE unique_id ALTER id SET DEFAULT 1;
SELECT UUID(id) id FROM unique_id;
