DROP TABLE sessions;
DROP TABLE activities;
DROP TABLE members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    address VARCHAR(255)
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    start_time INT,
    duration INT
);

CREATE TABLE sessions (
id SERIAL PRIMARY KEY,
member_id INT REFERENCES members(id) ON DELETE CASCADE,
activity_id INT REFERENCES activities(id) ON DELETE CASCADE,
date DATE --Change this to date later int just placeholder to get things working
);