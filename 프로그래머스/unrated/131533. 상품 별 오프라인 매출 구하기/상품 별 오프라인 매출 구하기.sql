-- 코드를 입력하세요
SELECT a.PRODUCT_CODE,b.sum*(a.price) as SALES
from product as a
join (select product_id,sum(sales_amount) as sum
      from offline_sale
      group by product_id) as b
on a.product_id=b.product_id
order by SALES desc,a.product_code asc