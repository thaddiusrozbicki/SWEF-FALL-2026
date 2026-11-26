create table members (
  id bigint generated always as identity primary key,
  name text not null,
  email text not null unique,
  hometown text,
  major text,
  tamid_class text
);

insert into members (name, email, hometown, major, tamid_class) values
  ('Rio Quinn',         'quinn.gre@northeastern.edu',   'Millbrook', 'Math',        'Alef'),
  ('Shaurya Dubey',     'dubey.shau@northeastern.edu',  'Princeton', 'CS',          'Alef'),
  ('Issa Rada',         'radasilva.i@northeastern.edu', 'Bogota',    'CS, Finance', 'Tav'),
  ('Thaddius Rozbicki', 'rozbicki.t@northeastern.edu',  'Saratoga',  'Business Administration and Economics', 'Bet');

alter table members enable row level security;

create policy "own row or admin can read"
on members for select
to authenticated
using (
  email = (auth.jwt() ->> 'email')
  or (auth.jwt() ->> 'email') = 'admin@tamidswef.org'
);

create view members_public as
  select id, name, major, tamid_class from members;

revoke all on members_public from anon, authenticated;
grant select on members_public to authenticated;
