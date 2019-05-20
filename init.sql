PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

-- CREATE TABLE alembic_version (
--         version_num VARCHAR(32) NOT NULL, 
--         CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
-- );
-- INSERT INTO alembic_version VALUES('1584d836f365');

CREATE TABLE citizen (
        citizen_id VARCHAR(12) NOT NULL, 
        name VARCHAR(64), 
        password_hash VARCHAR(128), 
        permission VARCHAR(20), 
        score FLOAT, 
        completed_signup INTEGER,
        profile_image VARCHAR(100),
        bio VARCHAR(200),
        fav_leader VARCHAR(30),
        income INTEGER,
        PRIMARY KEY (citizen_id)
);

-- CREATE INDEX ix_citizen_name ON citizen (name);
-- CREATE INDEX ix_citizen_permission ON citizen (permission);

CREATE TABLE report (
        reporter_id VARCHAR(12), 
        reported_id VARCHAR(12), 
        report_id INTEGER NOT NULL, 
        time DATETIME, 
        report_category VARCHAR(64), 
        body VARCHAR(140), 
        PRIMARY KEY (report_id), 
        FOREIGN KEY(reported_id) REFERENCES citizen (citizen_id), 
        FOREIGN KEY(reporter_id) REFERENCES citizen (citizen_id)
);
-- CREATE INDEX ix_report_time ON report (time);

CREATE TABLE status (
        citizen_id VARCHAR(12), 
        status_id INTEGER NOT NULL, 
        timestamp DATETIME, 
        status_category VARCHAR(64), 
        body VARCHAR(140), 
        PRIMARY KEY (status_id), 
        FOREIGN KEY(citizen_id) REFERENCES citizen (citizen_id)
);
-- CREATE INDEX ix_status_timestamp ON status (timestamp);

CREATE TABLE image (
        image_id INTEGER, 
        image_url VARCHAR(100),
        PRIMARY KEY (image_id)
);

INSERT INTO citizen VALUES('0000','0000','pbkdf2:sha256:150000$6dO5sbLc$8923805575b7493d976e1881bf30793c999fb22cb96513daf0dc9b38682ad1a0','admin',NULL,70000.0,'/static/assets/blank_profile.png',NULL,NULL,NULL);

COMMIT;