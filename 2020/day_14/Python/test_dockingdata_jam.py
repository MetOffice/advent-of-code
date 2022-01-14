from dockingdata_jam import dockingdata

def test_dockingdata():
    sample = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0"
    ]

    assert dockingdata(sample) == 165