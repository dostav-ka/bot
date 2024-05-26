FROM python:3.10

WORKDIR /app

COPY /api /app
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
RUN export PYTHONPATH=$PYTHONPATH:/app
CMD ["sh", "-c", "sleep 10 && flask db upgrade && python app.py"]