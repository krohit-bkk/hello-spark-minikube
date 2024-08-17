FROM bitnami/spark:3.5.0
WORKDIR /opt
COPY spark_etl.py /opt/