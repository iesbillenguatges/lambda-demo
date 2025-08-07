def handler(event, context):
    name = event.get("name", "món")
    return {
        "statusCode": 200,
        "body": f"Hola, {name}!"
    }
