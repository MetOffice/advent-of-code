import re

from common.loaders import load_string

class Passport:
    def __init__(self, byr=None, iyr=None, eyr=None, hgt=None,
                 hcl=None, ecl=None, pid=None, cid=None):
        ''' byr (Birth Year)
            iyr (Issue Year)
            eyr (Expiration Year)
            hgt (Height)
            hcl (Hair Color)
            ecl (Eye Color)
            pid (Passport ID)
            cid (Country ID)
        '''
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid
        self.required_fields = [
            "ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt", "cid"]


    def validate(self, ignorable_fields, validate_values=False):
        '''Validate the entries in the passport :
                1. that all required fields are present.
                2. That no /extra/ fields have crept '''
        result = True
        missing_fields = []
        for field in self.required_fields:
            value = getattr(self, field)
            if value is None:
                if field not in ignorable_fields:
                    missing_fields.append(field)
                    result = False
            else:
                if validate_values:
                    result = self._validate_value(field, value)

        if missing_fields:
            print(f"Missing fields {missing_fields}")
        return result

    def _validate_value(self, field, value):
        attribute = f"_validate_{field}_value"
        method = getattr(self, attribute, None)
        result = True
        if method is not None:
            result = method(value)
        return result

    def _validate_byr_value(self, value):
        four_digits = len(value) != 4
        valid_range = int(value) >= 1920 and int(value) <= 2002
        return four_digits and valid_range

    def _validate_iyr_value(self, value):
        four_digits = len(value) != 4
        valid_range = int(value) >= 2010 and int(value) <= 2020
        return four_digits and valid_range

    def _validate_eyr_value(self, value):
        four_digits = len(value) != 4
        valid_range = int(value) >= 2020 and int(value) <= 2030
        return four_digits and valid_range

    def _validate_hgt_value(self, value):
        valid_units = True
        units = value[-2]
        if units == "cm":
            lower_value = 150
            upper_value = 193
        elif units == "in":
            lower_value = 59
            upper_value = 76
        else:
            valid_units = False
        valid_range = True
        if valid_units:
            valid_range = (
                value[:-2] >= lower_value and value[:-2] <= upper_value)
        return valid_units and valid_range

    def _validate_hcl_value(self, value):
        pattern = r"#[0-9a-f]{6}"
        valid_string = re.match(pattern, value)
        return valid_string is not None

    def _validate_ecl_value(self, value):
        valid_values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return value in valid_values

    def _validate_pid_value(self, value):
        pattern = r"[0-9]{9}"
        valid_string = re.match(pattern, value)
        return valid_string is not None

    def __eq__(self, other):
        '''test for equality in 2 passports'''
        return all([self.byr == other.byr,
                    self.iyr == other.iyr,
                    self.eyr == other.eyr,
                    self.hgt == other.hgt,
                    self.hcl == other.hcl,
                    self.ecl == other.ecl,
                    self.pid == other.pid,
                    self.cid == other.cid])


def parse_passport(lines):
    '''Provided with lines from an input file, splits them into passport records
    and then splits each record into the attributes of a passport'''
    current_passport = Passport()
    passports = []

    lines.append("")
    for line in lines:
        # Passports are separated by blank lines, which may contain spaces.
        # Remove all whitespace before checking if the line is empty.
        if line.strip():
            for entry in line.split():
                key, value = entry.split(":")
                setattr(current_passport, key, value)
        else:
            passports.append(current_passport)
            current_passport = Passport()
    return passports


def get_passports(input_data):
    return parse_passport(input_data)


def count_valid_passports(passports, ignorable_fields):
    valid_passports = 0
    for passport in passports:
        valid_passports += int(passport.validate(ignorable_fields,
                                                 validate_values=True))
    return valid_passports


def main():
    input_data = load_string()
    passports = get_passports(input_data)
    print(f"Number of passports: {len(passports)}")
    ignorable_fields = ["cid"]
    count = count_valid_passports(passports, ignorable_fields)
    return count


if __name__ == '__main__':
    print(main())
