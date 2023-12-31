# Generated by rust2rpm 24
%bcond_with check
%global debug_package %{nil}

%global crate kvm-ioctls

Name:           rust-kvm-ioctls
Version:        0.15.0
Release:        1%{?dist}
Summary:        Safe wrappers over KVM ioctls

License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/kvm-ioctls
Source:         %{crates_source}

# This crate only supports x86_64 and aarch64 targets
ExclusiveArch:  x86_64 aarch64

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Safe wrappers over KVM ioctls.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Tue Oct 31 2023 Sergio Lopez <slp@redhat.com> - 0.15.0-1
- Update to version 0.15.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Sergio Lopez <slp@redhat.com> - 0.14.0-1
- Update to version 0.14.0
- Regenerate with rust2rpm 24

* Wed Feb 08 2023 Sergio Lopez <slp@redhat.com> - 0.13.0-1
- Update to version 0.13.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 07 2022 Sergio Lopez <slp@redhat.com> - 0.11.0-1
- Initial package
