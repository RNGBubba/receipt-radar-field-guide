from pathlib import Path


HTML = Path(__file__).with_name("receipt-radar.html")


def test_receipt_radar_is_a_self_contained_original_infographic():
    source = HTML.read_text(encoding="utf-8")
    assert "Receipt Radar" in source
    assert "Evidence ladder" in source
    assert "Payment proof" in source
    assert "<svg" in source
    assert "</html>" in source


def test_infographic_is_accessible_and_has_no_external_dependencies():
    source = HTML.read_text(encoding="utf-8")
    assert 'lang="en"' in source
    assert 'aria-labelledby="title subtitle"' in source
    assert "https://" not in source
    assert "http://" not in source


def test_receipt_radar_contains_operator_checklist():
    source = HTML.read_text(encoding="utf-8")
    for phrase in ("Who paid?", "What was delivered?", "Can someone else verify it?"):
        assert phrase in source
