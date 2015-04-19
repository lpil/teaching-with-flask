drop table if exists posts;
create table posts (
  id integer primary key autoincrement,
  title string not null,
  text text not null
);
