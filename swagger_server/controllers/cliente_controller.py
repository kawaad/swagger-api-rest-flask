import connexion
import six

from swagger_server.models.cliente import Cliente  # noqa: E501
from swagger_server import util


def cadastra_cliente(cliente_=None):  # noqa: E501
    """Cadastra Cliente

    Cadastra um novo cliente # noqa: E501

    :param cliente_: 
    :type cliente_: dict | bytes

    :rtype: Cliente
    """
    if connexion.request.is_json:
        cliente_ = Cliente.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
