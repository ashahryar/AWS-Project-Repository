import json
import boto3
glueClient = boto3.client('glue')
def lambda_handler(event, context):
	glueClient.start_job_run(JobName="Glue_lambda_ETL_Project")
	return "Job started"