.read su19data.sql

CREATE TABLE obedience AS
  SELECT seven, instructor
  FROM students;

CREATE TABLE smallest_int AS
  SELECT time, smallest
  FROM students
  WHERE smallest > 2
  ORDER BY smallest
  LIMIT 20;

CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color
  FROM students AS a, students AS b
  WHERE
    a.time < b.time AND
    a.pet = b.pet AND
    a.song = b.song;

CREATE TABLE smallest_int_having AS
  SELECT time, smallest
  FROM students
  GROUP BY smallest
  HAVING COUNT(*) = 1
  ORDER BY smallest;
