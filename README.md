# Reconhecimento de Expressões faciais

Aplicação que, a partir de uma webcam, reconhece as emoções de uma pessoa fora outros dados como faixa etária, genero e etc.

## Iniciando

**Para começar você precisa de uma conta AWS e criar um user no console da aws : [AWS Console](https://console.aws.amazon.com/)
Não se preocupe, a conta pede um cartão de crédito, mas a aplicação não fará nenhuma cobrançã.**

![](readme_assets/create_user.png)

**Assossie as seguintes permissões**

![](readme_assets/permissions.png)

**Crie uma chave de acesso:**

![](readme_assets/access_key.png)

**Salve como CSV e coloque este arquivo na pasta user_credentials do projeto com o nome new_user_credentials.csv: (user_credentials/new_user_credentials.csv)**


![](readme_assets/access_key_csv.png)

### Pre-requisitos

Instale Python3, Pip3, Node.Js, Yarn e AWS CLI em seu ambiente.

### Instalando

Clone este rerpositório para sua máquina:
```
git clone https://github.com/XDYuuki/temtotem.git
```

Rode este comando para instalar as dependências: 

```
pip install -r requirements.txt
```

Certifique-se de que tem uma webcam conectada e rode este comando para rodar o programa:

```
python main.py
```

## Desenvolvido com

* [Python](https://www.python.org/) - Base de desenvolvimento
* [AWS Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/getting-started.html) - API's para reconhecimento de imagens

## Autores


## Para rodar o front-end

navegue até a pasta dee fronted

```
cd temtotem-frontend
```

rode a aplicação:

```
yarn start
```

* **Time 18**
