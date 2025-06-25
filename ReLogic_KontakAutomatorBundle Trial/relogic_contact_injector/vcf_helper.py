import re

def parse_vcf(vcf_path):
    contacts = []
    with open(vcf_path, 'r', encoding='utf-8') as f:
        vcard = {}
        for line in f:
            line = line.strip()
            if line == 'BEGIN:VCARD':
                vcard = {}
            elif line.startswith('FN:'):
                vcard['name'] = line[3:]
            elif line.startswith('TEL'):
                match = re.search(r':(.+)', line)
                if match:
                    vcard['phone'] = match.group(1)
            elif line == 'END:VCARD':
                if vcard:
                    contacts.append(vcard)
    return contacts

def validate_contact(contact):
    # Minimal validasi: harus ada nama & nomor
    name = contact.get('name', '').strip()
    phone = contact.get('phone', '').strip()
    return bool(name and phone)
