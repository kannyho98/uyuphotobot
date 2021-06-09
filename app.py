import json
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import QA_Col
import random

app = Flask(__name__)


line_bot_api = LineBotApi('6D3uPq6/EcQM2HSo89EogoTUscTIk8+cwXsrOShGEI76TpOAZQmkpvL7pwQP0YAenayWQYWqrQ7S0sATZvqx5CdMQ9/qLcV5BN3D07H67Eei/chJB6d1IUCXxtrr4PMlYfhHxEjRQavohaJs6te17QdB04t89/1O/w1cDnyilFU=')

handler = WebhookHandler('83de04c484d27744f7e928ba03e74c9f')

line_bot_api.push_message('Uda7c7cd63b657df623242b5985af6baf', TextSendMessage(text='System Testing！！若您覺得訊息干擾到您，您可以將聊天室設為靜音，感謝！'))

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

######################處理LINE USER 傳來得訊息 ###############################
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user id when reply
    
    profile = line_bot_api.get_profile(event.source.user_id)
    nameid = profile.display_name     #使用者名稱
    uid = profile.user_id             #使用者ID  
    user_message=str(event.message.text) 
    

        #user_message='圖文訊息'
    if user_message.find('各種查詢') != -1:    
        
        res_message = TemplateSendMessage(
            alt_text='各種查詢',
            template = CarouselTemplate(
                columns=[
#-----------------------------------------------------------------------------                    
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='拍攝服務',
                        text='請在下方選出您需要的服務！',
                        actions=[
                            MessageTemplateAction(
                                label='人像拍攝',
                                text='人像拍攝'
                            ),
                            MessageTemplateAction(
                                label='商業拍攝',
                                text='商業拍攝'
                            ),
                        ]
                    ),                                          
# =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='查詢空檔',
                        text='請由下方選出您想要的時段！',
                        actions=[
                            MessageTemplateAction(
                                label='上午',
                                text='上午'
                            ),
                            MessageTemplateAction(
                                label='下午/全天',
                                text='下午/全天'
                            ),
                        ]
                    ),                                          
 # =============================================================================            
                     CarouselColumn(
                        # thumbnail_image_url='',
                        title='工作室地址',
                        text='請在下方選出您需要的！',
                        actions=[
                            MessageTemplateAction(
                                label='地址',
                                text='地址'
                            ),
                            MessageTemplateAction(
                                label='N/A',
                                text='N/A'
                            ),
                        ]
                    ),                       
                 ]            
            )
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0
    
###############################################################################
        #user_message='人像攝影'
    elif user_message.find('人像拍攝') != -1:         #判斷用戶使否傳來"人像拍攝"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='本訊息為【人像拍攝】',
            template=ConfirmTemplate(
                text='拍攝人數',
                actions=[
                    MessageTemplateAction(
                        label='單人',
                        text='單人'
                    ),
                    MessageTemplateAction(
                        label='雙人',
                        text='雙人'
                    )
                ]
            )
        )
              
        line_bot_api.reply_message(event.reply_token,res_message)
        
###############################################################################
      #user_message='商業拍攝'
    elif user_message.find('商業拍攝') != -1:         #判斷用戶使否傳來"商業拍攝"關鍵字，若為是則觸發本區段。 
        
        res_message = TextSendMessage(text='TWD 20000 UP')
                                      
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0  
    
###############################################################################
    elif user_message.find('單人') != -1 :         #判斷用戶使否傳來"單人"關鍵字，若為是則觸發本區段。  
        
        res_message = TextSendMessage(text='TWD 3500 UP')
                                      
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0  
    
###############################################################################
    elif user_message.find('雙人') != -1 :         #判斷用戶使否傳來"雙人"關鍵字，若為是則觸發本區段。  
        
        res_message = TextSendMessage(text='TWD 6000 UP')
                                      
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0  
    
###############################################################################
    elif user_message.find('上午') != -1 :         #判斷用戶使否傳來"上午"關鍵字，若為是則觸發本區段。  
        
        res_message = TextSendMessage(text='6月上午空檔 -- 6/1-12，13，18，21，30 ')
                                      
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0  
    
###############################################################################

    elif user_message.find('下午') != -1 :         #判斷用戶使否傳來"下午"關鍵字，若為是則觸發本區段。  
        
        res_message = TextSendMessage(text='6月下午空檔 -- 6/1-12，13，18，21，31 ')
        
    elif user_message.find('全天') != -1 :         #判斷用戶使否傳來"全"關鍵字，若為是則觸發本區段。 
        
        res_message = TextSendMessage(text='6月全天空檔 -- 6/1-12，13，18，21，31 ')
                                      
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0  
    
###############################################################################
      
