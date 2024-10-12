from rest_framework import permissions


# Classe de permissão personalizada que define permissões com base no método HTTP e no modelo sendo acessado
class GlobalDefaultPermission(permissions.BasePermission):

    # Método principal que verifica se o usuário tem permissão para a requisição atual
    def has_permission(self, request, view):
        # Obtém o código de permissão específico baseado no método HTTP (GET, POST, etc.) e no modelo sendo acessado
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,  # O método HTTP da requisição (GET, POST, etc.)
            view=view,  # A view atual sendo acessada
        )

        # Se não houver um código de permissão correspondente, a permissão é negada
        if not model_permission_codename:
            return False

        # Verifica se o usuário tem a permissão correspondente no modelo
        return request.user.has_perm(model_permission_codename)

    # Método auxiliar para gerar o codename da permissão baseado no método e no modelo
    def __get_model_permission_codename(self, method, view):
        try:
            # Obtém o nome do modelo e do app a partir da queryset definida na view
            model_name = view.queryset.model._meta.model_name  # Nome do modelo (ex: 'car')
            app_name = view.queryset.model._meta.app_label  # Nome do app ao qual o modelo pertence (ex: 'cars')

            # Obtém o sufixo da ação (view, add, change, delete) com base no método HTTP
            action = self.__get_action_sufux(method)

            # Retorna o código de permissão no formato "app_name.action_model_name" (ex: 'cars.view_car')
            return f'{app_name}.{action}_{model_name}'

        except AttributeError:
            # Se ocorrer um erro (por exemplo, a view não tiver um queryset), retorna None
            return None

    # Método auxiliar para mapear o método HTTP para a ação correspondente
    def __get_action_sufux(self, method):
        # Dicionário que mapeia os métodos HTTP para as ações de permissão do Django
        method_actions = {
            'GET': 'view',       # 'GET' é mapeado para a ação de 'visualizar'
            'POST': 'add',       # 'POST' é mapeado para a ação de 'adicionar'
            'PUT': 'change',     # 'PUT' é mapeado para a ação de 'alterar'
            'PATCH': 'change',   # 'PATCH' também é mapeado para 'alterar'
            'DELETE': 'delete',  # 'DELETE' é mapeado para 'deletar'
            'OPTIONS': 'view',   # 'OPTIONS' é mapeado para 'visualizar'
            'HEAD': 'view',      # 'HEAD' é mapeado para 'visualizar'
        }

        # Retorna a ação correspondente ao método HTTP; se o método não estiver no dicionário, retorna uma string vazia
        return method_actions.get(method, '')
