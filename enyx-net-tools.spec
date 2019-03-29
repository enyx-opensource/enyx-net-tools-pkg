Name: enyx-net-tools
Release: 1%{dist}
Version: 0.1.6
License: GPLv3
URL: http://www.enyx.fr
BuildRequires: cmake3 boost-devel
ExclusiveOS: Linux
Vendor: Enyx
Source0: https://github.com/enyx-opensource/net-tools/archive/v%{version}/net-tools-%{version}.tar.gz
Summary: Net utilities used to test and benchmark Enyx solutions

%description
This package contains nx-iperf utility used to communicate from
a software application with the Enyx TCP or UDP hardware IP.

%files
%defattr(-,root,root,-)
/usr/bin/nx-iperf

%prep
%autosetup -n net-tools-%{version}

%build
cmake3 -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
      .
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%make_install

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Fri Mar 29 2019 Enyx <support@enyx.fr> - 0.1.6-1
    - Follow upstream 0.1.6.
* Mon Jan 21 2019 Enyx <support@enyx.fr> - 0.1.5-1
    - Follow upstream 0.1.5.
* Mon Jan 21 2019 Enyx <support@enyx.fr> - 0.1.4-1
    - Follow upstream 0.1.4.
* Fri Oct 26 2018 Enyx <support@enyx.fr> - 0.1.3-1
    - Follow upstream 0.1.3.
* Mon Oct 15 2018 Enyx <support@enyx.fr> - 0.1.2-1
    - Follow upstream 0.1.2.
