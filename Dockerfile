FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install allure-behave

RUN chmod +x ./run_critical_cases.sh ./run_medium_priority_tests.sh

CMD ["behave"]
