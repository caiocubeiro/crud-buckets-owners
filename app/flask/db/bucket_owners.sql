CREATE DATABASE buckets_owners;

CREATE TABLE buckets (
    uuid CHAR(36) PRIMARY KEY,
    bucket_name VARCHAR(255) NOT NULL,
    owner_name VARCHAR(255) NOT NULL,
    owner_email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
);
