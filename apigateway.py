import json
import os
import mercadopago

def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN"])
    bodyGet = json.loads(event["body"])

    payment_data = {
        "token": bodyGet["token"],
        "installments": int(bodyGet["installments"]),
        "payment_method_id": bodyGet["payment_method_id"],
        "transaction_amount": int(bodyGet["transaction_amount"]),
        "payer": {
            "email": bodyGet["payer"]["email"],
            "identification": {
                "type": bodyGet["payer"]["identification"]["type"], 
                "number": bodyGet["payer"]["identification"]["number"]
            }
        }
    }

    payment_response = sdk.payment().create(payment_data)
    return{
        "statusCode": 201,
        "body": json.dumps(
            payment_response["response"]
        ),
        
    }