from passports import parse_passport, Passport, get_passports, count_valid_passports
import pytest

# NO NEW LINE AT THE END OF THE INPUT!
INPUT_DATA = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm                                
              
iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884        
hcl:#cfa07d byr:1929           

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""".split(
    "\n"
)


# @pytest.mark.parametrize(
#    "right, down, expected", [(1, 1, 2), (3, 1, 7), (5, 1, 3), (7, 1, 4), (1, 2, 2)]
# )
def test_parse_passport():
    expected_len = 4
    actual = parse_passport(INPUT_DATA)

    assert len(actual) == expected_len
    # Next, Do what Harold said, only later:
    # i.e setup 4 passports which should match input data above and then
    # test all possports are equal to those generated by parse_passport
    expected_passports = []
    expected_passports.append(
        Passport(
            ecl="gry",
            pid="860033327",
            eyr="2020",
            hcl="#fffffd",
            byr="1937",
            iyr="2017",
            cid="147",
            hgt="183cm",
        )
    )
    expected_passports.append(
        Passport(
            iyr="2013",
            ecl="amb",
            cid="350",
            eyr="2023",
            pid="028048884",
            hcl="#cfa07d",
            byr="1929",
        )
    )
    expected_passports.append(
        Passport(
            hcl="#ae17e1",
            iyr="2013",
            eyr="2024",
            ecl="brn",
            pid="760753108",
            byr="1931",
            hgt="179cm",
        )
    )
    expected_passports.append(
        Passport(
            hcl="#cfa07d",
            eyr="2025",
            pid="166559648",
            iyr="2011",
            ecl="brn",
            hgt="59in",
        )
    )
    assert actual == expected_passports


def test_passport_equality():
    passport_a = Passport(
        ecl="gry",
        pid="860033327",
        eyr="2020",
        hcl="#fffffd",
        byr="1937",
        iyr="2017",
        hgt="183cm",
    )
    passport_b = Passport(
        ecl="gry",
        pid="860033327",
        eyr="2020",
        hcl="#fffffd",
        byr="1937",
        iyr="2017",
        hgt="183cm",
    )

    assert passport_a == passport_b


def test_passport_inequality():
    """Have altered eye colour and added 'cid' """
    passport_a = Passport(
        ecl="gry",
        pid="860033327",
        eyr="2020",
        hcl="#dddddd",
        byr="1937",
        iyr="2017",
        hgt="183cm",
        cid="147",
    )
    passport_b = Passport(
        ecl="gry",
        pid="860033327",
        eyr="2020",
        hcl="#fffffd",
        byr="1937",
        iyr="2017",
        hgt="183cm",
    )

    assert passport_a != passport_b


def test_validate_passport_missing_cid():
    passport = Passport(
        ecl="gry",
        pid="860033327",
        eyr="2020",
        hcl="#fffffd",
        byr="1937",
        iyr="2017",
        hgt="183cm",
    )
    ignorable_fields = ["cid"]
    actual = passport.validate(ignorable_fields)
    assert actual


def test_validate_passport_missing_eyr():
    passport = Passport(
        ecl="gry", pid="860033327", hcl="#fffffd", byr="1937", iyr="2017", hgt="183cm"
    )
    ignorable_fields = ["cid"]
    actual = passport.validate(ignorable_fields)
    assert not actual


def test_count_valid_passports():
    passports = get_passports(INPUT_DATA)
    ignorable_fields = ["cid"]
    actual = count_valid_passports(passports, ignorable_fields)
    expected = 2
    assert actual == expected


def test_count_valid_passports_no_ignorable_fields():
    passports = get_passports(INPUT_DATA)
    ignorable_fields = []
    actual = count_valid_passports(passports, ignorable_fields)
    expected = 1
    assert actual == expected


@pytest.mark.parametrize(
    "input, expected", [("#123abc", True), ("#123abz", False), ("123abc", False)]
)
def test__validate_hcl_value(input, expected):
    passport = Passport()

    result = passport._validate_hcl_value(input)
    assert expected == result


@pytest.mark.parametrize(
    "input, expected",
    [("60in", True), ("190cm", True), ("190in", False), ("190", False)],
)
def test__validate_hgt_value(input, expected):
    passport = Passport()
    result = passport._validate_hgt_value(input)
    assert expected == result


@pytest.mark.parametrize(
    "input, expected",
    [("000000001", True), ("0123456789", False), ("19238459j", False)],
)
def test__validate_pid_value(input, expected):
    passport = Passport()
    result = passport._validate_pid_value(input)
    assert expected == result