import unittest
import src.events as events


class TestEventsInitialization(unittest.TestCase):
    def test_init_status_event(self):
        mock_post_form = {'id': 'unique_id2', 'from': 'operator1', 'site_id': '123', 'type': 'status',
                          'data_status': 'online', 'timestamp': 1429026448}
        result = events.PostEvent(mock_post_form)
        self.assertEqual(result.data_status, 'online')
        with self.assertRaises(AttributeError):
            result.data_message
        
    def test_build_message_event(self):
        mock_post_form = {'id': 'unique_id1', 'from': 'visitor5', 'type': 'message', 'site_id': '123',  
                          'data_message': 'Hello', 'timestamp': 1429026445}
        result = events.PostEvent(mock_post_form)
        self.assertEqual(result.data_message, 'Hello')
        with self.assertRaises(AttributeError):
            result.data_status
