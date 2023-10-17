FROM python:3.11

WORKDIR /backend

COPY backend/requirements.txt .

RUN pip install -r requirements.txt

# python-opencv dependencies
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY backend/ . 

EXPOSE 8000
CMD ["python", "manage.py", "runserver"]