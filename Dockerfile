FROM python
COPY / /
RUN pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/
RUN pip install -r requirement.txt -i https://mirrors.aliyun.com/pypi/simple/
CMD gunicorn --bind 0.0.0.0:8000 wsgi:app
