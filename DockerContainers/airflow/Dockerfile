# Use the official Apache Airflow image as a base image
FROM apache/airflow:2.7.2

# Install Apache Beam and its dependencies
RUN pip install apache-beam[gcp]
RUN pip install pyyaml


# Optionally, you can install any other dependencies you need

# Set the user
USER ${AIRFLOW_UID:-50000}:0



###### apache beam

# This can be any container image,
# FROM python:3.7

# Install SDK. (needed for Python SDK)
# RUN pip install --no-cache-dir apache-beam[gcp]==2.48.0

# Copy files from official SDK image, including script/dependencies.
# COPY --from=apache/beam_python3.7_sdk:2.48.0 /opt/apache/beam /opt/apache/beam

# # Perform any additional customizations if desired

# # Set the entrypoint to Apache Beam SDK launcher.
# ENTRYPOINT ["/opt/apache/beam/boot"]
