import csv  # Biblioteca do Python para ler arquivos CSV
from django.core.management.base import BaseCommand  # Classe base para criar comandos personalizados
from actors.models import Actor  # Importa o modelo Actor, onde os dados serão salvos
from datetime import datetime


# Define o comando customizado
class Command(BaseCommand):
    # Texto de ajuda que será exibido quando o usuário rodar o comando com --help
    help = 'Importa um arquivo CSV com informações de atores'

    # Função para adicionar argumentos ao comando
    # Neste caso, estamos adicionando o argumento 'csv_file', que é o caminho para o arquivo CSV
    def add_arguments(self, parser):
        parser.add_argument(
            'csv_file',
            type=str,
            help='Caminho para o arquivo CSV'
        )

    # Função principal que será executada quando o comando for rodado
    def handle(self, *args, **kwargs):
        # Pega o caminho do arquivo CSV passado pelo usuário ao rodar o comando
        csv_file = kwargs['csv_file']

        try:
            # Abre o arquivo CSV em modo de leitura ('r') com a codificação 'utf-8'
            with open(csv_file, mode='r', encoding='utf-8') as file:
                # Usa o DictReader do CSV para ler o arquivo e mapeia cada linha para um dicionário
                reader = csv.DictReader(file)

                # Itera sobre cada linha (que é um dicionário) do arquivo CSV
                for row in reader:
                    # Pega os valores do dicionário de acordo com as chaves (colunas do CSV)
                    name = row['name']  # Coluna 'name' no CSV
                    birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()  # Coluna 'birthday' no CSV
                    nationality = row['nationality']  # Coluna 'nationality' no CSV

                    # Imprimir os nomes de cada atores
                    self.stdout.write(self.style.NOTICE(name))

                    # Cria um novo objeto Actor no banco de dados com os dados lidos do CSV
                    Actor.objects.create(name=name, birthday=birthday, nationality=nationality)

                # Exibe uma mensagem de sucesso no terminal ao final da operação
                self.stdout.write(self.style.SUCCESS('Dados importados com sucesso!'))

        # Caso haja algum erro ao abrir ou ler o arquivo, ou ao salvar no banco de dados
        except Exception as e:
            # Exibe uma mensagem de erro no terminal
            self.stdout.write(self.style.ERROR(f'Erro ao processar o arquivo CSV: {e}'))
