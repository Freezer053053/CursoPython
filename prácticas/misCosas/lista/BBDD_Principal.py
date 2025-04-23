import sqlite3
from io import open
from utils import emergentes

miConexion = None
miCursor = None

miConexion=sqlite3.connect("BBDD_P.db")
miCursor=miConexion.cursor()

miCursor.execute('''

                    create table users (
                    id bigint primary key generated always as identity,
                    name text not null,
                    email text unique not null
                    );

                    create table capacitors (
                    id bigint primary key generated always as identity,
                    user_id bigint references users (id),
                    type text check (
                        type in (
                        'electrolítico',
                        'electrolítico SMD',
                        'cerámico',
                        'cerámico SMD',
                        'film',
                        'mica',
                        'variable'
                        )
                    ),
                    polarized boolean,
                    capacitance numeric,
                    voltage numeric,
                    quantity int
                    );

                    create table diodes (
                    id bigint primary key generated always as identity,
                    user_id bigint references users (id),
                    type text check (type in ('Zener', 'Zener SMD', 'Led', 'Led SMD')),
                    color text,
                    voltage numeric,
                    quantity int
                    );

                    create table resistors (
                    id bigint primary key generated always as identity,
                    user_id bigint references users (id),
                    resistance_value numeric,
                    tolerance numeric,
                    power_rating numeric,
                    quantity int
                    );

                    create table chips (
                    id bigint primary key generated always as identity,
                    user_id bigint references users (id),
                    model text,
                    manufacturer text,
                    quantity int
                    );

                    create table transistors (
                    id bigint primary key generated always as identity,
                    user_id bigint references users (id),
                    type text,
                    hfe numeric,
                    max_voltage numeric,
                    quantity int
                    );

                    alter table chips
                    add column type text check (
                    type in ('rom', 'microprocessor', 'cmos', 'eeprom', 'etc')
                    );

                    create table capacitor_types (
                    id bigint primary key generated always as identity,
                    type text unique not null
                    );

                    create table diode_types (
                    id bigint primary key generated always as identity,
                    type text unique not null
                    );

                    create table chip_types (
                    id bigint primary key generated always as identity,
                    type text unique not null
                    );

                    alter table capacitors
                    drop constraint if exists capacitors_type_check;

                    alter table capacitors
                    add constraint capacitors_type_fk foreign key (type) references capacitor_types (type);

                    alter table diodes
                    drop constraint if exists diodes_type_check;

                    alter table diodes
                    add constraint diodes_type_fk foreign key (type) references diode_types (type);

                    alter table chips
                    drop constraint if exists chips_type_check;

                    alter table chips
                    add constraint chips_type_fk foreign key (type) references chip_types (type);

                    create table chip_packages (
                    id bigint primary key generated always as identity,
                    package_type text unique not null
                    );

                    alter table chips
                    add column package_type text;

                    alter table chips
                    add constraint chips_package_fk foreign key (package_type) references chip_packages (package_type);

                    create table diode_colors (
                    id bigint primary key generated always as identity,
                    color text unique not null
                    );

                    alter table diodes
                    drop constraint if exists diodes_color_check;

                    alter table diodes
                    add constraint diodes_color_fk foreign key (color) references diode_colors (color);

                    alter table diodes
                    drop constraint if exists diodes_color_check;

                    alter table diodes
                    add constraint diodes_color_check check (
                    (
                        type = 'Zener'
                        and color is null
                    )
                    or (
                        type <> 'Zener'
                        and color is not null
                    )
                    );

        ''')