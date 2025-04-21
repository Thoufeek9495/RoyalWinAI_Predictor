[app]

# ✅ App Info
title = RoyalWinAI
package.name = royalwinai
package.domain = org.royalwin.ai
version = 1.0

# ✅ Project Structure
source.dir = .
source.include_exts = py,png,jpg,kv,json
icon.filename = %(source.dir)s/icon.png

# ✅ Main Python File (change if your main file is not main.py)
entrypoint = main.py

# ✅ Orientation
orientation = portrait

# ✅ Permissions
android.permissions = INTERNET

# ✅ Android Versions
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.build_tools_version = 33.0.0

# ✅ Architectures
android.archs = armeabi-v7a, arm64-v8a

# ✅ Python and Kivy
requirements = python3,kivy

# ✅ Updated Build Configuration
p4a.bootstrap = sdl2
android.entrypoint = org.kivy.android.PythonActivity
android.apptheme = @android:style/Theme.NoTitleBar

# ✅ Modern Compatibility
enable_androidx = 1
copy_libs = 1
log_level = 2

# ✅ Optional Extras (customize if needed)
# android.logcat_filters = *:S python:D
# android.add_src = path/to/extra/java
# android.add_jars = path/to/extra.jar
