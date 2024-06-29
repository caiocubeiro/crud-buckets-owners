CREATE DATABASE buckets_owners;

CREATE TABLE buckets (
    uuid CHAR(36) PRIMARY KEY,
    bucket_name VARCHAR(255) NOT NULL,
    owner_uuid CHAR(36) NOT NULL,
    owner_name VARCHAR(255) NOT NULL,
    owner_email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
);

CREATE TABLE owners (
    uuid CHAR(36) NOT NULL PRIMARY KEY,
    owner_name VARCHAR(255) NOT NULL,
    owner_email VARCHAR(255) NOT NULL UNIQUE,
    owner_department VARCHAR(255),
    owner_manager VARCHAR(255),
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);