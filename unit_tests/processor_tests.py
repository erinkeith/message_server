import unittest
import src.events as events
import src.processor as processor
import src.sites as sites


class TestProcessor(unittest.TestCase):
    def test_process_online_status_message(self):
        mock_post_form = {'id': 'unique_id2', 'from': 'operator1', 'site_id': '123', 'type': 'status',
                          'data_status': 'online', 'timestamp': 1429026448}

        event = events.PostEvent(mock_post_form)
        our_sites = sites.Sites()
        messages = []
        processor.process_event(event, our_sites, messages)

        test_site = our_sites.get_site(event.msg_site_id)
        self.assertTrue(test_site.online)
        self.assertEqual(test_site.num_operators(), 1)
        self.assertEqual(len(messages), 1)

    def test_process_offline_status_message(self):
        mock_post_form = {'id': 'unique_id2', 'from': 'operator1', 'site_id': '123', 'type': 'status',
                          'data_status': 'offline', 'timestamp': 1429026448}

        event = events.PostEvent(mock_post_form)
        our_sites = sites.Sites()
        messages = []
        processor.process_event(event, our_sites, messages)

        test_site = our_sites.get_site(event.msg_site_id)
        self.assertFalse(test_site.online)
        self.assertEqual(test_site.num_operators(), 1)
        self.assertEqual(len(messages), 1)

    def test_process_dup_message(self):
        mock_post_form = {'id': 'unique_id2', 'from': 'operator1', 'site_id': '123', 'type': 'status',
                          'data_status': 'offline', 'timestamp': 1429026448}

        event = events.PostEvent(mock_post_form)
        our_sites = sites.Sites()
        messages = []
        processor.process_event(event, our_sites, messages)
        processor.process_event(event, our_sites, messages)

        test_site = our_sites.get_site(event.msg_site_id)
        self.assertFalse(test_site.online)
        self.assertEqual(test_site.num_operators(), 1)
        self.assertEqual(len(messages), 1)

    def test_save_stats(self):
        tests_sites = sites.Sites()
        tests_sites.add_site('123')

        processor.save_stats(tests_sites)

    def test_build_json_string(self):
        test_sites = sites.Sites()
        test_sites.add_site('456')
        test_sites.add_site('123')

        expected_string = '[{"site_id": 123, "messages": 0, "emails": 0, "operators": 0, "visitors": 0}' \
                          ',{"site_id": 456, "messages": 0, "emails": 0, "operators": 0, "visitors": 0}]'
        self.assertEqual(processor.build_json_string(test_sites), expected_string)
