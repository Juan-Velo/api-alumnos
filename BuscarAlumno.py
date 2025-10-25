import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # Entrada (json)
    print(event)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    response = table.get_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )
    # Salida (json)
    if 'Item' in response:
        return {
            'statusCode': 200,
            'message': 'Alumno encontrado',
            'alumno': response['Item']
        }
    else:
        return {
            'statusCode': 404,
            'message': 'Alumno no encontrado'
        }
