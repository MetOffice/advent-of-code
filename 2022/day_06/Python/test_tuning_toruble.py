from tuning_toruble import find_packet
import pytest
@pytest.mark.parametrize("string,packet_position", [(["mjqjpqmgbljsphdztnvjfqwrcgsmlb"], 7),
                                          (["bvwbjplbgvbhsrlpgdmjqwftvncz"], 5),
                                          (["nppdvjthqldpwncqszvftbrmjlhg"], 6),
                                          (["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"], 10),
                                          (["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"], 11)])
def test_find_packet(string, packet_position):
    test_out = find_packet(string)
    assert packet_position == test_out

@pytest.mark.parametrize("string,packet_position", [(["mjqjpqmgbljsphdztnvjfqwrcgsmlb"], 19),
                                          (["bvwbjplbgvbhsrlpgdmjqwftvncz"], 23),
                                          (["nppdvjthqldpwncqszvftbrmjlhg"], 23),
                                          (["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"], 29),
                                          (["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"], 26)])
def test_find_message(string, packet_position):
    test_out = find_packet(string, packet_length=14)
    assert packet_position == test_out