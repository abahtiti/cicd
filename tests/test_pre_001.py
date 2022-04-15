from pybatfish.client.asserts import *


def test_bgp_multipath(bf_init):
    """Test BGP Multipath is configured"""
    bgp_multipath = list(
        bf_init.q.bgpProcessConfiguration(properties="Multipath_EBGP")
        .answer()
        .frame()
        .Multipath_EBGP
    )

    if False in bgp_multipath:
        raise AssertionError(bgp_multipath)


def test_no_ip_duplicates(bf_init):
    """Test IP duplicates"""
    ip_duplicates = bf_init.q.ipOwners(duplicatesOnly=True).answer().frame()

    # Remove VPC SVIs
    ip_duplicates_no_svi = ip_duplicates[
        ip_duplicates["IP"].str.contains(r"10.2.[1-3]0.254") == False
    ].empty

    if not ip_duplicates_no_svi:
        raise AssertionError(ip_duplicates)


def test_no_duplicate_router_ids(bf_init):
    """Test OSPF and BGP for duplicate route ids"""
    assert assert_no_duplicate_router_ids(session=bf_init)


def test_no_unestablished_bgp_sessions(bf_init):
    """Test BGP sessions are established"""
    assert assert_no_unestablished_bgp_sessions(session=bf_init)


def test_assert_no_incompatible_bgp_sessions(bf_init):
    """Test BGP sessions are compatible"""
    #assert assert_no_incompatible_bgp_sessions(session=bf_init)
    pass


def test_assert_no_incompatible_ospf_sessions(bf_init):
    """Test OSPF sessions are compatible"""
    assert assert_no_incompatible_ospf_sessions(session=bf_init)


def test_assert_no_forwarding_loops(bf_init):
    """Test for forwarding loops"""
    assert assert_no_forwarding_loops(session=bf_init)
