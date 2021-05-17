import connexion
import six

from swagger_server.models.extrato import Extrato  # noqa: E501
from swagger_server import util


def consulta_extrato(agencia, numero, digito, Authorization):  # noqa: E501
    """Consulta Extrato

    Consulta o extrato da conta do cliente # noqa: E501

    :param agencia: 
    :type agencia: int
    :param numero: 
    :type numero: int
    :param digito: 
    :type digito: int
    :param Authorization: 
    :type Authorization: str

    :rtype: Extrato
    """
    return 'do some magic!'
