# frida-python

Python [bindings](https://github.com/frida/frida-python) for [Frida](https://frida.re), built against a Frida devkit.

The extension and its Python facade are generated at install time from the devkit's `frida-core.gir`, then linked against its `libfrida-core` library. No Frida source checkout or Frida source build is needed.

# Some tips during development

To build and test your own wheel, do something along the following lines:

```shell
FRIDA_VERSION=<FRIDA_VERSION> FRIDA_CORE_DEVKIT=<DEVKIT_PATH> pip wheel .
pip install --force-reinstall frida-<FRIDA_VERSION>-cp37-abi3-linux_aarch64.whl
```

> [!NOTE]
> Use the devkit for the same version that you are installing. The generator also needs the system `GLib-2.0.gir`, `GObject-2.0.gir`, and `Gio-2.0.gir` files. On Termux these are normally in `$PREFIX/share/gir-1.0`. Set `FRIDA_GIR_DIR` if they are elsewhere.

## Example:

### Automatic (Termux):
```shell
wget https://maglit.me/frida-python -O frida-python.sh && bash frida-python.sh
```

### Manually
If you're installing frida `16.4.10` and you've downloaded devkit `frida-core-devkit-16.4.10-android-arm64.tar.xz` and extracted into your termux path `$HOME/devkit`:

```shell
git clone https://github.com/AbhiTheModder/frida-python
cd frida-python
FRIDA_VERSION=16.4.10 FRIDA_CORE_DEVKIT=../devkit pip install .
```
then install `frida-tools`:
```shell
pip install --upgrade frida-tools
```
