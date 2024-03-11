CREATE TABLE IF NOT EXISTS accounts
(
    id SERIAL PRIMARY KEY,
    instagram_id varchar(191),
    username varchar(191),
    profile_pic_url text,
    typename text,
    created_at timestamp(0) without time zone default current_timestamp,
    updated_at timestamp(0) without time zone default current_timestamp,
    deleted_at timestamp(0) without time zone
)