# =============================================================================
    elif user_message.find('Instagram') != -1 :         #判斷用戶使否傳來"Instagram"關鍵字，若為是則觸發本區段。  
        
        res_message = TextSendMessage(text='https://www.instagram.com/uyunishino_')
                                      
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0  
# =============================================================================
    elif user_message.find('Porfolio') != -1 :         #判斷用戶使否傳來"Porfolio"關鍵字，若為是則觸發本區段。  
        
        res_message = TextSendMessage(text='https://www.uyunishino.work')
                                      
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0  
# =============================================================================
        #user_message='影片訊息'
    elif user_message.find('影片訊息') != -1:         #判斷用戶使否傳來"影片訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = VideoSendMessage(
            original_content_url='https://r5---sn-npoe7n7r.googlevideo.com/videoplayback?expire=1612879931&ei=20MiYIfkBIyWiwTEhrSQBQ&ip=144.202.56.145&id=o-ANCIwAp79OWJyLwTkkaRuKvMzGSf6gsljTB-wPAcLNh5&itag=22&source=youtube&requiressl=yes&vprv=1&mime=video%2Fmp4&ns=6LcWIDtZWbxjYUXS1Dod_vIF&ratebypass=yes&dur=328.423&lmt=1572331630804319&fvip=5&c=WEB&txp=2216222&n=fRjt_f_oTJeD95i&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAMXkWqUW9UIIMrcCJZ8dh_xZ7nWpUlNVWd4sdw2JHME4AiAKGxqLL5z6kL30RkfuW-mCUVIwWmqG1nPPOo0_PbecxA%3D%3D&redirect_counter=1&cm2rm=sn-vgqe7s76&req_id=3b1b213d3dba3ee&cms_redirect=yes&mh=ww&mip=182.234.79.223&mm=34&mn=sn-npoe7n7r&ms=ltu&mt=1612858827&mv=m&mvi=5&pl=18&lsparams=mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRAIgXT3f533nuXNJnQlehCh9ePDKFQtHpmkoWKAN1IzsJsgCIBtOmjBzv9DrdIWDtPjsHRSZXLCFcjAZN1zQSqWOHGEM',
            preview_image_url='https://lh3.googleusercontent.com/pw/ACtC-3fmvQXV2wh96fqQjSJ5KZXRUjprXHH9zG2EVFLuExV-Uxl1sN2AQ76RIN8Cy6A0COCT4FvQg9YRzqNujWkrxwA3kgGLcAOtsupqBi0JCqx4HUQuMqR8KMJ6CRQ7FBSJ3JLHfYv04V_BFmQAMFQIrWgvsg=w958-h539'
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='音訊訊息'
    elif user_message.find('音訊訊息') != -1:         #判斷用戶使否傳來"音訊訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = message = AudioSendMessage(
            original_content_url='https://r5---sn-npoe7n7r.googlevideo.com/videoplayback?expire=1612879931&ei=20MiYIfkBIyWiwTEhrSQBQ&ip=144.202.56.145&id=o-ANCIwAp79OWJyLwTkkaRuKvMzGSf6gsljTB-wPAcLNh5&itag=140&source=youtube&requiressl=yes&vprv=1&mime=audio%2Fmp4&ns=vL6EbYMqRar6wkILnGFdM6sF&gir=yes&clen=5315836&otfp=1&dur=328.423&lmt=1572331593044296&fvip=5&keepalive=yes&c=WEB&txp=2211222&n=jinyYfcO0NUsfzO&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cotfp%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAL1zzZOOX4qwpMs5f8cTrPvw7OLcoFlrx7IoNt4qKE_jAiA7W2Xce4BnGqfOPsuzNGEVGudGIMhqHBb5d40qsKMjdQ%3D%3D&ratebypass=yes&redirect_counter=1&cm2rm=sn-vgqe7s76&req_id=a0e283de1a31a3ee&cms_redirect=yes&mh=ww&mip=182.234.79.223&mm=34&mn=sn-npoe7n7r&ms=ltu&mt=1612858105&mv=m&mvi=5&pl=18&lsparams=mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIhANHX1USrlIJC8IXts4LcHkOClswgQoSKtfv-bBU76R7VAiB8SAfZxTgonssKfxUs6FL8O8Q5wn5cnL2r_OSUuKtjRQ%3D%3D',
            duration=328000
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='地址'
    elif user_message.find('地址') != -1:         #判斷用戶使否傳來"地址"關鍵字，若為是則觸發本區段。 
        
        res_message = LocationSendMessage(
            title='西野工作室',
            address='XX區鼓山區XX路',
            latitude=22.6632785,
            longitude=120.2987984
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   

###############################################################################
        #user_message='按鈕介面訊息'
    elif user_message.find('按鈕介面訊息') != -1:         #判斷用戶使否傳來"按鈕介面訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='按鈕介面訊息',
            template=ButtonsTemplate(
                thumbnail_image_url='https://imgs.gvm.com.tw/upload/gallery/20210126/77456_01.png',
                title='按鈕介面訊息',
                text='此種訊息可以設定1~4個按鈕選項，並可以設定一張1.51:1尺寸的圖片。',
                actions=[
                    MessageTemplateAction(
                        label='測試訊息',
                        text='您剛剛點擊了【測試訊息】'
                    ),
                    URITemplateAction(
                        label='文藻首頁',
                        uri='https://a001.wzu.edu.tw/'
                    )
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token,res_message)

        return 0
    
###############################################################################

        #user_message='確認介面訊息'
    elif user_message.find('確認介面訊息') != -1:         #判斷用戶使否傳來"確認介面訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='本訊息為【確認介面訊息】',
            template=ConfirmTemplate(
                text='您是否確認要離開本次對話？',
                actions=[
                    MessageTemplateAction(
                        label='是',
                        text='我要離開對話'
                    ),
                    MessageTemplateAction(
                        label='否',
                        text='圖文訊息'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)

        return 0
    
###############################################################################
    elif user_message.find('輪播圖') != -1:
        
        return 0
###############################################################################
    elif user_message.find('您剛剛點擊了') != -1:
        
        return 0
###############################################################################
    elif user_message.find('教材尚在開發中') != -1:
        
        return 0
###############################################################################
    elif user_message.find('我要離開對話') != -1:
        response='好的，期待您下次的呼喚，再見！'
        line_bot_api.reply_message(event.reply_token,TextSendMessage(response))
        
        return 0
###############################################################################
    else:
        response='我不太了解您的意思，建議您透過選單與我互動唷！'
        line_bot_api.reply_message(event.reply_token,TextSendMessage(response))
        return 0
        
    
    # user_id = event.source.user_id
    # print("user_id =", user_id)

    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text))



###############################################################################
import os

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 27017))
    app.run(host='0.0.0.0', port=port)
if __name__ == "__main__":
    app.run()
    
