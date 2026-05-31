"""Tests for the KeyHandler module (mock-based)."""
from unittest.mock import Mock, patch
import pytest
from input_monitor.handler import KeyHandler
from pynput.keyboard import Key

class TestKeyHandler:
    def setup_method(self):
        self.mock_logger = Mock()
        self.handler = KeyHandler(logger=self.mock_logger)
    
    def test_on_press_regular_key(self):
        mock_key = Mock()
        mock_key.char = 'a'
        result = self.handler.on_press(mock_key)
        self.mock_logger.log_key.assert_called_once_with('a')
        assert result is True
    
    def test_on_press_special_key(self):
        mock_key = Key.enter
        result = self.handler.on_press(mock_key)
        self.mock_logger.log_special.assert_called_once_with('ENTER')
        assert result is True
    
    def test_on_press_esc_stops(self):
        mock_key = Key.esc
        result = self.handler.on_press(mock_key)
        self.mock_logger.log_special.assert_called_once_with('ESC')
        assert result is False
    
    def test_on_press_error_handled(self):
        self.mock_logger.log_key.side_effect = Exception("Test error")
        mock_key = Mock()
        mock_key.char = 'x'
        result = self.handler.on_press(mock_key)  # Should not raise
        assert result is True