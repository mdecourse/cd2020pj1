CREATE TABLE upload(
        id integer primary key autoincrement,
        user text not null,
        date text not null,
        filename text not null,
        memo text
);
