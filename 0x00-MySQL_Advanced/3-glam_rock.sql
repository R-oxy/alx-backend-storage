-- Ranking bands with Glam rock style by longevity until 2022

SELECT band_name, ifnull(split, 2020)-ifnull(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC
