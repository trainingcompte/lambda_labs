import json 

def lambda_handler(event, context):
    # TO DO implement
    print(' C est ma fonction AWS Lambda pour juste tester')
    if event['planete'] == 'Terre':
        return 'Lune'
    elif event['planete'] == 'Soleil'
        return 'C n est pas une planete'
    else:
        return 'Je ne comprends pas votre argument!!'