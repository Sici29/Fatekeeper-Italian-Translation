# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path

block_cipher = None

datas = [
    ('payload/pakchunk0-Windows_P.pak', 'payload'),
    ('payload/SLASHER.uproject', 'payload'),
    ('payload/Game.locres', 'payload'),
    ('payload/Game.locmeta', 'payload'),
]

a = Analysis(
    ['tools/fatekeeper_it_installer.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['pandas', 'openpyxl', 'lxml', 'matplotlib', 'scipy', 'tkinter'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Fatekeeper-Italian-Translation',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/fatekeeper-italian-installer-icon.ico',
)
