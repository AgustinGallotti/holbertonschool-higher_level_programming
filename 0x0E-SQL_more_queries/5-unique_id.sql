-- sql
CREATE TABLE IF NOT EXISTS unique_id (
  id INT,
  name VARCHAR(256),
  UNIQUE(id)
);
ALTER TABLE unique_id ALTER id SET DEFAULT 1;
