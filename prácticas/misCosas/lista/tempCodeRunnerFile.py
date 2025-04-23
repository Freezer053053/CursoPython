    id bigint primary key generated always as identity,
                        name text not null,
                        email text unique not null