Name: dosfstools
Summary: Utilities for making and checking MS-DOS FAT filesystems on Linux
Version: 3.0.10
Release: 6
License: GPLv3+
Group: Applications/System
Source0: http://www.daniel-baumann.ch/software/dosfstools/%{name}-%{version}.tar.bz2
URL: http://www.daniel-baumann.ch/software/dosfstools/
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The dosfstools package includes the mkdosfs and dosfsck utilities,
which respectively make and check MS-DOS FAT filesystems on hard
drives or on floppies.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install-bin install-man PREFIX=%{_prefix} SBINDIR=/sbin

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc  COPYING doc/*-2.x
/sbin/*
%doc %{_mandir}/man8/*

