import unittest
import src.sites as sites
from src.sites import Site


class SitesTests(unittest.TestCase):
    def test_add_site(self):
        site_id = '123'
        test_sites = sites.Sites()

        test_sites.add_site(site_id)

        self.assertEqual(len(test_sites.list), 1)

    def test_add_dup_site(self):
        site_id = '123'
        test_sites = sites.Sites()

        test_sites.add_site(site_id)
        test_site = test_sites.get_site(site_id)
        test_site.add_operator('operator1')
        test_site.add_visitor('visitor1')
        test_sites.add_site(site_id)

        self.assertEqual(len(test_sites.list), 1)
        self.assertEqual(test_site.num_operators(), 1)
        self.assertEqual(test_site.num_visitors(), 1)

    def test_sort_sites(self):
        test_sites = sites.Sites()

        site_id = '456'
        test_sites.add_site(site_id)

        site_id = '123'
        test_sites.add_site(site_id)

        sorted_sites_list = ['123', '456']

        result_sites = test_sites.list_sorted_site_ids()
        self.assertEqual(result_sites, sorted_sites_list)


class TestSite(unittest.TestCase):
    def test_add_operator(self):
        test_site = Site()
        test_site.add_operator('operator1')

        self.assertEqual(test_site.num_operators(), 1)

    def test_remove_operator(self):
        test_site = Site()
        test_site.add_operator('operator1')
        test_site.add_operator('operator2')
        test_site.remove_operator('operator2')

        self.assertEqual(test_site.num_operators(), 2)

    def test_remove_operator_non_existent(self):
        test_site = Site()
        test_site.remove_operator('operator2')

        self.assertEqual(test_site.num_operators(), 1)

    def test_num_online_operators(self):
        test_site = Site()
        test_site.add_operator('operator1')
        test_site.add_operator('operator2')
        test_site.remove_operator('operator2')

        self.assertEqual(test_site.num_online_operators(), 1)

    def test_add_visitor(self):
        test_site = Site()
        test_site.add_visitor('visitor5')

        self.assertEqual(test_site.num_visitors(), 1)
