FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y unzip curl && \
    curl -sLo allure.zip https://github.com/allure-framework/allure2/releases/latest/download/allure-2.22.5.zip && \
    unzip allure.zip -d / && \
    mv /allure-2.22.5 /allure && \
    ln -s /allure/bin/allure /usr/bin/allure && \
    rm allure.zip \

RUN chmod +x ./run_critical_cases.sh ./run_medium_priority_tests.sh

CMD ["behave"]
