# The Mwebaza Enterprise
The familie Portal of Mr Kyagulanyi Vicent. Is a user specific environment for familie members 

### Contributing? How to get started 
Using Pycharm? 
  -  `$ git clone https://github.com/pmutale/fam-kyagulanyi-cms.git`
  -  `$ cd fam-kyagulanyi-cms`
  -  Create a virtual environment `$ virtualenv venv`
  -  Install requirements `$ pip install -r requirements.txt`
  -  Create a new branch according to issue you are working on `$ git checkout -b { MILESTONE }-{ BRANCH-NAME }` e.g. `git checkout -b 1-Adding-Bootstrap`
  -  Set upstream to remote with `$ git push -u origin { NAME OF NEW BRANCH }` e.g. `git push -u origin 1-Adding-Bootstrap`
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

#### Styles setup [ Look and feel ]
Semantic UI

  -  Install Semantic UI with `npm`
     
     At the root of your project run the following commands. If you dont have `npm` checkout the
     following guidelines.
    
     -  Install `npm` on Windows 
        https://blog.teamtreehouse.com/install-node-js-npm-windows
        
     -  Install `npm` on Linux
        ```
          $ sudo apt-get update
          $ sudo apt-get install npm nodejs
          $ npm --version # _Should output a version number_
        ```
  -  Build Sematic UI 
      ```
        $ npm install  #Run after npm/node is installed!
        $ npm install semantic-ui --save
            => When asked "Where should we put Semantic UI"... use `static/` folder
        $ npm install gulp --global
        $ cd static/semantic/
        $ gulp build
      ```
  -  Getting started:
     -  In your `etc/hosts` file you should create an endpoint for the application. Edit your hosts
         file and add the following.
        
         `127.0.0.1   mwebaza.localhost`
      
     -  To be able to get the application running. You have to build the scripts and start the server
         ```
          $ npm run watch
         ```

Start your application and if watch runs you should be able to access the project on http://mwebaza.localhost:9090

