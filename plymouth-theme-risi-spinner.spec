%define themename risi-spinner
%define set_theme %{_sbindir}/plymouth-set-default-theme

Name:           plymouth-theme-%{themename}
Version:        1.0
Release:        1%{?dist}
Summary:        risiOS Plymouth Theme
 
License:        GPLv2+
URL:            https://github.com/risiOS/risi-plymouth-theme
Source0:        https://github.com/risiOS/risi-plymouth-theme/archive/refs/heads/main.tar.xz
BuildArch:      noarch
Requires:       plymouth-plugin-two-step >= 0.7.0
Requires(post): plymouth-scripts

%description
Plymouth Theme for risiOS

%prep

%build
%autosetup -n risi-plymouth-theme-main

%install
mkdir -p %{buildroot}%{_datadir}/plymouth/themes/risi-spinner
install -m 0644 %{themename}.plymouth %{_builddir}*.png %{_datadir}/plymouth/themes/risi-spinner
%{_builddir}

%post
export LIB=%{_lib}
# on initial install, set this as the new theme
if [ $1 -eq 1 ]; then
    %{set_theme} %{themename}
fi
 
%postun
export LIB=%{_lib}
# if uninstalling, reset to boring meatless default theme
if [ $1 -eq 0 ]; then
    if [ "$(%{set_theme})" == "%{themename}" ]; then
        %{set_theme} --reset
    fi
fi
	
%files
%doc README
%dir %{_datadir}/plymouth/themes/%{themename}
%{_datadir}/plymouth/themes/%{themename}/*.png
%{_datadir}/plymouth/themes/%{themename}/%{themename}.plymouth
	
%changelog
* Thu Aug 19 2021 PizzaLovingNerd - 1.0
