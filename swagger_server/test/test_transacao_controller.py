# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.transacao import Transacao  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTransacaoController(BaseTestCase):
    """TransacaoController integration test stubs"""

    def test_altera_valor_transacao(self):
        """Test case for altera_valor_transacao

        Altera o valor da Transação
        """
        query_string = [('valor', 1.2)]
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/bytebank-api/v1/transacao/{codigo}'.format(codigo=789),
            method='PUT',
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cadastra_transacao(self):
        """Test case for cadastra_transacao

        Cadastra Transação na Conta
        """
        transacao = Transacao()
        query_string = [('tipo', 'tipo_example')]
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/bytebank-api/v1/transacao',
            method='POST',
            data=json.dumps(transacao),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_exclui_transacao(self):
        """Test case for exclui_transacao

        Exclui a Transação
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/bytebank-api/v1/transacao/{codigo}'.format(codigo=789),
            method='DELETE',
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
