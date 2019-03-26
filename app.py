from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
    	token_sent=request.args.get("hub.verify_token")
    	return verify_fb_token(token_sent)
    else:
    	output=request.get_json()
    	for even in output['entry']:
    		messaging=event['messaging']
    		for message in messaging:
    			if message.get('message'):
    				recipient_id=message['sender']['id']
    				if message['message'].get('text'):
    					response_sent_text=get_message()
    					send_message(recipient_id,response_sent_text)
    				if message['message'].get('attachments'):
    					response_sent_nontext=get_message()
    					send_message(recipient_id,response_sent_nontext)
    	return "Message processed"						

def verify_fb_token(token_sent):
	if token_sent=="EAAkbo0OIjqwBAIZBtZCkentMQyUZBCMBESfbr5My62p1S67Ohy0RHdQw7kHIQIxZBFJ8gZBxG4bplCSXMjjvWorU4jJgjcUZAhZCYomKns6Ek0ynYXJpNwqFMkOblN7JHvPJvP3MZBdRi8FkSZCywNQU0S6j1zeKriFUf2LHdsk38P0IZCX1FOu6bPc0Fsh0GphxwZD":
		return request.args.get("hub.challenge")
	return 'invalid verification token'
	
def send_message(recipient_id,response):
	bot.send_text_message(recipient_id,response)
	return "success"		


if __name__ == '__main__':
    app.run()