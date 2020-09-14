def test_site_hello(host):
    assert host.run("wget -O - -q 127.0.0.1").stdout == "Hello world !"
