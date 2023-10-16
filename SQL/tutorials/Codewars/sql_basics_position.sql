-- SQL Basics - Position (kyu 7)
-- ####################################################################################################
-- https://www.codewars.com/kata/59401e0e54a655a298000040
-- You have access to a table of monsters as follows:
-- monsters schema
-- id
-- name
-- legs
-- arms
-- characteristics
-- In each row, the characteristic column has a single comma. Your job is to find it using position(). You must return a table with the format as follows:
-- output schema
-- id
-- name
-- comma
-- The comma column will contain the position of the comma within the characteristics string. Order the results by comma.

select 
   id
  ,name
  ,position(',' in characteristics) comma
from monsters m
order by comma asc