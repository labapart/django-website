Abstract
--------
Web hosting providers (eg: OVH) do not always provide django support as part of their python modules.
This github project provides a template to create and deploy a Django website for these web hosting providers.

This base website template contains all the required modules by django 1.6 - including PostgreSQL support.

This project is also covered in this blog: http://labapart.com/blogs/1-powerful-django-development-process-for-your-cheap-web-hosted-website

Starting a new django website
-----------------------------

1.   Clone this github project

    ```
    git clone https://github.com/labapart/django-website.git
    ```

2.   Create a new django application (or import your existing django application)

    ```
    cd django-website
    django-admin startproject mysite
    ```

3.   Review and update:
    -    `mysite-www/deploy.cgi`
    -    `mysite-www/django.cgi`
    -    `deploy.py`
4.    Set your web hosting information in `.git/ftpdata`  
    For instance:
    ```
    [master]
    username=olivier
    hostname=localhost
    remotepath=/srv/mysite/django-website
    www_directory=mysite-www
    
    [production]
    username=mysite
    hostname=ftp.mysite.com
    remotepath=/django-website
    www_directory=mysite-www
    ```
5. Deploy the website on your web hosting
    ```
    ./deploy.sh -s production
    ```

Run the django project locally
------------------------------
```
./mysite/manage.py syncdb
./mysite/manage.py runserver
```

Good practise
-------------
The django settings have been splitted into 3 files to differentiate the local and production specific settings (eg: Debug support, hostname, database).
```
mysite/mysite
├── settings
│   ├── base.py
│   ├── __init__.py
│   ├── local.py
│   ├── production.py
```

Note
----
`deploy.py` is based on <https://github.com/ezyang/git-ftp>. I encourage you to backport any features or bug fixes to this other github project.

License
-------

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

