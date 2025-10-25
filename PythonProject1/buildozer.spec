[app]
title = Biogás nas Escolas
package.name = biogasapp
package.domain = br.edu.unila
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
source.include_patterns = assets/*,kv/*
source.exclude_dirs = .buildozer,bin,venv,venv_buildozer,venv_buildozer_py39,dist,tests,docs,examples
source.exclude_patterns = *.pyc,*.swp,venv*/*

version = 0.1

requirements = python3,kivy==2.3.0,sqlite3,plyer,pyjnius

icon.filename = assets/images/app_icon.png

orientation = portrait
fullscreen = 0

# Permissões do Android
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Configurações do Android SDK/NDK
android.api = 34
android.minapi = 21
android.ndk_api = 21

android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True


[buildozer]
log_level = 2
warn_on_root = 1

p4a.branch = develop
