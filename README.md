# This FLASK's structure is used with: #

* Nginx is running as reverse proxy
* uWSGI is running as master process for flask
* Running with systemd service
* OS Centos 7

### What is this repository for? ###

* flask development for small application
* 0.1

### How do I get set up? ###

* Set up the wsgi.ini - see the wsgi.ini for sample
* Set up the wsgi.service - see the wsgi.serivce for sample
* Set up the nginx server - see nginx.conf for sample
* Configuration
  - usermod -a -G hadn nginx
  - chmod 710 /home/hadn
  - cp file nginx.conf into nginx conf folder
  - cp file wsgi.service into /etc/systemd/system folder
  - start nginx, wsgi service by: systemctl start nginx/wsgi
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions
* [Reference link](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-centos-7)

### Contribution guidelines ###

* Steps to git release
  - git tag -a v0.1 -m "finish guide for nginx and uwsgi"
  - git push --tags
* Steps to git delete release/tag
  - # delete local tag '12345'
    + git tag -d 12345
  - # delete remote tag '12345' (eg, GitHub version too)
    + git push origin :refs/tags/12345
  - # alternative approach
    + git push --delete origin tagName
    + git tag -d tagName
* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact