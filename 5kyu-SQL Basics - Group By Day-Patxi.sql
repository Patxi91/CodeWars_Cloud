SELECT DATE(created_at) as day, description, COUNT(*) as count
FROM events
GROUP BY name, day, description
HAVING name = 'trained'