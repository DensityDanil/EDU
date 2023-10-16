with Produce AS (
  SELECT 'Kale' as product, 51 as sales, 'Q1' as quarter UNION ALL
  SELECT 'Kale', 23, 'Q2' UNION ALL
  SELECT 'Kale', 45, 'Q3' UNION ALL
  SELECT 'Kale', 3, 'Q4' UNION ALL
  SELECT 'Apple', 77, 'Q1' UNION ALL
  SELECT 'Apple', 0, 'Q2' UNION ALL
  SELECT 'Apple', 25, 'Q3' UNION ALL
  SELECT 'Apple', 2, 'Q3')



SELECT * FROM
(SELECT product, sales, quarter FROM Produce)
PIVOT(SUM(sales) FOR quarter IN ('Q1', 'Q3', 'Q4'))
