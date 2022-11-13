import json
import requests
import base64


class QYWXServer:
    def __init__(self, cid, aid, secret, scheduler):
        self.cid = cid 
        self.aid = aid 
        self.secret = secret
        self.scheduler = scheduler

    def send(self, text, wecom_touid='@all'):
        get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.cid}&corpsecret={self.secret}"
        response = requests.get(get_token_url).content
        access_token = json.loads(response).get('access_token')
        if access_token and len(access_token) > 0:
            send_msg_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
            data = {
                "touser":wecom_touid,
                "agentid":self.aid,
                "msgtype":"text",
                "text":{
                    "content":text
                },
                "duplicate_check_interval":600
            }
            response = requests.post(send_msg_url,data=json.dumps(data)).content
            print(text)
            print(response)
            return response
        else:
            return False

    '''
    def send_to_wecom_image(base64_content, wecom_touid='@all'):
        get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={wecom_cid}&corpsecret={wecom_secret}"
        response = requests.get(get_token_url).content
        access_token = json.loads(response).get('access_token')
        if access_token and len(access_token) > 0:
            upload_url = f'https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={access_token}&type=image'
            upload_response = requests.post(upload_url, files={
                "picture": base64.b64decode(base64_content)
            }).json()
            if "media_id" in upload_response:
                media_id = upload_response['media_id']
            else:
                return False

            send_msg_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
            data = {
                "touser":wecom_touid,
                "agentid":wecom_aid,
                "msgtype":"image",
                "image":{
                    "media_id": media_id
                },
                "duplicate_check_interval":600
            }
            response = requests.post(send_msg_url,data=json.dumps(data)).content
            return response
        else:
            return False

    def send_to_wecom_markdown(text,wecom_cid,wecom_aid,wecom_secret,wecom_touid='@all'):
        get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={wecom_cid}&corpsecret={wecom_secret}"
        response = requests.get(get_token_url).content
        access_token = json.loads(response).get('access_token')
        if access_token and len(access_token) > 0:
            send_msg_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
            data = {
                "touser":wecom_touid,
                "agentid":wecom_aid,
                "msgtype":"markdown",
                "markdown":{
                    "content":text
                },
                "duplicate_check_interval":600
            }
            response = requests.post(send_msg_url,data=json.dumps(data)).content
            return response
        else:
            return False
    '''