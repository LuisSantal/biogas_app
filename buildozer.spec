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
source.include_patterns = assets/*,kv/*,media/*

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.1,plyer,sqlite3

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = PythonProject1/assets/images/app_icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 2.3.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (list) Permissions
android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 30

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 23b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you do not want to wait for it.
#android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.renpy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
#android.apptheme = "@android:style/Theme.NoTitleBar"

# (str) Android logcat filters (default)
#android.logcat_filters = *:S python:D

# (str) Android additional adb arguments
#android.adb_args = -H host.docker.internal

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) List of shared libraries to add to the APK
# The library will be copied in the sources/lib-<abi> folder and
# will be included in the APK.
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android/*.so
#android.add_libs_arm64_v8a = libs/android/*.so
#android.add_libs_x86 = libs/android/*.so
#android.add_libs_x86_64 = libs/android/*.so

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (list) add java files to add to the android project (can be java or a
# directory containing the files)
#android.add_java_files =

# (list) add jar files to add to the android project
#android.add_jar_files =

# (list) add files or directories to add to the java classpath
#android.add_classpath =

# (list) add files or directories to add to the java sourcepath
#android.add_sourcepath =

# (list) Java classes to add as activities to the manifest.
#android.add_activities =

# (str) OUYA Console category. For the OUYA Console.
# see: https://devs.ouya.tv/docs/ouya-consoles-categories
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in the main activity
#android.manifest.intent_filters =

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (list) Android additional libraries to copy into the libs/ folder
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android/*.so
#android.add_libs_arm64_v8a = libs/android/*.so
#android.add_libs_x86 = libs/android/*.so
#android.add_libs_x86_64 = libs/android/*.so

# (bool) Indicate whether the screen should stay on
# Don't forget to add the WAKE_LOCK permission if you set this to True
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
#android.library_references =

# (list) Android shared libraries which will be added to AndroidManifest.xml using <uses-library> tag
#android.uses_library =

# (str) Android logcat filters (default)
#android.logcat_filters = *:S python:D

# (bool) Android logcat only display log for activity's pid
#android.logcat_pid_only = False

# (str) Android additional adb arguments
#android.adb_args = -H host.docker.internal

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = arm64-v8a

# (bool) Enable AndroidX support. 
# When enabled, the Android support library will be replaced by AndroidX. 
# You need to set the same version for AndroidX libraries than the support library version.
#android.use_androidx = False

# (bool) Enable Android Service. 
# You need to add a service section.
#android.service = False

# (bool) Enable auto backup (Android 6.0+). 
# If set to True, the application will be automatically backed up. 
# Note: This will not backup the application data, only the APK.
android.allow_backup = True

# (str) Android app process name, default is ok for Kivy-based app
#android.app_process_name = org.renpy.android.PythonActivity

#
# Buildozer specific
#

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = .buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = bin

#    -----------------------------------------------------------------------------
#    List of sections
#    -----------------------------------------------------------------------------

#    You can define sections to be used later in the requirements.
#    For example:
#    from kivy.utils import platform
#    if platform == 'android':
#        requirements.append('pyjnius')
#    elif platform == 'ios':
#        requirements.append('pyobjus')

#    -----------------------------------------------------------------------------
#    Profiles
#    -----------------------------------------------------------------------------

#    You can define section profiles to build the application on different
#    configurations.

#    For example:
#    [profile@demo]
#    title = My Application (Demo)
#    source.include_exts = txt,png,jpg
#    source.include_patterns = assets/demo/*

#    [profile@full]
#    title = My Application
#    source.include_exts = txt,png,jpg,kv
#    source.include_patterns = assets/*

#    Then, to build the application in demo mode, run:
#    buildozer --profile demo android debug

#    To build the application in full mode, run:
#    buildozer --profile full android debug

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = .buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = bin

#    -----------------------------------------------------------------------------
#    List of find commands
#    -----------------------------------------------------------------------------

#    You can define find commands to be used to find files in the source.dir
#    For example:
#    [find]
#    name = **/*.py
#    exclude = **/test*

#    Then, to use the find command, add the following in the requirements:
#    requirements = hostpython3, find

#    -----------------------------------------------------------------------------
#    List of grep commands
#    -----------------------------------------------------------------------------

#    You can define grep commands to be used to grep files in the source.dir
#    For example:
#    [grep]
#    name = version
#    files = main.py

#    Then, to use the grep command, add the following in the requirements:
#    requirements = hostpython3, grep
