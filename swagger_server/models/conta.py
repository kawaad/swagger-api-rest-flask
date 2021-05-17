# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Conta(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, agencia: int=None, numero: int=None, digito: int=None, saldo: float=None, cliente: Cliente=None, transacoes: List[Transacao]=None):  # noqa: E501
        """Conta - a model defined in Swagger

        :param agencia: The agencia of this Conta.  # noqa: E501
        :type agencia: int
        :param numero: The numero of this Conta.  # noqa: E501
        :type numero: int
        :param digito: The digito of this Conta.  # noqa: E501
        :type digito: int
        :param saldo: The saldo of this Conta.  # noqa: E501
        :type saldo: float
        :param cliente: The cliente of this Conta.  # noqa: E501
        :type cliente: Cliente
        :param transacoes: The transacoes of this Conta.  # noqa: E501
        :type transacoes: List[Transacao]
        """
        self.swagger_types = {
            'agencia': int,
            'numero': int,
            'digito': int,
            'saldo': float,
            'cliente': Cliente,
            'transacoes': List[Transacao]
        }

        self.attribute_map = {
            'agencia': 'agencia',
            'numero': 'numero',
            'digito': 'digito',
            'saldo': 'saldo',
            'cliente': 'cliente',
            'transacoes': 'transacoes'
        }

        self._agencia = agencia
        self._numero = numero
        self._digito = digito
        self._saldo = saldo
        self._cliente = cliente
        self._transacoes = transacoes

    @classmethod
    def from_dict(cls, dikt) -> 'Conta':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Conta of this Conta.  # noqa: E501
        :rtype: Conta
        """
        return util.deserialize_model(dikt, cls)

    @property
    def agencia(self) -> int:
        """Gets the agencia of this Conta.


        :return: The agencia of this Conta.
        :rtype: int
        """
        return self._agencia

    @agencia.setter
    def agencia(self, agencia: int):
        """Sets the agencia of this Conta.


        :param agencia: The agencia of this Conta.
        :type agencia: int
        """

        self._agencia = agencia

    @property
    def numero(self) -> int:
        """Gets the numero of this Conta.


        :return: The numero of this Conta.
        :rtype: int
        """
        return self._numero

    @numero.setter
    def numero(self, numero: int):
        """Sets the numero of this Conta.


        :param numero: The numero of this Conta.
        :type numero: int
        """

        self._numero = numero

    @property
    def digito(self) -> int:
        """Gets the digito of this Conta.


        :return: The digito of this Conta.
        :rtype: int
        """
        return self._digito

    @digito.setter
    def digito(self, digito: int):
        """Sets the digito of this Conta.


        :param digito: The digito of this Conta.
        :type digito: int
        """

        self._digito = digito

    @property
    def saldo(self) -> float:
        """Gets the saldo of this Conta.


        :return: The saldo of this Conta.
        :rtype: float
        """
        return self._saldo

    @saldo.setter
    def saldo(self, saldo: float):
        """Sets the saldo of this Conta.


        :param saldo: The saldo of this Conta.
        :type saldo: float
        """

        self._saldo = saldo

    @property
    def cliente(self) -> Cliente:
        """Gets the cliente of this Conta.


        :return: The cliente of this Conta.
        :rtype: Cliente
        """
        return self._cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        """Sets the cliente of this Conta.


        :param cliente: The cliente of this Conta.
        :type cliente: Cliente
        """

        self._cliente = cliente

    @property
    def transacoes(self) -> List[Transacao]:
        """Gets the transacoes of this Conta.


        :return: The transacoes of this Conta.
        :rtype: List[Transacao]
        """
        return self._transacoes

    @transacoes.setter
    def transacoes(self, transacoes: List[Transacao]):
        """Sets the transacoes of this Conta.


        :param transacoes: The transacoes of this Conta.
        :type transacoes: List[Transacao]
        """

        self._transacoes = transacoes