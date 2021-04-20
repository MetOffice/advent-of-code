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

    def validate(self):
        '''Validate the entries in the passport :
                1. that all required fields are present.
                2. That no /extra/ fields have crept '''
        pass

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

    for line in lines:
        if line:
            for entry in line.split():
                key, value = entry.split(":")
                setattr(current_passport, key, value)
        else:
            passports.append(current_passport)
            current_passport = Passport()
    return passports




def main():
    input_data = load_string()
    something = parse_passport(input_data)
    pass

if __name__ == '__main__':
    main()
