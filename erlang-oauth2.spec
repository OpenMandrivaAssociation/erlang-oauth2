%global srcname oauth2
# Erlang packages do not provide debug subpackages.
%global debug_package %{nil}


Name:       erlang-%{srcname}
Version:    0.6.1
Release:    1
Group:      Development/Erlang

License:    MIT
Summary:    An Oauth2 implementation for Erlang
URL:        https://github.com/kivra/%{srcname}
Source0:    https://github.com/kivra/%{srcname}/archive/%{version}.tar.gz

BuildRequires: erlang-meck
BuildRequires: erlang-proper
BuildRequires: erlang-rebar


%description
This library is designed to simplify the implementation of the server side of
OAuth2.


%prep
%autosetup -n %{srcname}-%{version}


%build
%rebar_compile


%install
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/ebin

install -pm644 ebin/* $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/ebin


%files
%license LICENSE
%doc README.md
%{_erllibdir}/%{srcname}-%{version}



%changelog
* Sat May 07 2016 neoclust <neoclust> 0.6.1-3.mga6
+ Revision: 1010415
- Rebuild as it as been rejected
- imported package erlang-oauth2

