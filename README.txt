Documentação da API de Faturamento de Chamadas

Descrição do Projeto

A API de Chamadas é uma aplicação web baseada em Django projetada para gerenciar e calcular registros de chamadas telefônicas. A API processa registros de chamadas para gerar informações de faturamento com base em regras específicas, incluindo duração da chamada, períodos de tarifa padrão ou reduzida e taxas aplicáveis. Este projeto permite que os usuários armazenem, recuperem e gerenciem registros de chamadas, além de fornecer um endpoint para calcular o faturamento com base nos registros fornecidos.

Tabela de Conteúdos

Funcionalidades
Requisitos
Instalação
Executando o Projeto
Testando o Projeto

Registro de Chamadas: Armazena registros de chamadas com horários de início e fim, IDs de chamadas, números de origem e destino.
Cálculo de Faturamento: Gera informações de faturamento com base na duração da chamada, horário e períodos de tarifa.
Validação: Aplica regras específicas para números de telefone, timestamps e identificadores únicos de chamada.
Requisitos

Python: Versão >= 3.9
Django: Versão >= 3.2
Django REST Framework: Versão >= 3.12
Railway: Para deploy e hospedagem (opcional)
Instalação

Para configurar e executar este projeto localmente, siga os passos abaixo:

1. Clone o Repositório
cd chamadas-api

2. Crie um Ambiente Virtual
Crie um ambiente virtual para isolar as dependências.
python3 -m venv env
source env/bin/activate  # No Windows use `env\Scripts\activate`

3. Instale as Dependências
Instale todos os pacotes Python necessários a partir do arquivo requirements.txt.
pip install -r requirements.txt

4. Configure o Banco de Dados
Este projeto usa um banco de dados SQLite por padrão. No entanto, se preferir usar PostgreSQL ou outro banco de dados, configure-o no arquivo settings.py na seção DATABASES.

5. Execute as Migrações
Aplique as migrações para configurar o esquema do banco de dados.
python manage.py migrate

6. Crie um Superusuário
Crie um usuário administrador para acessar a interface de administração do Django.
python manage.py createsuperuser

7. Execute o Servidor de Desenvolvimento
Inicie o servidor para garantir que tudo esteja configurado corretamente.
python manage.py runserver
Acesse a aplicação em http://127.0.0.1:8000.

Executando o Projeto

Usando Railway para Deploy
Railway fornece uma maneira prática de fazer deploy de aplicações Django. Para fazer deploy deste projeto no Railway, siga estes passos:

Instale o Railway CLI: Instale o Railway CLI seguindo as instruções no site do Railway.
Inicie o Projeto no Railway: Dentro do diretório do seu projeto, execute:
railway init

Adicione Variáveis de Ambiente: Configure as variáveis de ambiente necessárias para seu banco de dados e chaves secretas no Railway.

Faça o Deploy: Realize o deploy do projeto no Railway.
railway up

Testando o Projeto

Executando Testes
Para executar os testes unitários do projeto, use o comando abaixo:
python manage.py test

Esse comando executará todos os casos de teste do projeto para garantir que cada funcionalidade esteja funcionando conforme o esperado.
