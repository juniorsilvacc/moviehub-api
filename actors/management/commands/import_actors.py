import csv  # Biblioteca do Python para ler arquivos CSV
from django.core.management.base import BaseCommand  # Classe base para criar comandos personalizados
from actors.models import Actor  # Importa o modelo Actor, onde os dados serão salvos
from datetime import datetime
from actors.exceptions.csv_format_error import CSVFormatError
from django.db import transaction


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

                # Inicia uma transação atômica
                with transaction.atomic(): 
                    # Itera sobre cada linha (que é um dicionário) do arquivo CSV
                    for row in reader:
                        # Pega os valores do dicionário de acordo com as chaves (colunas do CSV)

                        name = row['name']  # Coluna 'name' no CSV
                        birthday = row['birthday']  # Coluna 'name' no CSV
                        nationality = row['nationality']  # Coluna 'name' no CSV

                        # Validação dos campos
                        if not name or not birthday or not nationality:
                            raise CSVFormatError(f'Erro de formato na linha: {row}') # Linha com erro

                        try:
                            birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()  # Converte a data
                        except ValueError:
                            raise CSVFormatError(f'Data de aniversário inválida no formato: {row["birthday"]}') # Linha com erro de data

                        # Imprimir os nomes de cada atores
                        self.stdout.write(self.style.NOTICE(name))

                        # Cria um novo objeto Actor no banco de dados com os dados lidos do CSV
                        Actor.objects.create(name=name, birthday=birthday, nationality=nationality)

                    # Exibe uma mensagem de sucesso no terminal ao final da operação
                    self.stdout.write(self.style.SUCCESS(f'Dados importados com sucesso! Total de atores: {Actor.objects.count()}'))

        # Caso haja algum erro ao abrir ou ler o arquivo, ou ao salvar no banco de dados
        except CSVFormatError as e: # Except personalizada
            self.stdout.write(self.style.ERROR(f'Erro: Formato de CSV - {e}'))
            raise
        except FileNotFoundError as e: # Except personalizada padrão
            self.stdout.write(self.style.ERROR(f"Erro: O arquivo não foi encontrado - {e}"))
        except Exception as e: # Except genérica
            self.stdout.write(self.style.ERROR(f'Erro: Ao processar o arquivo CSV - {e}'))
