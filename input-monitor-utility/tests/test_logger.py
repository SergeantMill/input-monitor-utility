"""Tests for the KeyLogger module."""
import os
import tempfile
import pytest
from input_monitor.logger import KeyLogger

class TestKeyLogger:
    def setup_method(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
        self.filename = self.temp_file.name
        self.temp_file.close()
        self.logger = KeyLogger(filename=self.filename)
    
    def teardown_method(self):
        if os.path.exists(self.filename):
            os.unlink(self.filename)
    
    def test_log_key_creates_file(self):
        assert os.path.exists(self.filename)
    
    def test_log_key_writes_content(self):
        self.logger.log_key("a")
        with open(self.filename, 'r') as f:
            content = f.read()
        assert "a" in content
    
    def test_log_special_writes_tag(self):
        self.logger.log_special("ENTER")
        with open(self.filename, 'r') as f:
            content = f.read()
        assert "<ENTER>" in content
    
    def test_multiple_logs(self):
        self.logger.log_key("h")
        self.logger.log_key("e")
        self.logger.log_key("l")
        with open(self.filename, 'r') as f:
            lines = f.readlines()
        # First line is header, next 3 are logs
        assert len(lines) >= 4
        assert any("h" in line for line in lines)
        assert any("e" in line for line in lines)
        assert any("l" in line for line in lines)