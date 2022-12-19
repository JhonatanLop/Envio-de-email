# Envio de email
Script em python que envia menságens por email.
> Status: Finalizado!

## Objetivo:<br>
Foi criado com o propósito de enviar senhas pré definidas à usuários que foram cadastrado em um sistema.

> Este código em específico foi desenvolvido com uma necessidade que surgiu em um projeto de faculdade, onde ao cadastrar um usuário dentro de uma aplicação, com o email fornecido pelo mesmo usuário, um email é enviado com uma senha auto-gerada.

## Como funciona?<br>
O código é bem simples.

> Ele é feito dentro de uma função (*usando o método "def funcao()"*), para que possa ser usado dentro de qualquer script python

> A seguir, importo as bibliotecas necessárias para que o código funcione.

> * *host*  - é o endereço do servidor que será acessádo </div>
> * *port*  - é a porta de acesso <br>
> * *login* - é o endereço de email de onde a mensagem vai ser enviada <br>
> * *password* - é a senha de máquina para que o computador acesse o email. <br>

## Possíveis problemas

Para que o código consiga se conectar com o endereço de email, é importante fazer algumas configurações antes.<br>
Habilitar acesso de apps menos seguras era uma delas até o google tirar esse recurso. agora o processo é um pouco diferente.<br>

> * Você deve entrar nas configurações do email e habilitar uma senha de máquina. (*existem alguns tutoriais no youtube de como fazer isso*)
> * Ao criar uma senha de máquina, ela deve atribuida à variável "password" ao invés da senha do email.

### Continuando...

* "server = smtplib.SMTP(host, port)"
> Cria uma conexão com o servidor, utilizando o endereço e a porta.

* "server.ehlo()" 
> É uma função que fornece um indereço de IP do servidor.

* "server.starttls()" 
> É uma função que inicializa uma segurança necessária que é requerida pelo Gmail pra poder fazer esse acesso, sem ela o Google entrende que seu código não é seguro e não irá permitir o acesso.

* "server.login(login, password)" 
> É resposável por "entrar" na sua conta de email com os parâmetros fornecidos anteriormente.

* No corpo, é escrito em formato HTML, o corpo de fato da mensagem a ser enviada para outra pessoa

> *Da linha 43 até 48, ocorre uma incriptação da mensagem o email em tipo MIME (**não necessita de alteração**)*

## Para quem vai ser enviado?

> Para configurar o destinatário da mensagem usamos "email_msg ['To'] = to" onde "to" em minusculo, estará o endereço de email do destinatário. <br>
> Após isso, ele envia o email com a função "serve.sendmail()" com os paramedros de onde o email vai ser enviado e do destinatário.

Na condição presente no final do código está uma verificação para que "@" esteja presente no email. É um indicativo de que ele é válido<br>

## Agradecimentos ✌️

> *Obrigado por acessar meu github e conhecer meu projeto. Caso queira enviar sugestões meu email e instagram estarão logo abaixo*
> <br>
>
>
> <a href = "mailto:jhooliveira.lopes@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a> <a href="https://www.instagram.com/jhonatan_lopes_lmao/?next=%2F" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank"></a> 
