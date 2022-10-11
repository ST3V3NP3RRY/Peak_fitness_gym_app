DROP TABLE bookings;
DROP TABLE sessions;
DROP TABLE activities;
DROP TABLE members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    address TEXT
);

CREATE TABLE activities (
id SERIAL PRIMARY KEY,
name VARCHAR
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    time INT,
    duration INT,
    activity_id INT REFERENCES activities(id) ON DELETE CASCADE
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    session_id INT REFERENCES sessions(id) ON DELETE CASCADE
);



