USE socialapp;

SELECT users.first_name, users.last_name, user2.first_name AS friend_f_name, user2.last_name AS friend_l_name FROM users
LEFT JOIN friendships ON friendships.user_id = users.id
LEFT JOIN users as user2 on user2.id = friendships.friend_id