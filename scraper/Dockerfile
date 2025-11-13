
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install playwright requests
RUN playwright install
CMD ["python", "run_daily.py"]
