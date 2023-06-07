-- INSERT INTO attendance (user_id, start_time, end_time) VALUES ('1123456789', '1998-01-23 14:45:56', NULL); -- 1998-01-23 14:45:56
-- SELECT * FROM attendance ORDER BY id DESC LIMIT 1;
-- UPDATE attendance SET swipe_out = '1998-01-23 12:45:56' WHERE user_id = '0123456789' ORDER BY id DESC LIMIT 1;
-- SELECT * FROM attendance;

SELECT t1.*
FROM attendance AS t1
LEFT JOIN attendance AS t2
ON t1.user_id = t2.user_id
AND t1.start_time < t2.start_time
WHERE t2.user_id IS NULL;

SELECT * FROM attendance;