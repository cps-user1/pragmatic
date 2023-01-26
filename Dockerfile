FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/cps-user1/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=django-insecure-=0-lwodvareqp-+m4-ynj(9&c!s@bh((g6*xf(rqcuk++k$=ar" > .env

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn","pragmatic.wsgi","--bind","0.0.0.0:8000"]