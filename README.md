# Envio-de-email
Programa para envio de email

# OBJETIVO:
Foi criado com o propósito de enviar senhas pré definidas à usuários que foram cadastrado em um sistema.

Este código em específico foi desenvolvido com uma necessidade que surgiu em um projeto de faculdade. onde um instrutor irá cadastrar várias pessoas com senhas autogeradas e com um email fornecido pelo usuário. 

Com o email fornecido, a senha criada, o código tem a função de informar ao futuro usuário da palaforma os seus dados para login.

# COMO FUNCIONA?
O código é bem simples.
De início, crio ele com uma função usando o método "def funcao()" para que posa ser importado e usado em um sistema mais complexo.

A seguir, importo as bibliotecas necessárias para que o código funcione, junto com uma que me conecte com o servidor.

Da linha 13 à 16, estou declarando valores que serão usado para me conectar à um servidor e uma conta de email que será usada para o envio. è importante que o email e a senha estejam corretos ou o código não irá funcionar.

host - é o endereço do servidor que será acessádo
port - é a porta de acesso
login - é o endereço de email de onde a mensagem vai ser enviada
password - é a senha de máquina para que o computador acesse o email.

### Possíveis problemas
Para que o código consiga se conectar com o endereço de email, é importante fazer algumas configurações antes. 
Habilitar acesso de apps menos seguras era uma delas até o google tirar esse recurso. agora o processo é um pouco diferente. Você deve entrar nas configurações do email e habilitar uma senha de máquina. Ao criar uma senha de máquina, ela deve atribuida à variável "password" ao invés da senha do email.

#### Continuando...

"server = smtplib.SMTP(host, port)" cria uma conexão com o servidor, utilizando o endereço e a porta.

"server.ehlo()" é uma função que fornece um indereço de IP do servidor.

"server.starttls()" é uma função que inicializa uma segurança necessária que é requerida pelo Gmail pra poder fazer esse acesso, sem ela o Google entrende que seu código não é seguro e não irá permitir o acesso.

"server.login(login, password)" é resposável por "entrar" na sua conta de email com os parâmetros fornecidos anteriormente.

No corpo, é escrito em formato HTML oque você deseja mandar para outra pessoa

Da linha 43 até 48, ocorre uma incriptação da mensagem o email em tipo MIME

### para quem vai ser enviado?

Para configurar o destinatário da mensagem usamos "email_msg ['To'] = to" onde "to" em minusculo, estará o endereço de email do destinatário.

Após isso, ele envia o email com a função "serve.sendmail()" com os paramedros de onde a mensagem irá  partir e para quem ela vai.

Na condição presente no final do código, está uma verificação, caso o objeto @ esteja presente no email, é um indicativo de que ele é válido, mas isso nem sempre. Caso ele tenha @ no endereço do destinatário, uma menságem será fornecida de que o email foi enviado. Caso não tiver, apontará que o email fornecido está incorreto