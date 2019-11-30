# Django 프레임웍 테스트

RDS MySQL, S3 연동.

## 환경
- RDS MySQL 5.7 DB, SSL 연결.
- S3 버킷 생성, 퍼블릭 엑세스 설정.
- EC2에 mysqlclient 설치, Nginx 설치(80->8000 포워딩)
- gunicorn으로 구동.

## 설치
```
$ git clone THIS_REPOSITORY_CLONE_URL
$ vi gramming/.env
SECRET_KEY=
DEBUG=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=
AWS_REGION=
AWS_DEFAULT_ACL=public-read
DB_ENGINE=django.db.backends.mysql
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip3 install -r package.txt
(venv) $ python3 manage.py migrate
(venv) $ python3 manage.py createsuperuser
(venv) $ gunicorn -b 0.0.0.0:8000 -D gramming.wsgi:application
(venv) $ cat gramming/urls.py
```

