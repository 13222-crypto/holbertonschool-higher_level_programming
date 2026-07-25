# Python - Object-relational mapping

This repository contains Python scripts that explore Object-relational mapping (ORM) concepts using `MySQLdb` (MySQL client for Python) and `SQLAlchemy` (Python SQL Toolkit and Object Relational Mapper).

## Requirements

* Python 3.8.5
* MySQL 8.0
* `MySQLdb` module version 2.0.x
* `SQLAlchemy` module version 1.4.x
* Code compliance with `pycodestyle` (v2.8.*)

## Tasks Overview

| File | Description |
| --- | --- |
| `0-select_states.py` | Lists all `states` from the database `hbtn_0e_0_usa`. |
| `1-filter_states.py` | Lists all `states` with a name starting with `N` (upper N) from `hbtn_0e_0_usa`. |
| `2-my_filter_states.py` | Displays all values in the `states` table where `name` matches the argument. |
| `3-my_safe_filter_states.py` | Displays all values in the `states` table matching the argument, protected against SQL injections. |
| `4-cities_by_state.py` | Lists all `cities` from the database `hbtn_0e_4_usa` with their corresponding state names. |
| `5-filter_cities.py` | Takes a state name as an argument and lists all `cities` of that state. |
| `model_state.py` | Python file containing the class definition of a `State` and an instance `Base = declarative_base()`. |
| `7-model_state_fetch_all.py` | Lists all `State` objects from the database `hbtn_0e_6_usa` using SQLAlchemy. |
| `8-model_state_fetch_first.py` | Prints the first `State` object from the database `hbtn_0e_6_usa` using SQLAlchemy. |

## Installation & Setup

```bash
# Install MySQLdb module
sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
sudo pip3 install mysqlclient==2.0.3

# Install SQLAlchemy module
sudo pip3 install SQLAlchemy==1.4.22
