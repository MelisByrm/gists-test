FROM python:3.12

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get install -y --no-install-recommends unzip curl && \
    curl -sLo allure.zip https://github.com/allure-framework/allure2/releases/download/2.32.0/allure-2.32.0.zip && \
    unzip allure.zip -d /tmp/ && mv /tmp/allure-2.32.0 /opt/allure && \
    ln -s /opt/allure/bin/allure /usr/bin/allure && \
    rm -rf allure.zip /var/lib/apt/lists/*

RUN update-alternatives --set java /usr/lib/jvm/java-11-openjdk-amd64/bin/java && \
    echo "JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64" >> /etc/environment

ENV JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
ENV PATH="$JAVA_HOME/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install allure-behave

RUN chmod +x ./run_critical_cases.sh ./run_medium_priority_tests.sh

CMD ["behave"]
