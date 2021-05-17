# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestContaController(BaseTestCase):
    """ContaController integration test stubs"""

    def test_consulta_saldo(self):
        """Test case for consulta_saldo

        Consulta Saldo
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/bytebank-api/v1/conta{agencia}/{numero}/{digito}/saldo'.format(agencia=56, numero=789, digito=56),
            method='GET',
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
