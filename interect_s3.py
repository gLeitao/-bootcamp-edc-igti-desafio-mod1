import boto3
import os 

#criar um cliente para interagir com aws s3
s3_cliente = boto3.client('s3')

pasta = './dados'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        print(os.path.join(diretorio, arquivo))
        s3_cliente.upload_file(os.path.join(diretorio, arquivo), 'datalake-geovani-igti-edc-desafio-mod1-tf', f'raw/{arquivo}')
