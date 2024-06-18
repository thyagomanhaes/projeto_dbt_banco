{{
	config(materialized='table')
}}

SELECT 
	c.city_id
	, c.city
	, c.state_id 
	, s.state 
	, s.country_id 
	, c2.country 
FROM {{ source('bronze', 'city') }} c
left join transacional.state s on s.state_id = c.state_id
left join transacional.country c2 on c2.country_id = s.country_id