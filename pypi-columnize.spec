#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-columnize
Version  : 0.3.11
Release  : 6
URL      : https://files.pythonhosted.org/packages/b0/ab/47c68ccca6052e18ccce562e6af92404b08cb2715edd9e9da31f4118cbcd/columnize-0.3.11.tar.gz
Source0  : https://files.pythonhosted.org/packages/b0/ab/47c68ccca6052e18ccce562e6af92404b08cb2715edd9e9da31f4118cbcd/columnize-0.3.11.tar.gz
Summary  : Format a simple (i.e. not nested) list into aligned columns.
Group    : Development/Tools
License  : MIT
Requires: pypi-columnize-license = %{version}-%{release}
Requires: pypi-columnize-python = %{version}-%{release}
Requires: pypi-columnize-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
|packagestatus|
        
        In showing a long lists, sometimes one would prefer to see the value
        arranged aligned in columns. Some examples include listing methods of an
        object, listing debugger commands, or showing a numeric array with data
        aligned.
        
        This is a Python module to format a simple (i.e. not nested) list into
        aligned columns. A string with embedded newline characters is returned.
        
        Setup
        -----

%package license
Summary: license components for the pypi-columnize package.
Group: Default

%description license
license components for the pypi-columnize package.


%package python
Summary: python components for the pypi-columnize package.
Group: Default
Requires: pypi-columnize-python3 = %{version}-%{release}

%description python
python components for the pypi-columnize package.


%package python3
Summary: python3 components for the pypi-columnize package.
Group: Default
Requires: python3-core
Provides: pypi(columnize)

%description python3
python3 components for the pypi-columnize package.


%prep
%setup -q -n columnize-0.3.11
cd %{_builddir}/columnize-0.3.11
pushd ..
cp -a columnize-0.3.11 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656366453
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-columnize
cp %{_builddir}/columnize-0.3.11/LICENSE %{buildroot}/usr/share/package-licenses/pypi-columnize/6044e4ed016dcd2b620554a8a1a6880bc24dd72d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-columnize/6044e4ed016dcd2b620554a8a1a6880bc24dd72d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
