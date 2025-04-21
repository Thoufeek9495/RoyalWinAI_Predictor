[app]
title = RoyalWinAI
package.name = royalwinai
package.domain = org.royalwin.ai
source.dir = .
source.include_exts = py,png,jpg,kv,json
entrypoint = predictor_gui.py
icon.filename = %(source.dir)s/icon.png
orientation = portrait
android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.build_tools_version = 33.0.0
android.archs = armeabi-v7a, arm64-v8a

requirements = python3,kivy

log_level = 2
copy_libs = 1
android.entrypoint = org.kivy.android.PythonActivity
android.apptheme = @android:style/Theme.NoTitleBar
android.bootstrap = sdl2
enable_androidx = 1
