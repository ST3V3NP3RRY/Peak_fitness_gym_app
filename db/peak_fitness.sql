DROP TABLE members;
DROP TABLE activities;
DROP TABLE sessions;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE activity (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    title VARCHAR(255)
);

CREATE TABLE sessions (
id SERIAL PRIMARY KEY,
members_id INT REFERENCES members(id),
activity_id INT REFERENCES activity(id),
date DATE,
time INT,
duration INT
);