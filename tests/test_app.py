def test_home_status_code_and_body(client, monkeypatch):
    import app as app_module  # import the module to patch

    def fake_render_template(template_name):
        assert template_name == "index.html"
        return "OK"

    monkeypatch.setattr(app_module, "render_template", fake_render_template, raising=True)

    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.data == b"OK"