# Follow / Unfollow

POST /api/accounts/follow/<user_id>/
Auth: Token <token>

POST /api/accounts/unfollow/<user_id>/
Auth: Token <token>

# Feed

GET /api/feed/
Auth: Token <token>
Returns latest posts from users you follow, ordered by -created_at
