%define		_plugin	change_mysqlpass
%define		mversion	1.2.8
Summary:	Change_mysqlpass plugin for SquirrelMail
Summary(pl.UTF-8):   Wtyczka do zmiany haseł w bazie MySQL
Name:		squirrelmail-plugin-%{_plugin}
Version:	3.2
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}-%{mversion}.tar.gz
# Source0-md5:	fe62211cae50bf460feec643211d7308
URL:		http://www.squirrelmail.org/
Requires:	squirrelmail >= %{mversion}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_datadir}/squirrelmail/plugins/%{_plugin}

%description
Change MySQL Password allows users to change their passwords when they
are stored in a MySQL database. Supports both crypted (MD5, SASL,
UNIX) and plaintext passwords as well as allowing the administrator to
force password changes. If you have SSL support in your web server,
you may also force the connection to SSL when the user is changing her
password.

%description -l pl.UTF-8
Change MySQL Password pozwala użytkownikom na zmianę ich haseł jeśli
są przechowywane w mazie MySQL. Obsługuje szyfrowanie (MD5, SASL,
UNIX) oraz hasła czystym tekstem w zależności od tego, na co pozwala
administrator. Jeśli serwer WWW obsługuje SSL, można także wymusić
połączenie przez SSL w przypadku zmiany hasła przez użytkownika.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}

install *.php $RPM_BUILD_ROOT%{_plugindir}
install config.php.sample $RPM_BUILD_ROOT%{_plugindir}/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README
%config(noreplace) %verify(not size mtime md5) %{_plugindir}/config.php
%dir %{_plugindir}
%{_plugindir}/*.php
