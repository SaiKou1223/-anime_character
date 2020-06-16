import requests
import base64
def get_access():
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    params = {
        'grant_type':'client_credentials',
        'client_id':'<此处变量涉及个人数据使用次数，看 readme>',
        'client_secret':'<此处变量涉及个人数据使用次数，看 readme>'
    }
    response = requests.get(url,params)
    data = response.json()
    key = data["access_token"]
    # print(key)
    # print(data)
    return key
def get_image(access_token,image_name):
    request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime"
    f = open(image_name, 'rb')
    image = base64.b64encode(f.read())
    headers = {
        'User - Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded'
    }
    params = {"image": image}
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=params, headers=headers)
    content = response.json()
    with open('a11.jpg','wb') as r:
        data = base64.b64decode(content['image'])
        r.write(data)
if __name__ == '__main__':
    access_token = get_access()
    get_image(access_token,'11.jpg')
