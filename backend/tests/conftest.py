from portal.ufac.volto.testing import ACCEPTANCE_TESTING
from portal.ufac.volto.testing import FUNCTIONAL_TESTING
from portal.ufac.volto.testing import INTEGRATION_TESTING
from pytest_plone import fixtures_factory


pytest_plugins = ["pytest_plone"]


globals().update(
    fixtures_factory(
        (
            (ACCEPTANCE_TESTING, "acceptance"),
            (FUNCTIONAL_TESTING, "functional"),
            (INTEGRATION_TESTING, "integration"),
        )
    )
)