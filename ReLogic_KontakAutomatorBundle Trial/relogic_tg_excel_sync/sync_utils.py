from collections import OrderedDict

def sync_contacts(tg_contacts, excel_contacts):
    # Gabungkan kontak berdasarkan nomor telepon (phone) sebagai key unik
    merged = OrderedDict()
    for c in excel_contacts:
        phone = c.get('phone', '').strip()
        if phone:
            merged[phone] = c
    for c in tg_contacts:
        phone = c.get('phone', '').strip()
        if phone:
            merged[phone] = {**merged.get(phone, {}), **c}  # update/merge
    return list(merged.values())
