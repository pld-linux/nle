%define		rel	2
Summary:	Logo editor for Nokia cellular phones
Summary(pl):	Edytor logo dla telefonów komórkowych Nokia
Name:		nle
Version:	0.0.1
Release:	2
License:	GPL
Source0:	ftp://ftp.mimuw.edu.pl/People/lczajka/nle/%{name}-%{version}-%{rel}.tgz
URL:		http://www.mimuw.edu.pl/~lczajka/nle/
Group:		X11/Applications
BuildRequires:	XFree86-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_bindir		%{_prefix}/bin

%description
Nokia Logo Editor allows you to edit nol and ngg files on a Nokia
phone.

%description -l pl
Edytor logo dla telefonów Nokia pozwala na edycjê plików nol oraz ngg.

%prep
%setup -q -n nle

%build
#./autogen.sh --prefix=%{_prefix}
rm -f missing
libtoolize --copy --force
gettextize --force --copy
aclocal
autoheader
autoconf
automake -a -c -f
%configure --with-gtk-exec-prefix=%{_prefix}
#--prefix=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/,%{_pixmapsdir}/%{name}/,%{_bindir}}
cp pixmaps/* $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}/

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT
gzip -9nf {AUTHORS,ChangeLog}

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz examples/*
%{_prefix}/bin/nle
%{_datadir}/pixmaps/nle/
