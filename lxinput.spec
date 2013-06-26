Summary:	Configure keyboard and mouse
Name:		lxinput
Version:	0.3.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
# restore broked system changes for GTK3
Url:		http://www.lxde.org
Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.gz
BuildRequires:	docbook-dtd412-xml
BuildRequires:	intltool >= 0.40.0
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(gtk+-x11-2.0)

%description
LXInput is a small program used to configure keyboard and mouse for LXDE.

%prep
%setup -q

%build
%configure2_5x --enable-man
%make

%install
%makeinstall_std

%{find_lang} %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_mandir}/man1/*.1*

