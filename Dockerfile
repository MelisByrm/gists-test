FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get install -y --no-install-recommends unzip curl && \
    curl --retry 5 --retry-connrefused -sLo /tmp/allure.zip https://github.com/allure-framework/allure2/releases/latest/download/allure-2.22.5.zip && \
    test -f /tmp/allure.zip && \
    unzip /tmp/allure.zip -d /tmp/ && \
    mv /tmp/allure-2.22.5 /opt/allure && \
    ln -s /opt/allure/bin/allure /usr/bin/allure && \
    rm -rf /tmp/allure.zip /var/lib/apt/lists/*

RUN chmod +x ./run_critical_cases.sh ./run_medium_priority_tests.sh

CMD ["behave"]
