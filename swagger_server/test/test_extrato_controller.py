# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.extrato import Extrato  # noqa: E501
from swagger_server.test import BaseTestCase


class TestExtratoController(BaseTestCase):
    """ExtratoController integration test stubs"""

    def test_consulta_extrato(self):
        """Test case for consulta_extrato

        Consulta Extrato
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/bytebank-api/v1/extrato/{agencia}/{numero}/{digito}'.format(agencia=56, numero=789, digito=56),
            method='GET',
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
