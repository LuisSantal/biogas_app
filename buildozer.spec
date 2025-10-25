[app]

# (str) Title of your application
title = Biogás nas Escolas

# (str) Package name
package.name = biogasapp

# (str) Package domain (needed for android/ios packaging)
package.domain = br.edu.unila

# (str) Source code where the main.py live
source.dir = PythonProject1

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,db

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,kv/*

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_dirs = .buildozer,bin,venv,venv_buildozer,venv_buildozer_py39,dist,tests,docs,examples

# (list) List of exclusions using pattern matching
source.exclude_patterns = *.pyc,*.swp,venv*/*

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy==2.3.0,sqlite3,plyer,pyjnius

# (str) Icon of the application
icon.filename = PythonProject1/assets/images/app_icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
android.accept_sdk_license = True

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support. 
# When enabled, the Android support library will be replaced by AndroidX. 
# You need to set the same version for AndroidX libraries than the support library version.
#android.use_androidx = False

# (bool) Enable auto backup (Android 6.0+). 
# If set to True, the application will be automatically backed up. 
# Note: This will not backup the application data, only the APK.
android.allow_backup = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

p4a.branch = develop
