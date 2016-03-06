%define bname   fedberry
%define name    %{bname}-config

Name:       %{name}
Version:    0.1
Release:    1%{?dist}
License:    GPLv3+
Summary:    Easy configuration of various system options in FedBerry
Group:      Applications/System
URL:        https://github.com/agrez/fedberry-config
Source0:    https://raw.githubusercontent.com/%{bname}/%{name}/master/%{name}
Source1:    https://raw.githubusercontent.com/%{bname}/%{name}/master/LICENSE
Source2:    https://raw.githubusercontent.com/%{bname}/%{name}/master/README.md
Source3:    https://raw.githubusercontent.com/%{bname}/%{name}/master/rootfs-grow.service
BuildArch:  noarch
Obsoletes:  rootfs-resize
Conflicts:  rootfs-resize
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
A utility for making common Raspberry Pi configuration changes via a simple menu-driven interface.
The majority of the configuration changes result in automated modifications to /boot/config.txt
and/or other standard Fedora configuration files. Many options will require a reboot to take effect.


%prep
%setup -c -T
cp -a %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} .


%build


%install
rm -rf %{buildroot}

%{__install} -d %{buildroot}/%{_sbindir}
%{__install} -p %{name} %{buildroot}/%{_sbindir}

%{__install} -d %{buildroot}/%{_unitdir}
%{__install} -p rootfs-grow.service %{buildroot}/%{_unitdir}


%clean
rm -rf %{buildroot}


%post
%systemd_post rootfs-grow.service


%preun
%systemd_preun rootfs-grow.service


%files
%doc README.md
%license LICENSE
%attr(0755,root,root) %{_sbindir}/%{name}
%attr(0644,root,root) %{_unitdir}/rootfs-grow.service


%changelog
* Sun Mar 06 2016 Vaughan <vaughan at agrez dot net> 0.1-1
- Initial package