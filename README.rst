============================
Installation for development
============================

#. Install nginx::

    sudo apt-get install nginx
    curl http://localhost/
    sudo rm /etc/nginx/sites-enabled/default

#. Install and configure git::

    sudo apt-get install git
    git config --global user.name 'Firstname Lastname'
    git config --global user.email 'youremail@youremail_domain.com'

#. Fork upstream repository git@github.com:findbyanswers/startbootstrap-one-page-wonder.git
#. Clone repository::

    git clone <address of forked repository>

#. Add upstream::

    cd startbootstrap-one-page-wonder
    git remote add upstream git@github.com:findbyanswers/startbootstrap-one-page-wonder.git
    git fetch upstream

#. Install prerequisites::

    sudo apt-get install python-dev python-pip
    sudo pip install virtualenv

#. Create virtual environment and install dependencies::

    virtualenv ENV
    . ENV/bin/activate
    pip install -e .

#. Add name to /etc/hosts::

    sudo su
    echo '127.0.0.1 findbyanswers.development' >> /etc/hosts
    exit

#. Generate nginx configuration file::

    mkdir local
    python -m findbyanswers_website.generate_nginx_config --server-name=findbyanswers.development > local/nginx.conf

#. Create symlink to site configuration file::

    ln -s $PWD/local/nginx.conf /etc/nginx/sites-enabled/findbyanswers.conf

#. Reload nginx configuration::

    sudo service nginx reload

#. Test development installation::

    curl http://findbyanswers.development
    firefox http://findbyanswers.development &
    google-chrome http://findbyanswers.development &

===========================
Installation for production
===========================

#. Generate nginx configuration file::

    python -m findbyanswers_website.generate_nginx_config --server-name=findbyanswers.com
