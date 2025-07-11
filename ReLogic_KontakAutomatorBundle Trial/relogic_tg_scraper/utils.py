import os

def log_failed_contact(user_id, name, username, reason):
    log_path = os.path.join(os.path.dirname(__file__), '../example_output/failed_contacts.log')
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write('TRIAL VERSION - Generated by ReLogic\n')
        f.write(f"ID: {user_id}, Name: {name}, Username: {username}, Reason: {reason}\n")

def write_vcf(entries, vcf_path, trial_watermark=None):
    os.makedirs(os.path.dirname(vcf_path), exist_ok=True)
    with open(vcf_path, 'w', encoding='utf-8') as f:
        if trial_watermark:
            f.write(f";{trial_watermark}\n")
        for entry in entries:
            name = entry.get('name', '')
            phone = entry.get('phone', '')
            f.write(
                'BEGIN:VCARD\n'
                'VERSION:3.0\n'
                f'FN:{name}\n'
                f'TEL;TYPE=CELL:{phone}\n'
                'END:VCARD\n'
            )
