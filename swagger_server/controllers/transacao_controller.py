import connexion
import six

from swagger_server.models.transacao import Transacao  # noqa: E501
from swagger_server import util


def altera_valor_transacao(codigo, valor, Authorization):  # noqa: E501
    """Altera o valor da Transação

    Altera o valor da transação existente na conta do cliente. # noqa: E501

    :param codigo: 
    :type codigo: int
    :param valor: 
    :type valor: float
    :param Authorization: 
    :type Authorization: str

    :rtype: None
    """
    return 'do some magic!'


def cadastra_transacao(Authorization, transacao, tipo):  # noqa: E501
    """Cadastra Transação na Conta

    Cadastra uma transação de débito ou deposito na conta. # noqa: E501

    :param Authorization: 
    :type Authorization: str
    :param transacao: 
    :type transacao: dict | bytes
    :param tipo: 
    :type tipo: str

    :rtype: Transacao
    """
    if connexion.request.is_json:
        transacao = Transacao.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def exclui_transacao(codigo, Authorization):  # noqa: E501
    """Exclui a Transação

    Exclusão da transação existente na conta do cliente # noqa: E501

    :param codigo: 
    :type codigo: int
    :param Authorization: 
    :type Authorization: str

    :rtype: None
    """
    return 'do some magic!'
