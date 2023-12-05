FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY S3app ${LAMBDA_TASK_ROOT}/S3app
ENV PYTHONPATH=${LAMBDA_TASK_ROOT}/S3app

CMD [ "S3app.lambda_ingest" ]