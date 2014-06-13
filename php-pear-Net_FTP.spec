%define	_class		Net
%define	_subclass	FTP
%define	modname	%{_class}_%{_subclass}

Summary:	Comfortable communication with FTP-servers
Name:		php-pear-%{modname}
Version:	1.3.7
Release:	13
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Net_FTP/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires:	php-ftp
Requires(post,preun):	php-pear
Requires:	php-pear

%description
This class allows you to communicate with FTP-servers more comfortable
that the ftp-functions of PHP. Especially you can up- and download
recursively.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/data/%{modname}/CHANGELOG

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/example
%doc %{modname}-%{version}/CHANGELOG
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

