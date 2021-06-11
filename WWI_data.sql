create table wwi_aerial_attack(
Aircraft_id int,
AIRCRAFT varchar (1200),
FULL_NAME varchar (1200),
Aircraft_type varchar (1200),
HYPERLINK varchar (1200)
);

create table wwi_aerial_attack(
WWI_ID int,
MSNDATE date,
COUNTRY varchar (1200),
SERVICE varchar (1200),
UNIT varchar (1200),
MDS varchar (1200),
TAKEOFFTIME varchar (1200),
NUMBEROFPLANESATTACKING varchar(1200),
WEAPONTYPE varchar (1200),
WEAPONWEIGHT dec,
BOMBLOAD dec,
LATITUDE dec,
LONGITUDE dec,
TGTLOCATION varchar (1200),
TGTCOUNTRY varchar (1200),
TGTTYPE varchar (1200),
TAKEOFFBASE varchar (1200),
TAKEOFFLATITUDE dec,
TAKEOFFLONGITUDE dec, 
FRIENDLYCASUALTIES varchar(1200),
ALTITUDE dec
);


create table wwi_weapon_data(
ID int,
COUNTRY varchar (1200),
WEAPON_NAME varchar (1200),
WEAPON_CLASS varchar (1200),
WEAPON_DESCRIPTION varchar (1200)
);

select * from wwi_weapon_data;