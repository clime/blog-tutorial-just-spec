# Spec file Preamble
Name:       example
Version:	1.0.0
Release:	1%{?dist}
Summary:	This is a simple example to test copr

License:	GPLv2+
URL:		https://github.com/blog-tutorial-just-spec
Source0:	https://clime.cz/%{name}-%{version}.tar.gz


# What this package does
%description
Simple example to demonstrate copr's abilites.


# These are instructions to prepare sources for the build.
%prep
%setup -q


# These are instructions to build the package.
%build
make %{?_smp_mflags}


# This installs package into system after it has been been built.
# Invoked e.g. by `dnf install example`.
%install
install -d %{buildroot}%{_sbindir}
cp -a main %{buildroot}%{_sbindir}/main


# Here you should list all the files the package provides.
%files
%doc
%{_sbindir}/main

# What has changed since the last version. High level overview
# over the last commits.
%changelog
* Tue Oct 24 2017 clime <clime@redhat.com> 1.0.0-1
- Initial version
