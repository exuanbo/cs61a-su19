CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size
  FROM dogs, sizes
  WHERE min < height AND height <= max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT dog_child.name
  FROM
    dogs AS dog_child,
    parents,
    dogs AS dog_parent
  WHERE dog_child.name = child
    AND dog_parent.name = parent
  ORDER BY dog_parent.height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT
    dog_child_1.name as dog_1_name,
    dog_child_2.name as dog_2_name
  FROM
    dogs as dog_child_1,
    dogs AS dog_child_2,
    parents AS dog_parents_1,
    parents AS dog_parents_2
  WHERE dog_1_name < dog_2_name
    AND dog_1_name = dog_parents_1.child
    AND dog_2_name = dog_parents_2.child
    AND dog_parents_1.parent = dog_parents_2.parent;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT PRINTF("%s and %s are %s siblings", dog_1_name, dog_2_name, dog_sizes_1.size)
  FROM
    siblings,
    dogs AS dogs_1,
    dogs AS dogs_2,
    sizes AS dog_sizes_1,
    sizes AS dog_sizes_2
  WHERE dogs_1.name = dog_1_name
    AND dogs_2.name = dog_2_name
    AND dog_sizes_1.min < dogs_1.height
    AND dogs_1.height <= dog_sizes_1.max
    AND dog_sizes_2.min < dogs_2.height
    AND dogs_2.height <= dog_sizes_2.max
    AND dog_sizes_1.size = dog_sizes_2.size;

-- Total size for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT fur, SUM(height)
  FROM dogs
  GROUP BY fur
  HAVING 0.7 * AVG(height) <= height AND height <= 1.3 * AVG(height);
