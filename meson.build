project('frida-python', 'c',
  version: run_command(find_program('python3'), files('setup.py'), '-V',
    capture: true,
    check: true).stdout().strip(),
  meson_version: '>=1.3.0',
)

python = import('python').find_installation()
cc = meson.get_compiler('c')
host_os_family = host_machine.system()
if host_os_family == 'android'
  host_os_family = 'linux'
endif

frida_component_cflags = []
ndebug = get_option('b_ndebug')
if ndebug == 'true' or (ndebug == 'if-release' and not get_option('debug'))
  frida_component_cflags += [
    '-DG_DISABLE_ASSERT',
    '-DG_DISABLE_CHECKS',
    '-DG_DISABLE_CAST_CHECKS',
  ]
endif

python_dep = python.dependency()
frida_core_dep = dependency('frida-core-1.0')

os_deps = []
if host_machine.system() != 'windows'
  os_deps += dependency('gio-unix-2.0')
endif

subdir('frida')
