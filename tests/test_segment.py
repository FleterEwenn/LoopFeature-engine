from loopfeature.segment import Segment

def test_access_attribute_Segment():
    segment = Segment(35, 123456789)
    assert segment.id == 123456789
    assert segment.score == 35
