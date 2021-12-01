# flask-app
### server
- `ubuntu-18.04`

### components
- `uwsgi`: `uwsgi.ini`
- `nginx`
- `supervisor`
- `celery`

### uwsgi
#### 安裝
:::warning
不要安裝在虛擬環境中
:::
* `pip3 insatll uwsgi`

#### 執行命令
* `uwsgi --ini uwsgi.ini`

### nginx
#### 安裝
* `apt install nginx`

#### nginx命令
* `service nginx start`
* `service nginx stop`
* `service nginx restart`
* `service nginx configtest`

#### 配置檔案
```bash=
upstream flask_app{
    server unix:///home/joe/flask_app/uwsgi.sock;
}

server {
    listen      80;
    server_name 192.168.0.100;
    charset     utf-8;

    client_max_body_size 75M;

    location / {
        uwsgi_pass  flask_app;
        include     /etc/nginx/uwsgi_params;
    }
}
```

### supervisor
> c/s架構
#### 安裝
* `pip3 install supervisor`

#### 執行
* `supervisord -c supervisor.conf`

#### 查看
* `supervisorctl -c supervisor.conf`

#### 進入控制台後的常用命令
* `status`
* `start program_name`
* `restart program_name`
* `stop program_name`
* `reload`
* `quit`

