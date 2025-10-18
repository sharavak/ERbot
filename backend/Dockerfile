FROM python:3.12
RUN mkdir -p app/backend

COPY backend/requirements.txt app/backend/requirements.txt
COPY backend app/backend

WORKDIR /app/backend


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000   

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ,"--reload"]