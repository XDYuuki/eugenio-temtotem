import boto3
import csv
import cv2
import time
import requests
import json

def send_to_eugenio(dados):
    cabecalho = {"Content-Type": "application/json", "apikey": "reAdE9upscITtZVz6tonDs2s09NHZ7ex", "X-Schema": "temtotem_data"}
    data_to_send = json.dumps(dados)

    try:
        requisicao = requests.post('https://portal.stg.eugenio.io/api/v1/data',
                                   headers=cabecalho,
                                   data=data_to_send)
        print(requisicao.status_code)
        print(requisicao.text)

    except Exception as erro:
        print('Requisição deu erro', erro)

def select_emotion(Emotions):
    for item in Emotions:
        if item['Confidence'] > 50:
            return(item['Type'])


def parse_response(img_analise):

    data_to_send = {
	"agerange": "",
	"beard": bool,
	"emotions": "",
	"eyeglasses": bool,
	"eyeopen": bool,
	"gender": "",
	"mouthopen": bool,
	"mustache": bool,
	"smile": bool,
	"sunglasses": bool
}

    conteudo1 = img_analise['FaceDetails']
    conteudo2   = conteudo1[0]

    AgeRange    = conteudo2['AgeRange']
    Beard       = conteudo2['Beard']
    Emotions    = conteudo2['Emotions']
    Eyeglasses  = conteudo2['Eyeglasses']
    EyesOpen    = conteudo2['EyesOpen']
    Gender      = conteudo2['Gender']
    MouthOpen   = conteudo2['MouthOpen']
    Mustache    = conteudo2['Mustache']
    Smile       = conteudo2['Smile']
    Sunglasses  = conteudo2['Sunglasses']

    data_to_send['agerange']    = str(AgeRange['Low'])+'-'+str(AgeRange['High'])
    data_to_send['beard']       = Beard['Value']
    data_to_send['emotions']    = select_emotion(Emotions)
    data_to_send['eyeglasses']  = Eyeglasses['Value']
    data_to_send['eyeopen']     = EyesOpen['Value']
    data_to_send['gender']      = Gender['Value']
    data_to_send['mouthopen']   = MouthOpen['Value']
    data_to_send['mustache']    = Mustache['Value']
    data_to_send['smile']       = Smile['Value']
    data_to_send['sunglasses']  = Sunglasses['Value']


    return data_to_send
    #print(data_to_send)

def detect_faces(source_bytes):
    # with open(
    #         'user_credentials/new_user_credentials.csv', 'r'
    # ) as input_csv:
    #     next(input_csv)
    #     reader = csv.reader(input_csv)
    #     for line in reader:
    #         access_key_id = line[2]
    #         secret_access_key = line[3]

    access_key_id = 'AKIA5EOQICHBCFCVXLXA'
    secret_access_key = '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'

    try:
        client = boto3.client('rekognition', 'us-east-1',
                              aws_access_key_id=access_key_id,
                              aws_secret_access_key=secret_access_key)
    except:
        print('Client set error')

    try:
        response = client.detect_faces(Image={'Bytes': source_bytes}, Attributes=['ALL'])
    except:

        print('Client set error')

    #print('raw data', response)

    eugenio_post_data = parse_response(response)

    send_to_eugenio(eugenio_post_data) #sending to eugenio


def main():
    cap = cv2.VideoCapture(0)

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        cv2.imwrite('frame.jpg', frame)

        photo = 'frame.jpg'
        with open(photo, 'rb') as source_image:
            source_bytes = source_image.read()

        # print(source_bytes)
        detect_faces(source_bytes)

        # Display the resulting frame
        cv2.imshow('frame', frame)

        time.sleep(10)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
