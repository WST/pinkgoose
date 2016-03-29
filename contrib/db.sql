
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username VARCHAR(64),
	password VARCHAR(32)
);

CREATE TABLE posts (
	id SERIAL PRIMARY KEY,
	slug VARCHAR(50) NOT NULL DEFAULT '',
	title VARCHAR(255) NOT NULL DEFAULT '',
	published BOOL NOT NULL DEFAULT false,
	published_at BIGINT NOT NULL DEFAULT 0,
	intro TEXT NOT NULL,
	fulltext TEXT NOT NULL,
	author_id INTEGER NOT NULL DEFAULT 0
);