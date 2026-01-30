users = """
    CREATE TABLE IF NOT EXISTS users (
    id              BIGSERIAL PRIMARY KEY,
    chat_id         BIGINT UNIQUE NOT NULL,
    username        VARCHAR(255) NOT NULL,
    full_name       VARCHAR(255) NOT NULL,
    language        VARCHAR(2) NOT NULL DEFAULT 'UZ',
    phone_number    VARCHAR(13) UNIQUE NOT NULL,
    longitude        VARCHAR(64) NOT NULL,
    latitude        VARCHAR(64) NOT NULL,
    student_id      BIGINT ,
    crated_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""
