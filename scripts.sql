-- Задание 1
select c.login, count(*) AS ordersCountInDelivery
from "Couriers" AS c
join "Orders" AS o
on c.id = o."courierId"
where o."inDelivery" = true
group by c.login;

-- Задание 2
select o.track,
(
	case
	when o.finished = True then 2
	when o.cancelled = True then -1
	when o."inDelivery" = True then 1
	else 0
	end
) AS status
from "Orders" AS o;

