
CREATE TABLE IF NOT EXISTS penguins (

    id SERIAL PRIMARY KEY,
    species VARCHAR(12),
    bill_length_mm NUMERIC,
    bill_depth_mm NUMERIC,
    flipper_length_mm NUMERIC,
    body_mass_g NUMERIC,
    sex VARCHAR(10)

);

COPY penguins (species, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex) 
  FROM '/docker-entrypoint-initdb.d/penguins_simple.csv' CSV HEADER DELIMITER ';';