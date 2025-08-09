import os
import subprocess

def before_build_arch(context):
    for arch in ['arm64-v8a', 'armeabi-v7a']:
        pyx_dir = f'.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/android-sdl2/{arch}__ndk_target_21/android/android'
        if os.path.isdir(pyx_dir):
            for pyx in ['_android.pyx', '_android_jni.pyx']:
                pyx_path = os.path.join(pyx_dir, pyx)
                if os.path.isfile(pyx_path):
                    subprocess.run(['cython', pyx_path], check=False)
