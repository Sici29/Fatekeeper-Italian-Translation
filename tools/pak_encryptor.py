import os
import struct
import hashlib
import subprocess
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

FATEKEEPER_AES_KEY = bytes.fromhex('3AB2785AB187B2089737DB4BE249A3C1E885D7ED7F0BBF225B5320B0529A511F')
PATH_HASH_SEED = 3324237248 # 0xC623D5C0 (v0.1.4 update)
REPAK_EXE = r'E:\TRADUZIONI\Tool UE\repak\repak.exe'

def pad16(data: bytes) -> bytes:
    rem = len(data) % 16
    if rem != 0:
        return data + b'\x00' * (16 - rem)
    return data

def aes_ecb_encrypt(data: bytes, key: bytes = FATEKEEPER_AES_KEY) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    enc = cipher.encryptor()
    return enc.update(data) + enc.finalize()

def encrypt_pak_indices(in_pak_path: str, out_pak_path: str, key: bytes = FATEKEEPER_AES_KEY):
    """
    Encrypts an unencrypted UE V11 pak file created by repak so that
    Primary Index, Path Hash Index, and Full Directory Index are AES-256-ECB encrypted,
    and FPakInfo footer has bEncryptedIndex = 1.
    """
    with open(in_pak_path, 'rb') as f:
        pak = f.read()

    # V11 footer is 221 bytes
    footer = pak[-221:]
    magic, = struct.unpack_from('<I', footer, 17)
    if magic != 0x5a6f12e1:
        raise ValueError(f"Invalid pak magic: 0x{magic:08x}")
    ver_major, = struct.unpack_from('<I', footer, 21)
    idx_off, = struct.unpack_from('<Q', footer, 25)
    idx_sz, = struct.unpack_from('<Q', footer, 33)

    raw_idx = bytearray(pak[idx_off:idx_off + idx_sz])

    # Parse primary index header
    pos = 0
    mp_len, = struct.unpack_from('<i', raw_idx, pos); pos += 4 + mp_len
    num_entries, = struct.unpack_from('<I', raw_idx, pos); pos += 4
    seed, = struct.unpack_from('<Q', raw_idx, pos); pos += 8
    
    has_phi, = struct.unpack_from('<I', raw_idx, pos); pos += 4
    phi_off_pos = pos
    phi_off, phi_sz = struct.unpack_from('<QQ', raw_idx, pos); pos += 16
    phi_hash_pos = pos
    phi_hash = raw_idx[pos:pos+20]; pos += 20

    has_fdi, = struct.unpack_from('<I', raw_idx, pos); pos += 4
    fdi_off_pos = pos
    fdi_off, fdi_sz = struct.unpack_from('<QQ', raw_idx, pos); pos += 16
    fdi_hash_pos = pos
    fdi_hash = raw_idx[pos:pos+20]; pos += 20

    raw_phi = pak[phi_off:phi_off + phi_sz]
    raw_fdi = pak[fdi_off:fdi_off + fdi_sz]

    padded_phi = pad16(raw_phi)
    new_phi_sz = len(padded_phi)
    new_phi_hash = hashlib.sha1(padded_phi).digest()

    padded_fdi = pad16(raw_fdi)
    new_fdi_sz = len(padded_fdi)
    new_fdi_hash = hashlib.sha1(padded_fdi).digest()

    data_end = idx_off
    new_idx_sz = ((len(raw_idx) + 15) // 16) * 16
    new_idx_off = data_end
    new_phi_off = new_idx_off + new_idx_sz
    new_fdi_off = new_phi_off + new_phi_sz

    # Update offsets & hashes in raw_idx
    struct.pack_into('<QQ', raw_idx, phi_off_pos, new_phi_off, new_phi_sz)
    raw_idx[phi_hash_pos:phi_hash_pos + 20] = new_phi_hash
    struct.pack_into('<QQ', raw_idx, fdi_off_pos, new_fdi_off, new_fdi_sz)
    raw_idx[fdi_hash_pos:fdi_hash_pos + 20] = new_fdi_hash

    padded_idx = pad16(bytes(raw_idx))
    new_idx_hash = hashlib.sha1(padded_idx).digest()

    # Encrypt
    enc_idx = aes_ecb_encrypt(padded_idx, key)
    enc_phi = aes_ecb_encrypt(padded_phi, key)
    enc_fdi = aes_ecb_encrypt(padded_fdi, key)

    # Footer
    new_footer = bytearray(footer)
    new_footer[16] = 1 # bEncryptedIndex = 1
    struct.pack_into('<QQ', new_footer, 25, new_idx_off, new_idx_sz)
    new_footer[41:61] = new_idx_hash

    new_pak = pak[:data_end] + enc_idx + enc_phi + enc_fdi + bytes(new_footer)

    with open(out_pak_path, 'wb') as f:
        f.write(new_pak)

    return len(new_pak)

def build_encrypted_pak_from_dir(input_dir: str, output_pak_path: str, key: bytes = FATEKEEPER_AES_KEY, seed: int = PATH_HASH_SEED):
    temp_unenc_pak = output_pak_path + ".unenc.tmp"
    try:
        cmd = [
            REPAK_EXE,
            'pack',
            '--version', 'V11',
            '--compression', 'Oodle',
            '-p', str(seed),
            input_dir,
            temp_unenc_pak
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        encrypt_pak_indices(temp_unenc_pak, output_pak_path, key)
    finally:
        if os.path.exists(temp_unenc_pak):
            os.remove(temp_unenc_pak)

def verify_pak_with_repak(pak_path: str, key_hex: str = '0x3AB2785AB187B2089737DB4BE249A3C1E885D7ED7F0BBF225B5320B0529A511F') -> bool:
    cmd = [
        REPAK_EXE,
        '-a', key_hex,
        'info',
        pak_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("repak info error:", res.stderr)
        return False
    return "encrypted index: true" in res.stdout
