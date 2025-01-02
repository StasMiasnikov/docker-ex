FROM jenkins/jenkins
USER root
RUN apt-get update && apt-get install -y \
    ca-certificates \
    wget \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

ADD *.crt  /usr/local/share/ca-certificates/
RUN update-ca-certificates

RUN for cert in /usr/local/share/ca-certificates/*.crt; do \
        CERT_NAME=$(basename "$cert" .crt) && \
        keytool -import -noprompt -trustcacerts -alias "$CERT_NAME" -file "$cert" -keystore "$JAVA_HOME/lib/security/cacerts" -storepass changeit; \
    done
USER jenkins
RUN jenkins-plugin-cli --plugins git blueocean configuration-as-code workflow-multibranch ssh-slaves job-dsl
