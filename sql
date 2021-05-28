CREATE DATABASE sigma;
USE sigma;
CREATE TABLE coins (
    id_coin int NOT NULL AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    PRIMARY KEY (id_coin)
);

CREATE TABLE history (
    id_history int NOT NULL AUTO_INCREMENT,
    id_coin int,
    PRIMARY KEY (id_history),
    FOREIGN KEY (id_coin) REFERENCES coins(id_coin)
);

CREATE TABLE suggestions (
    id_suggest int NOT NULL AUTO_INCREMENT,
    id_coin int,
    PRIMARY KEY (id_suggest),
    FOREIGN KEY (id_coin) REFERENCES coins(id_coin)
);

CREATE TABLE users_sigma (
    id_users int NOT NULL AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    mail varchar(100) NOT NULL,
    PRIMARY KEY (id_users)
);

INSERT INTO coins (id_coin, name) VALUES (0, "BITCOIN");
INSERT INTO coins (id_coin, name) VALUES (1, "ETHEREUM");
INSERT INTO coins (id_coin, name) VALUES (2, "DOGE");

INSERT INTO users_sigma (id_users, name, mail) VALUES (0, "Facundo", "ddiiaazzfacu@gmail.com")
INSERT INTO users_sigma (id_users, name, mail) VALUES (1, "Tadeo", "tade.g.17@gmail.com")
INSERT INTO users_sigma (id_users, name, mail) VALUES (2, "Tomas", "tdecastroguelfi@gmail.com")