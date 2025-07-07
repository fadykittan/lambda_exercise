# Use the official AWS Lambda Python 3.11 base image
FROM public.ecr.aws/lambda/python:3.11

# Set working directory
WORKDIR /var/task

# Copy requirements and install dependencies
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Set the CMD to your handler (for Lambda) or run Flask for local dev
# For Lambda, the handler would be: app.lambda_handler (if using AWS Lambda Powertools or similar)
# For local dev, you can override the CMD to run Flask

CMD ["app.lambda_handler"] 