import os
import boto3
from boto3.dynamodb.conditions import Key
import uuid


def _get_database():
    # DynamoDBへの接続を修得する
    endpoint = os.environ.get('DB_ENDPOINT')
    if endpoint:
        return boto3.resource('dynamodb', endpoint_url=endpoint)
    else:
        return boto3.resource('dynamodb')


def get_all_todos():
    # すべてのレコードを修得
    table = _get_database().Table(os.environ['DB_TABLE_NAME'])
    response = table.scan()
    return response['Items']


def get_todo(todo_id):
    # IDからレコードを修得
    table = _get_database().Table(os.environ['DB_TABLE_NAME'])
    response = table.query(
        KeyConditionExpression=Key('id').eq(todo_id)
    )
    items = response['Items']
    return items[0] if items else None


def create_todo(todo):
    # 登録内容を作成
    item = {
        'id': uuid.uuid4().hex,
        'title': todo['title'],
        'memo': todo['memo'],
        'priority': todo['priority'],
        'completed': False,
    }

    # DynamoDB にデータ登録
    table = _get_database().Table(os.environ['DB_TABLE_NAME'])
    table.put_item(Item=item)
    return item