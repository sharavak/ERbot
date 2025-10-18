FROM python:3.12-slim

RUN mkdir -p app/frontend

COPY . app/frontend

WORKDIR /app/frontend


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8501   

ENTRYPOINT ["streamlit","run"]
CMD ["Home.py"]