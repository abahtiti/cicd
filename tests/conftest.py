import logging
from pathlib import Path

import pytest
from pybatfish.client.session import Session


@pytest.fixture(scope="session")
def bf_init():
    # SNAPSHOT_NAME = "013_integrations_pytest"
    SNAPSHOT_NAME = "snapshot"

    BF_SNAPSHOT_PATH = f"{Path(__file__).parent.parent}/{SNAPSHOT_NAME}"

    logging.getLogger("pybatfish").setLevel(logging.WARN)

    bf = Session(host="localhost")
    bf.init_snapshot(BF_SNAPSHOT_PATH, overwrite=True)

    return bf

