FROM python:3.9
COPY main.py /app/main.py
EXPOSE 8000
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install fastapi uvicorn
RUN pip install git+https://github.com/suno-ai/bark.git
RUN test -d /root/.cache || mkdir -p /root/.cache
COPY cache/. /root/.cache/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]