%define		rel	2
Summary:	Logo editor for Nokia cellular phones
Summary(pl):	Edytor logo dla telefonów komórkowych Nokia
Name:		nle
Version:	0.0.1
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.mimuw.edu.pl/People/lczajka/nle/%{name}-%{version}-%{rel}.tgz
# Source0-md5:	2d7304317736ce113979c6596982dfdc
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-gettext.patch
URL:		http://www.mimuw.edu.pl/~lczajka/nle/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nokia Logo Editor allows you to edit nol and ngg files on a Nokia
phone.

%description -l pl
Edytor logo dla telefonów Nokia pozwala na edycjê plików nol oraz ngg.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--with-gtk-exec-prefix=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir}/%{name},%{_desktopdir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install pixmaps/* $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog examples/*
%attr(755,root,root) %{_bindir}/nle
%{_desktopdir}/nle.desktop
%{_pixmapsdir}/*
