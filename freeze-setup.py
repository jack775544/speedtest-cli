from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('speedtest.py', base=base, targetName = 'speedtest-standalone.exe')
]

setup(name='speedtest-cli',
      version = '1.0',
      description = 'A cli client for speedtest.net',
      options = dict(build_exe = buildOptions),
      executables = executables)
