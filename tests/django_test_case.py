from unittest import TestCase

from django_framework.xxx import Xxx


class DjangoTestCase(TestCase):
    def setUp(self) -> None:
        use_perfect_technology = self._should_use_perfect_technology()
        if not use_perfect_technology:
            self._django_configurator = Xxx()
            self._django_configurator.initialize_django_from_test()
            self._django_configurator.initialize_django_db()

    def tearDown(self) -> None:
        use_perfect_technology = self._should_use_perfect_technology()
        if not use_perfect_technology:
            self._django_configurator.destroy_django_db()

    def _should_use_perfect_technology(self):
        import os
        testing_technology_var_name = 'TESTING_TECHNOLOGY'
        technology = os.getenv(testing_technology_var_name)
        if technology == 'PERFECT':
            return True
        if technology == 'DJANGO':
            return False
        raise ValueError(f'Unknown value for {testing_technology_var_name}: {technology}')
