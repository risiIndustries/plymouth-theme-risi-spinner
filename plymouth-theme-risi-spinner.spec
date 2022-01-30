%define set_theme %{_sbindir}/plymouth-set-default-theme

Name:           plymouth-theme-risi-spinner
Version:        0.9.5
Release:        2%{?dist}
Summary:        risiOS Plymouth Theme
 
License:        GPLv2+
URL:            https://github.com/risiOS/plymouth-theme-risi-spinner
Source0:        https://github.com/risiOS/plymouth-theme-risi-spinner/archive/refs/heads/main.tar.gz#/plymouth-theme-risi-spinner-main.tar.gz
BuildArch:      noarch
Requires:       plymouth-plugin-two-step >= 0.7.0
Requires(post): plymouth-scripts

%description
Plymouth Theme for risiOS

%prep
%autosetup -n plymouth-theme-risi-spinner-main

%build

%install
mkdir -p %{buildroot}%{_datadir}/plymouth/themes/risi-spinner
mkdir -p %{buildroot}%{_datadir}/plymouth/themes/risi-bgrt
install -m 0644 risi-bgrt.plymouth %{buildroot}%{_datadir}/plymouth/themes/risi-bgrt
install -m 0644 risi-spinner.plymouth *.png %{buildroot}%{_datadir}/plymouth/themes/risi-spinner

%post
export LIB=%{_lib}
# on initial install, set this as the new theme
if [ $1 -eq 1 ]; then
    %{set_theme} risi-bgrt
fi
 
%postun
export LIB=%{_lib}
# if uninstalling, reset to boring meatless default theme
if [ $1 -eq 0 ]; then
    if [ "$(%{set_theme})" == "risi-bgrt" ]; then
        %{set_theme} --reset
    fi
fi
	
%files
%{_datadir}/plymouth/themes/risi-bgrt
%{_datadir}/plymouth/themes/risi-spinner
	
%changelog
* Thu Aug 19 2021 PizzaLovingNerd - 1.0
- spec file created
