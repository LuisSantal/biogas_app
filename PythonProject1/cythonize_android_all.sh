#!/bin/bash
# Script para Cythonizar los archivos android/_android.pyx y android/_android_jni.pyx en ambas arquitecturas
set -e

for arch in arm64-v8a armeabi-v7a; do
    dir=".buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/android-sdl2/${arch}__ndk_target_21/android/android"
    pyx_dir=".buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/android-sdl2/${arch}__ndk_target_21/android/android"
    if [ -d "$pyx_dir" ]; then
        if [ -f "$pyx_dir/_android.pyx" ]; then
            cython "$pyx_dir/_android.pyx" || true
        fi
        if [ -f "$pyx_dir/_android_jni.pyx" ]; then
            cython "$pyx_dir/_android_jni.pyx" || true
        fi
    fi
done
