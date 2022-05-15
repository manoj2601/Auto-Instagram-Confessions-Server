DROP TABLE accounts;
CREATE TABLE accounts (
        username VARCHAR (255) UNIQUE NOT NULL,
        password VARCHAR (255),
        last_login TIMESTAMP
);

INSERT INTO accounts (username, password) VALUES ('manoj', 'manoj');

DROP TABLE entries;
CREATE TABLE entries (
        id  SERIAL PRIMARY KEY,
        entry TEXT NOT NULL
);

DROP TABLE accepted;
CREATE TABLE accepted (
        id INT UNIQUE NOT NULL
);

DROP TABLE declined;
CREATE TABLE declined (
        id INT UNIQUE NOT NULL
);

DROP TABLE skipped;
CREATE TABLE skipped (
        id INT UNIQUE NOT NULL
);
