#!/usr/bin/python3
"""Unittest for File_storage"""

import unittest
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Crear una instancia de FileStorage antes de cada prueba
        self.storage = FileStorage()

    def test_all_method(self):
        """Test if all() method returns __objects dictionary"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_method(self):
        """Test if new() method adds an object to __objects dictionary"""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", self.storage.all())

    @patch('builtins.open', create=True)
    def test_save_method(self, mock_open):
        """Test if save() method serializes __objects to a json file"""
        # Configurar el valor de retorno de write()
        mock_file = mock_open.return_value
        # Llamar al método save()
        self.storage.save()
        # Verificar si write() fue llamado correctamente
        mock_file.write.assert_called_once()

    @patch('builtins.open', create=True)
    def test_reload_method(self, mock_open):
        """Test if reload() method deserializes a json file"""
        # Configurar el valor de retorno de read()
        mock_file = mock_open.return_value
        mock_file.read.return_value = '{"BaseModel.1234567890": {"id": "1234567890", "name": "Test"}}'
        # Llamar al método reload()
        self.storage.reload()
        # Verificar si el objeto se carga correctamente en __objects
        self.assertIn('BaseModel.1234567890', self.storage.all())

if __name__ == '__main__':
    unittest.main()
