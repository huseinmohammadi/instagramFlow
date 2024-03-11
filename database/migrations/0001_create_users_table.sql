CREATE TABLE IF NOT EXISTS users
(
    id SERIAL PRIMARY KEY,
    first_name varchar(191),
    last_name varchar(191),
    username varchar(191),
    password text,
    email varchar(191),
    instagram_username varchar(191),
    instagram_password text,
    mobile varchar(191),
    created_at timestamp(0) without time zone default current_timestamp,
    updated_at timestamp(0) without time zone default current_timestamp,
    deleted_at timestamp(0) without time zone,
    CONSTRAINT users_mobile_unique UNIQUE (mobile)
)