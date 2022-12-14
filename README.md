# Projeto flightdashboard

Este projeto tem como objetivo a criação de um sistema integrado de controle de voos para um aeroporto. Tem como principais features o CRUD, que permite o cadastro, leitura, deleção e atualização de voos no sistema e a geração de relatório de voos. 

A linguagem de programação usada é o Python, com a framework Django.

**Diagrama de Entidade e Relacionamento:**

![This is an image](https://i.imgur.com/kcgnGWB.png)[

**Diagrama de Navegação no Sistema:**

![This is an image](https://i.imgur.com/UH5zzUy.png)

## Nome do Grupo: BCJ

**Integrantes:** 

Breno Suguru Costa Tominaga - NUSP: 11804320

Caio Amaral Gurgel Xavier - NUSP: 11804293

Johan Su Kwok - NUSP: 10770176

## Pré-requisitos:
[Python 3.6+](https://www.python.org/downloads/)


## Roteiro de Execução do Projeto

1. Clone o repositório a alguma pasta local.

    ```
    C:\...\MinhaPastaLocal> git clone https://github.com/Brenovyski/projeto_PCS3643_FD
    ```

2. É recomendado criar um ambiente virtual usando `venv` utilizando o python (a depender do seu sistema operacional). Para isso, use o comando:

    ```
    C:\...\MinhaPastaLocal> cd projeto_PCS3643_FD
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD> python -m venv env
    ```

3. Depois, e ative o ambiente usando o comando no Powershell do Windows:

    ```
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD> .\env\bin\Activate.ps1
    ```
    se não funcionar, tente trocar a pasta `bin` por `Scripts`:
    ```
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD> .\env\Scripts\Activate.ps1
    ```

4. Instale os requerimentos do projeto:

    ```
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD> pip install -r requirements.txt
    ```

5. Faça as migrações do Django:

    ```
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD> cd flightdashboard
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD\flightdashboard> python manage.py makemigrations
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD\flightdashboard> python manage.py makemigrations sys_voos
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD\flightdashboard> python manage.py migrate
    ```
6. Execute os testes:

    ```
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD\flightdashboard> python manage.py test
    ```

7. Crie os usuários padrão para o uso do sistema (logins pré-definidos):

    ```
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD\flightdashboard> python manage.py createsuperuser
    ```

    Rode esse comando 3 vezes para criar 3 credenciais diferentes conforme o seguinte padrão:

    | Username      | Email address              | Password    |
    |---------------|----------------------------|-------------|
    | operador      | oper@flightdashboard.com   | 1234        |
    | funcionario   | func@flightdashboard.com   | 1234        |
    | torre         | torre@flightdashboard.com  | 1234        |
    | piloto        | piloto@flightdashboard.com | 1234        |
    | gerente       | geren@flightdashboard.com  | 1234        |

   Para fins de desenvolvimento, pode-se também criar um login no molde abaixo:

    | Username      | Email address             | Password    |
    |---------------|---------------------------|-------------|
    | Desenvolvedor | dev@flightdashboard.com   | dev         | 
    

8. Para rodar o projeto, use os comandos:

    ```
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD\flightdashboard>python manage.py runserver
    ```


9. Finalmente, para executar os sistema, acessamos o link:

    http://localhost:8000/



## Observações

1. O sistema comporta as seguintes companhias aéreas pré-determinadas:
    | Companhia | Código | 
    |-----------|--------|
    | Azul      | AZ     |
    | Gol       | GO     |
    | Latam     | LA     |
    | Lufthansa | LF     |
    | Emirates  | EM     |

    O sistema não permite criar um voo com uma companhia aérea inexistente. Para criar companhias aéreas, acesse o admin do Django (http://localhost:8000/admin/) e logue com a crendencial. Clique em "Companhia aereas" na tabela "SYS_VOOS" e crie um novo objeto.

2. O sistema de login funciona com os aplicativos padrão do Django para a autenticação.
   O bloqueio de contas seguindo 3 tentativas de login por usuário funciona com a aplicação `axes` e tem algumas funcionalidades:

   Para limpar o histórico de tentativas de login de todos os usuários rode o seguinte comando:
   ```
   python manage.py axes_reset
   ```

   Para limpar o histórico de tentativas de login de apenas alguns usuários rode o seguinte comando:
   ```
   python manage.py axes_reset_username [username ...]
   ```

   Para mais informações, segue a documentação: 
   <https://django-axes.readthedocs.io/en/latest/3_usage.html#resetting-attempts-and-lockouts>

3. Para acessar o site, foi usado o PythonAnywhere para hospedar o sistema de voo, acessado no seguinte link: https://flightdashboard.pythonanywhere.com
