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
  SELECT
    student_1.pet,
    student_1.song,
    student_1.color,
    student_2.color
  FROM
    students AS student_1,
    students AS student_2
  WHERE student_1.time < student_2.time
    AND student_1.pet = student_2.pet
    AND student_1.song = student_2.song;

CREATE TABLE smallest_int_having AS
  SELECT time, smallest
  FROM students
  GROUP BY smallest
  HAVING COUNT(*) = 1
  ORDER BY smallest;
