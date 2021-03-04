Summary:	Configure keyboard and mouse
Name:		lxinput
Version:	0.3.5
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Other
# restore broked system changes for GTK3
Url:		http://www.lxde.org
Source0:	http://sourceforge.net/lxde/%{name}-%{version}.tar.xz
BuildRequires:	docbook-dtd412-xml
BuildRequires:	intltool >= 0.40.0
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(gtk+-3.0)

%description
LXInput is a small program used to configure keyboard and mouse for LXDE.

%prep
%setup -q

%build
%configure --enable-man --enable-gtk3
%make_build

%install
%make_install

%{find_lang} %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_mandir}/man1/*.1*
