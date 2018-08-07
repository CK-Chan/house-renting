FROM python:3.6

COPY . /yelp-crawler/crawler

VOLUME /etc/scrapyd/ /var/lib/scrapyd/

WORKDIR /yelp-crawler/crawler

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
