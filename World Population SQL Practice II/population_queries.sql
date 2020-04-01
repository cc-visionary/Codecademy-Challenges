-- How many entries in the database are from Africa?
SELECT continent, COUNT(*) AS 'entries' FROM countries
WHERE continent = 'Africa';

-- What was the total population of Oceania in 2005?
SELECT countries.continent, population_years.year, SUM(population_years.population) as 'total_population' 
FROM countries JOIN population_years 
  ON countries.id = population_years.country_id
WHERE countries.continent = 'Oceania' AND population_years.year = 2005;

-- -- What is the average population of countries in South America in 2003?
SELECT countries.continent, population_years.year, AVG(population_years.population) as 'average_population' 
FROM countries JOIN population_years 
  ON countries.id = population_years.country_id
WHERE countries.continent = 'South America' AND population_years.year = 2003;

-- What country had the smallest population in 2007?
SELECT countries.name, population_years.year, MIN(population_years.population) as 'average_population'
FROM countries JOIN population_years 
  ON countries.id = population_years.country_id
WHERE population_years.year = 2007;


-- What is the average population of Poland during the time period covered by this dataset?
SELECT countries.name, population_years.year, AVG(population_years.population) as 'average_population'
FROM countries JOIN population_years 
  ON countries.id = population_years.country_id
WHERE countries.name = 'Poland';

-- How many countries have the word "The" in their name? 4
SELECT COUNT(*) FROM countries
WHERE name LIKE '%The%';

-- What was the total population of each continent in 2010? 6842.96
SELECT population_years.year, SUM(population_years.population) as 'total_population'
FROM countries JOIN population_years 
  ON countries.id = population_years.country_id
WHERE population_years.year = 2010;
