[app]
title = My Kivy App
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.0.0

[buildozer]
log_level = 2
warn_on_root = 1

[app:source.exclude_patterns]
*.pyc
__pycache__

[buildozer:android]
android.ndk = 25b
android.sdk = 34
android.api = 34
android.minapi = 21
android.archs = arm64-v8a
android.permissions = INTERNET
p4a.bootstrap = sdl2
p4a.python_version = 3.11