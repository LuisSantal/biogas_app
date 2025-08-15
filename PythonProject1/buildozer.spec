[app]
title = Biogás nas Escolas
package.name = biogasapp
package.domain = br.edu.unila
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
source.include_patterns = assets/*,kv/*,media/*

version = 0.1

requirements = python3,kivy==2.2.1,plyer,requests

icon.filename = assets/images/app_icon.png

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 30
android.minapi = 21
android.ndk_api = 21

android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

# Adicione a linha abaixo para contornar o erro de compilação da libffi
p4a_hook = p4a_hook.py
android.p4a_recipes_exclude_arch_flags = libffi

# --- Ajustes para pyjnius e compatibilidade Python 3 ---
p4a_patches = local_recipes/pyjnius/pyjnius_python3_long_fix.patch,local_recipes/pyjnius/genericndkbuild_jnienv_getter.patch

# Forçar python-for-android a usar Python 3.9
android.python3 = /workspaces/biogas_app/PythonProject1/venv_buildozer_py39/bin/python3.9
android.python3_path = /workspaces/biogas_app/PythonProject1/venv_buildozer_py39/bin/python3.9
android.build_python = /workspaces/biogas_app/PythonProject1/venv_buildozer_py39/bin/python3.9

[buildozer]
log_level = 2
warn_on_root = 1

python3 = /workspaces/biogas_app/PythonProject1/venv_buildozer_py39/bin/python3.9


