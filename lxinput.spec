# git snapshot
%global snapshot 1
%if 0%{?snapshot}
	%global commit		c11ee4f7866de5e36e5b8b0e6959518cab24240d
	%global commitdate	20230917
	%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%endif

Summary:	Configure keyboard and mouse
Name:		lxinput
Version:	0.3.5
Release:	3
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://www.lxde.org
#Source0:	http://sourceforge.net/lxde/%{name}-%{version}.tar.xz
Source0:	https://github.com/lxde/lxinput/archive/%{?snapshot:%{commit}}%{!?snapshot:%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz
BuildRequires:	docbook-dtd412-xml
BuildRequires:	intltool >= 0.40.0
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(gtk+-3.0)

%description
LXInput is a small program used to configure keyboard and mouse for LXDE.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_mandir}/man1/*.1*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}

%build
autoreconf -fiv
%configure \
	--enable-gtk3 \
	--enable-man \
	%{nil}
%make_build
%install
%make_install

# locales
%{find_lang} %{name}

