import openai

openai.api_key = 'api_key'

def lambda_handler(event, context):
    if 'm' in event['params']['querystring']:
        input_message = event['params']['querystring']['m']
    else:
        input_message = '나는 신투증에 입사하려는데, 클라우드 배울 필요가 있어?'
    
    message = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages=[
            {"role":"system","content":"너는 클라우드 전문가야 핵심만 말해"},
            {"role":"user","content":input_message}
            ]
        )
    
    return message
