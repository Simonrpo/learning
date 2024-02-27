with tabla_ppal as (
SELECT 
t1.CountryCode,
row_number() over(partition by t1.CountryCode order by t1.Population desc) RowNumberColumn,
t1.District,
t1.Population,
sum(t1.Population) over(partition by t1.CountryCode) PoblacionPais
FROM world.city t1
where t1.CountryCode not in ("ABW")
order by 1 asc)
Select
*,
(Population / PoblacionPais) * 100 as PorcentajeDistritoPais
from tabla_ppal
where CountryCode = "COL";
