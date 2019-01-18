# The Mwebaza Enterprise
The familie Portal of Mr Kyagulanyi Vicent. Is a user specific environment for familie members 

### Contributing? How to get started 
Using Pycharm? 
-  `git clone https://github.com/pmutale/fam-kyagulanyi-cms.git`
-  `cd fam-kyagulanyi-cms`
-  Create a virtual environment `virtualenv venv`
-  Install requirements `pip install -r requirements.txt`
-  Create a new branch according to issue you are working on `git checkout -b { MILESTONE }-{ BRANCH-NAME }` e.g. `git checkout -b 1-Adding-Bootstrap`
-  Set upstream to remote with `git push -u origin { NAME OF NEW BRANCH }` e.g. `git push -u origin 1-Adding-Bootstrap`
-  In github - add a milestone, a project and create or add existing tags
-  Start CODING

#### Database Setup
Postgres?
-  Create a `.pgpass` file in the format
 
```hostname:port:database:username:password:commit```
-  PSQL into postgres `sudo -u posgres psql`
-  Create database *mwebaza_enterprise* with password => _mwebaza_
   ```
    CREATE DATABASE mwebaza_enterprise;
    CREATE USER youruser WITH ENCRYPTED PASSWORD 'mwebaza';
    GRANT ALL PRIVILEGES ON DATABASE mwebaza TO mwebaza;
    ```
    
-  Run migrations with `python manage.py migrate`
-  Create a superuser `python manage.py createsuperuser --username xxx --email example@example.domain`
