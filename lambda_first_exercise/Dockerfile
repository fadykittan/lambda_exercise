#FROM amazonlinux:2

# Install basic tools and Python 3.9 (or 3.11 if you use a newer runtime)
FROM public.ecr.aws/lambda/python:3.9

# Install system dependencies
RUN yum install -y \
    zip \
    unzip \
    && yum clean all

# Set working directory
WORKDIR /layer

# Create the package directory
RUN mkdir -p python/lib/python3.9/site-packages

# Install packages to that directory
RUN pip3 install scikit-learn -t python/lib/python3.9/site-packages/

# Zip the content
RUN cd python && zip -r ../layer.zip .
