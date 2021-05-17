import connexion
import six

from swagger_server import util


def consulta_saldo(agencia, numero, digito, Authorization):  # noqa: E501
    """Consulta Saldo

    Consulta o saldo da conta do cliente. # noqa: E501

    :param agencia: 
    :type agencia: int
    :param numero: 
    :type numero: int
    :param digito: 
    :type digito: int
    :param Authorization: 
    :type Authorization: str

    :rtype: float
    """
    return 'do some magic!'
