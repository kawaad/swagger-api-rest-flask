# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cliente import Cliente  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClienteController(BaseTestCase):
    """ClienteController integration test stubs"""

    def test_cadastra_cliente(self):
        """Test case for cadastra_cliente

        Cadastra Cliente
        """
        cliente_ = Cliente()
        response = self.client.open(
            '/bytebank-api/v1/cliente',
            method='POST',
            data=json.dumps(cliente_),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
