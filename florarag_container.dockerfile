FROM python:3.11

WORKDIR /florarag_platform

COPY . .

RUN pip install -r florarag_requirements.txt

CMD ["python", "florarag_pipeline_runner.py"]
