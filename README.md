# calluna
Imports Rundata file data into Postgres DB.

Dependencies: Python 3.5, xlrd, pg8000, PostgreSQL, Rundata "mac" version files

Current schema:

CREATE TABLE rune_info (id SERIAL PRIMARY KEY, sign text, place text);