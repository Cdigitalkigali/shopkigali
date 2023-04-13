CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT,
    password_hash TEXT,
    pfp_path TEXT
);
CREATE TABLE IF NOT EXISTS contacts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender_name TEXT,
    sender_email TEXT,
    sender_message TEXT,
    message_read INTEGER
);
CREATE TABLE IF NOT EXISTS blog_posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    posted TEXT,
    author TEXT,
    image_path TEXT,
    content TEXT,
    category TEXT
);
CREATE TABLE IF NOT EXISTS mall_listings(
    id INTEGER,
    mall_name TEXT,
    mall_address TEXT,
    mall_phone TEXT,
    mall_website TEXT,
    mall_opening TEXT,
    mall_closing TEXT,
    mall_description TEXT,
    mall_photo_path TEXT,
    mall_popular INTEGER
);
CREATE TABLE IF NOT EXISTS hotel_listings(
    id INTEGER,
    hotel_name TEXT,
    hotel_address TEXT,
    hotel_phone TEXT,
    hotel_website TEXT,
    hotel_opening TEXT,
    hotel_closing TEXT,
    hotel_description TEXT,
    hotel_photo_path TEXT,
    hotel_popular INTEGER
);
CREATE TABLE IF NOT EXISTS restaurant_listings(
    id INTEGER,
    restaurant_name TEXT,
    restaurant_address TEXT,
    restaurant_phone TEXT,
    restaurant_website TEXT,
    restaurant_opening TEXT,
    restaurant_closing TEXT,
    restaurant_description TEXT,
    restaurant_photo_path TEXT,
    restaurant_popular INTEGER
);
