-- 8-index_my_names.sql
-- Create an index on the name column of the my_names table.
CREATE INDEX idx_name_first
ON names (name(1));
