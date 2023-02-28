FROM python

WORKDIR /app

COPY . .

RUN pip install requests

RUN pip install flask

EXPOSE 81

CMD [ "python", "main.py" ]