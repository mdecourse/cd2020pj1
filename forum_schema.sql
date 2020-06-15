CREATE TABLE forum(
        id integer primary key autoincrement,
        title text not null,
        follow integer,
        user text not null,
        date text not null,
        content text,
        files text,
        memo text
);