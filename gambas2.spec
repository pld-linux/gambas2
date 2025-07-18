#
# Conditional build:
%bcond_without	bzip2		# gb.compress.bzlib2 module
%bcond_without	zlib		# gb.compress.zlib module
%bcond_without	mysql		# gb.db.mysql module
%bcond_without	odbc		# gb.db.odbc module
%bcond_without	pgsql		# gb.db.postgresql module
%bcond_without	sqlite2		# gb.db.sqlite2 module
%bcond_without	sqlite3		# gb.db.sqlite3 module
%bcond_without	firebird	# gb.db.firebird module
%bcond_without	gtk		# gb.gtk module
%bcond_without	librsvg		# gb.gtk.svg module (depends on gtk)
%bcond_without	pdf		# gb.pdf module
%bcond_without	net		# gb.net module
%bcond_without	curl		# gb.net.curl module
%bcond_without	smtp		# gb.net.smtp module
%bcond_without	pcre		# gb.pcre module
%bcond_without	qt		# gb.qt module
%bcond_with	qte		# gb.qte module
%bcond_without	kde		# gb.qt.kde module
%bcond_without	sdl		# gb.sdl module
%bcond_without	sdlsound	# gb.sdl.sound module
%bcond_without	xml		# gb.xml module
%bcond_without	v4l		# gb.v4l module
%bcond_without	crypt		# gb.crypt module
%bcond_without	opengl		# gb.opengl module
%bcond_without	corba		# gb.corba module
%bcond_without	image		# gb.image module
#bcond_without	desktop		# gb.desktop module
#
%if %{without gtk}
%undefine	with_librsvg
%endif
%if %{without opengl}
%undefine	with_sdl
%endif
%if %{without sdl}
%undefine	with_SDL_mixer
%endif
Summary:	Gambas - a free VB-like language
Summary(pl.UTF-8):	Gambas - wolnodostępny język podobny do VB
Name:		gambas2
Version:	2.8.2
Release:	0.1
License:	GPL v2
Group:		Development/Languages
Source0:	http://downloads.sourceforge.net/gambas/%{name}-%{version}.tar.bz2
# Source0-md5:	9f0d1c450b22580eccf3a0e3619a9d7c
Source1:	%{name}.desktop
Patch0:		%{name}-avoid-version.patch
URL:		http://gambas.sourceforge.net/
%{?with_firebird:BuildRequires:	Firebird-devel}
%{?with_opengl:BuildRequires:	OpenGL-GLU-devel}
%{?with_opengl:BuildRequires:	OpenGL-GLX-devel}
%{?with_sdl:BuildRequires:	SDL-devel >= 1.2.8}
%{?with_sdl:BuildRequires:	SDL_image-devel}
%{?with_SDL_mixer:BuildRequires:	SDL_mixer-devel}
%{?with_bzip2:BuildRequires:	bzip2-devel}
%{?with_curl:BuildRequires:	curl-devel >= 7.13}
BuildRequires:	gettext-tools
%{?with_gtk:BuildRequires:	gtk+2-devel >= 2:2.10.0}
%{?with_smtp:BuildRequires:	glib2-devel >= 2.0}
%{?with_kde:BuildRequires:	kdelibs-devel >= 3}
%{?with_v4l:BuildRequires:	libjpeg-devel}
%{?with_v4l:BuildRequires:	libpng-devel}
%{?with_librsvg:BuildRequires:	librsvg-devel >= 1:2.14.3}
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_corba:BuildRequires:	omniORB-devel >= 4}
%{?with_pcre:BuildRequires:	pcre-devel}
BuildRequires:	pkgconfig
%{?with_pdf:BuildRequires:	poppler-devel >= 0.8.0}
%{?with_pgsql:BuildRequires:	postgresql-backend-devel}
%{?with_pgsql:BuildRequires:	postgresql-devel}
%{?with_qt:BuildRequires:	qt-devel >= 3}
%{?with_qte:BuildRequires:	qte-devel >= 3}
%{?with_sqlite2:BuildRequires:	sqlite-devel >= 2}
%{?with_sqlite3:BuildRequires:	sqlite3-devel >= 3}
%{?with_xml:BuildRequires:	libxml2-devel >= 2.0}
%{?with_xls:BuildRequires:	libxslt-devel}
%{?with_sdl:BuildRequires:	xorg-lib-libXcursor-devel}
%{?with_sdl:BuildRequires:	xorg-lib-libXft-devel}
%{?with_desktop:BuildRequires:	xorg-lib-libXtst-devel}
%{?with_zlib:BuildRequires:	zlib-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gambas is a free development environment based on a Basic interpreter
with object extensions, like Visual Basic(tm). With Gambas, you can
quickly design your program GUI, access MySQL or PostgreSQL databases,
pilot KDE applications with DCOP, translate your program into many
languages, and so on...

This package provides the command-line utilities, as well as the
Gambas interpreter needed to run Gambas applications.

%description -l pl.UTF-8
Gambas to wolnodostępne środowisko programistyczne oparte na
interpreterze Basica z rozszerzeniami obiektowymi, podobnym do Visual
Basica(TM). Przy pomocy Gambasa można szybko projektować graficzne
interfejsy użytkownika, odwoływać się do baz danych MySQL i
PostgreSQL, sterować aplikacjami KDE poprzez DCOP, tłumaczyć
program na wiele języków itd.

Ten pakiet dostarcza narzędzia działające z linii poleceń, a
także interpreter potrzebny do uruchamiania aplikacji Gambas.

%package doc
Summary:	Documentation for Gambas language
Summary(pl.UTF-8):	Dokumentacja dla języka Gambas
Group:		Development/Languages

%description doc
Gambas is a free development environment based on a Basic interpreter
with object extensions, like Visual Basic(tm). With Gambas, you can
quickly design your program GUI, access MySQL or PostgreSQL databases,
pilot KDE applications with DCOP, translate your program into many
languages, and so on...

This package contains Gambas language documentation.

%description doc -l pl.UTF-8
Gambas to wolnodostępne środowisko programistyczne oparte na
interpreterze Basica z rozszerzeniami obiektowymi, podobnym do Visual
Basica(TM). Przy pomocy Gambasa można szybko projektować graficzne
interfejsy użytkownika, odwoływać się do baz danych MySQL i
PostgreSQL, sterować aplikacjami KDE poprzez DCOP, tłumaczyć
program na wiele języków itd.

Ten pakiet zawiera dokumentację dla języka Gambas.

%package ide
Summary:	The Gambas IDE
Summary(pl.UTF-8):	IDE dla Gambas
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-gb-db = %{version}-%{release}
Requires:	%{name}-gb-debug = %{version}-%{release}
Requires:	%{name}-gb-qt = %{version}-%{release}
Requires:	%{name}-gb-qt-editor = %{version}-%{release}
Requires:	%{name}-gb-qt-ext = %{version}-%{release}

%description ide
This package includes the complete Gambas Development Environment,
with the database manager and all necessary components.

%description ide -l pl.UTF-8
Ten pakiet zawiera kompletne środowisko programistyczne, łącznie z
menedżerem baz danych i wszystkimi niezbędnymi komponentami.

%package examples
Summary:	The examples for Gambas language
Summary(pl.UTF-8):	Przykłady dla języka Gambas
Group:		Development/Languages
Requires:	%{name}-ide = %{version}-%{release}

%description examples
The gambas-examples package contains some examples for Gambas.

%description examples -l pl.UTF-8
Ten pakiet zawiera kilka przykładów dla Gambas.

%if 0
%package gb-compress
Summary:	The Gambas compression component
Summary(pl.UTF-8):	Gambas - komponent do kompresji
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description gb-compress
This component allows you to compress/uncompress data or files with
the bzip2 and zip algorithms.

%description gb-compress -l pl.UTF-8
Ten komponent pozwala pakować/rozpakowywać dane lub pliki przy
użyciu algorytmów bzip2 i zip.

%package gb-db
Summary:	The Gambas database component
Summary(pl.UTF-8):	Gambas - komponent bazodanowy
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description gb-db
This component allows you to access many databases management systems,
provided that you install the needed driver packages.

%description gb-db -l pl.UTF-8
Ten komponent pozwala na dostęp do wielu systemów bazodanowych pod
warunkiem doinstalowania wymaganych pakietów sterowników.

%package gb-db-mysql
Summary:	The MySQL driver for the Gambas database component
Summary(pl.UTF-8):	Gambas - sterownik do MySQL dla komponentu bazodanowego
Group:		Development/Languages
Requires:	%{name}-gb-db = %{version}-%{release}

%description gb-db-mysql
This component allows you to access MySQL databases.

%description gb-db-mysql -l pl.UTF-8
Ten komponent pozwala na dostęp do bazy danych MySQL.

%package gb-db-postgresql
Summary:	The PostgreSQL driver for the Gambas database component
Summary(pl.UTF-8):	Gambas - sterownik do PostgreSQL dla komponentu bazodanowego
Group:		Development/Languages
Requires:	%{name}-gb-db = %{version}-%{release}

%description gb-db-postgresql
This component allows you to access PostgreSQL databases.

%description gb-db-postgresql -l pl.UTF-8
Ten komponent pozwala na dostęp do bazy danych PostgreSQL.

%package gb-db-sqlite
Summary:	The SQLite driver for the Gambas database component
Summary(pl.UTF-8):	Gambas - sterownik do SQLite dla komponentu bazodanowego
Group:		Development/Languages
Requires:	%{name}-gb-db = %{version}-%{release}

%description gb-db-sqlite
This component allows you to access SQLite databases.

%description gb-db-sqlite -l pl.UTF-8
Ten komponent pozwala na dostęp do bazy danych SQLite.

%package gb-debug
Summary:	The debugger helper component for the Gambas IDE
Summary(pl.UTF-8):	Gambas - komponent debuggera dla IDE
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description gb-debug
This component helps the IDE to debug Gambas programs.

%description gb-debug -l pl.UTF-8
Komponent przeznaczony dla IDE Gambasa, przydatny przy odpluskwianiu
programów.

%package gb-eval
Summary:	The Gambas expression evaluator component
Summary(pl.UTF-8):	Gambas - komponent do obliczania wyrażeń
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description gb-eval
This component allows you to evaluate expressions at runtime. It is
used by the Gambas Eval() function.

%description gb-eval -l pl.UTF-8
Ten komponent pozwala na obliczanie wyrażeń w programach. Jest
używany przez funkcję Gambasa Eval().

%package gb-net
Summary:	The Gambas networking component
Summary(pl.UTF-8):	Komponent sieciowy Gambasa
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description gb-net
This component allows you to use TCP/IP and UDP sockets, and to access
any serial ports.

%description gb-net -l pl.UTF-8
Ten komponent pozwala na używanie gniazd TCP/IP i UDP oraz na dostęp
do portów szeregowych.

%package gb-net-curl
Summary:	The Gambas advanced networking component
Summary(pl.UTF-8):	Zaawansowany komponent sieciowy Gambasa
Group:		Development/Languages
Requires:	%{name}-gb-net = %{version}-%{release}

%description gb-net-curl
This component allows your programs to easily become FTP or HTTP
clients.

%description gb-net-curl -l pl.UTF-8
Ten komponent pozwala programom w łatwy sposób stać się klientami
FTP lub HTTP.

%package gb-qt
Summary:	The Gambas Qt GUI component
Summary(pl.UTF-8):	Komponent graficznego interfejsu użytkownika Qt dla Gambasa
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description gb-qt
This package includes the Gambas Qt GUI component.

%description gb-qt -l pl.UTF-8
Ten pakiet zawiera komponent graficznego interfejsu użytkownika Qt
dla Gambasa.

%package gb-qt-ext
Summary:	The Gambas extended Qt GUI component
Summary(pl.UTF-8):	Komponent rozszerzonego graficznego interfejsu Qt dla Gambasa
Group:		Development/Languages
Requires:	%{name}-gb-qt = %{version}-%{release}

%description gb-qt-ext
This component includes some uncommon Qt controls.

%description gb-qt-ext -l pl.UTF-8
Ten komponent zawiera niektóre mało popularne kontrolki Qt.

%package gb-qt-editor
Summary:	The Gambas source code editor component
Summary(pl.UTF-8):	Komponent edytora kodu źródłowego Gambasa
Group:		Development/Languages
Requires:	%{name}-gb-qt = %{version}-%{release}

%description gb-qt-editor
This component includes a Gambas source code editor with syntax
highlighting. It is used by the IDE.

%description gb-qt-editor -l pl.UTF-8
Ten komponent zawiera edytor kodu źródłowego Gambasa z
podświetlaniem składni. Jest używany przez IDE.

%package gb-qt-kde
Summary:	The Gambas KDE component
Summary(pl.UTF-8):	Komponent KDE dla Gambasa
Group:		Development/Languages
Requires:	%{name}-gb-qt = %{version}-%{release}

%description gb-qt-kde
This component transforms your Qt application in a KDE application,
and allows you to pilot any other KDE application with the DCOP
protocol.

%description gb-qt-kde -l pl.UTF-8
Ten komponent zamienia aplikację Qt w aplikację KDE i pozwala na
sterowanie dowolnymi aplikacjami KDE poprzez protokół DCOP.

%package gb-qt-kde-html
Summary:	The Gambas KHTML component
Summary(pl.UTF-8):	Komponent KHTML dla Gambasa
Group:		Development/Languages
Requires:	%{name}-gb-qt-kde = %{version}-%{release}

%description gb-qt-kde-html
This component allows you to use the KHTML Web Browser widget included
in KDE.

%description gb-qt-kde-html -l pl.UTF-8
Ten komponent pozwala na używanie widgetu przeglądarki WWW KHTML
zawartego w KDE.

%package gb-sdl
Summary:	The Gambas SDL component
Summary(pl.UTF-8):	Komponent SDL dla Gambasa
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description gb-sdl
This component uses only the sound part of the SDL library. It allows
you to simultaneously play many sounds and a music stored in a file.

%description gb-sdl -l pl.UTF-8
Ten komponent używa tylko części dźwiękowej biblioteki SDL.
Pozwala na jednoczesne odtwarzanie wielu dźwięków i muzyki
zapisanej w pliku.

%package gb-vb
Summary:	The Gambas Visual Basic(TM) compatibility component
Summary(pl.UTF-8):	Komponent zgodności z Visual Basicem(TM) dla Gambasa
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description gb-vb
This component aims at including some functions that imitate the
behaviour of Visual Basic(TM) functions. Use it only if you try to
port some VB projects.

%description gb-vb -l pl.UTF-8
Ten komponent zawiera trochę funkcji, których celem jest imitowanie
zachowania funkcji Visual Basica(TM). Należy go używać wyłącznie
przy próbach sportowania projektów VB.

%package gb-xml
Summary:	The Gambas XML components based on the libxml and libxslt libraries
Summary(pl.UTF-8):	Komponenty XML Gambasa oparte na bibliotekach libxml i libxslt
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description gb-xml
These components brings the power of the libxml and libxslt libraries
to Gambas.

%description gb-xml -l pl.UTF-8
Te komponenty pozwalają na korzystanie z potęgi bibliotek libxml i
libxslt z poziomu Gambasa.
%endif

%prep
%setup -q
%patch -P0 -p1

%build
./reconf-all
%configure \
	--enable-bzlib2=%{?with_bzip2:yes}%{!?with_bzip2:no} \
	--enable-zlib=%{?with_zlib:yes}%{!?with_zlib:no} \
	--enable-mysql=%{?with_mysql:yes}%{!?with_mysql:no} \
	--enable-odbc=%{?with_odbc:yes}%{!?with_odbc:no} \
	--enable-postgresql=%{?with_pgsql:yes}%{!?with_pgsql:no} \
	--enable-sqlite2=%{?with_sqlite2:yes}%{!?with_sqlite2:no} \
	--enable-sqlite3=%{?with_sqlite3:yes}%{!?with_sqlite3:no} \
	--enable-firebird=%{?with_firebird:yes}%{!?with_firebird:no} \
	--enable-gtk=%{?with_gtk:yes}%{!?with_gtk:no} \
	--enable-gtksvg=%{?with_librsvg:yes}%{!?with_librsvg:no} \
	--enable-pdf=%{?with_pdf:yes}%{!?with_pdf:no} \
	--enable-net=%{?with_net:yes}%{!?with_net:no} \
	--enable-curl=%{?with_curl:yes}%{!?with_curl:no} \
	--enable-smtp=%{?with_smtp:yes}%{!?with_smtp:no} \
	--enable-pcre=%{?with_pcre:yes}%{!?with_pcre:no} \
	--enable-qt=%{?with_qt:yes}%{!?with_qt:no} \
	--enable-qte=%{?with_qte:yes}%{!?with_qte:no} \
	--enable-kde=%{?with_kde:yes}%{!?with_kde:no} \
	--enable-sdl=%{?with_sdl:yes}%{!?with_sdl:no} \
	--enable-sdlsound=%{?with_SDL_mixer:yes}%{!?with_SDL_mixer:no} \
	--enable-xml=%{?with_xml:yes}%{!?with_xml:no} \
	--enable-v4l=%{?with_v4l:yes}%{!?with_v4l:no} \
	--enable-crypt=%{?with_crypt:yes}%{!?with_crypt:no} \
	--enable-opengl=%{?with_opengl:yes}%{!?with_opengl:no} \
	--enable-corba=%{?with_corba:yes}%{!?with_corba:no} \
	--enable-image=%{?with_image:yes}%{!?with_image:no} \

#	--enable-desktop=%{?with_desktop:yes}%{!?with_desktop:no} \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install -D app/src/gambas2/img/logo/new-logo.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/gbc2
%attr(755,root,root) %{_bindir}/gbi2
%attr(755,root,root) %{_bindir}/gbr2
%attr(755,root,root) %{_bindir}/gbs2
%attr(755,root,root) %{_bindir}/gbs2.gambas
%attr(755,root,root) %{_bindir}/gbx2
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/info
%{_datadir}/%{name}/info/gb.info
%{_datadir}/%{name}/info/gb.list
%attr(755,root,root) %{_libdir}/%{name}/gb.so
%attr(755,root,root) %{_libdir}/%{name}/gb.compress.so
%attr(755,root,root) %{_libdir}/%{name}/gb.compress.bzlib2.so
%attr(755,root,root) %{_libdir}/%{name}/gb.compress.zlib.so
%attr(755,root,root) %{_libdir}/%{name}/gb.corba.so
%attr(755,root,root) %{_libdir}/%{name}/gb.crypt.so
%attr(755,root,root) %{_libdir}/%{name}/gb.db.so
%attr(755,root,root) %{_libdir}/%{name}/gb.db.firebird.so
%attr(755,root,root) %{_libdir}/%{name}/gb.db.mysql.so
%attr(755,root,root) %{_libdir}/%{name}/gb.db.odbc.so
%attr(755,root,root) %{_libdir}/%{name}/gb.db.postgresql.so
%attr(755,root,root) %{_libdir}/%{name}/gb.db.sqlite2.so
%attr(755,root,root) %{_libdir}/%{name}/gb.db.sqlite3.so
%attr(755,root,root) %{_libdir}/%{name}/gb.debug.so
%attr(755,root,root) %{_libdir}/%{name}/gb.desktop.so
%attr(755,root,root) %{_libdir}/%{name}/gb.draw.so
%attr(755,root,root) %{_libdir}/%{name}/gb.eval.so
%attr(755,root,root) %{_libdir}/%{name}/gb.gtk.so
%attr(755,root,root) %{_libdir}/%{name}/gb.gtk.ext.so
#%%attr(755,root,root) %{_libdir}/%{name}/gb.gtk.svg.so
%attr(755,root,root) %{_libdir}/%{name}/gb.gui.so
%attr(755,root,root) %{_libdir}/%{name}/gb.image.so
%attr(755,root,root) %{_libdir}/%{name}/gb.net.so
%attr(755,root,root) %{_libdir}/%{name}/gb.net.curl.so
%attr(755,root,root) %{_libdir}/%{name}/gb.net.smtp.so
%attr(755,root,root) %{_libdir}/%{name}/gb.opengl.so
%attr(755,root,root) %{_libdir}/%{name}/gb.option.so
%attr(755,root,root) %{_libdir}/%{name}/gb.pcre.so
%attr(755,root,root) %{_libdir}/%{name}/gb.pdf.so
%attr(755,root,root) %{_libdir}/%{name}/gb.qt.so
%attr(755,root,root) %{_libdir}/%{name}/gb.qt.ext.so
%attr(755,root,root) %{_libdir}/%{name}/gb.qt.kde.html.so
%attr(755,root,root) %{_libdir}/%{name}/gb.qt.kde.so
%attr(755,root,root) %{_libdir}/%{name}/gb.qt.opengl.so
%attr(755,root,root) %{_libdir}/%{name}/gb.sdl.so
%attr(755,root,root) %{_libdir}/%{name}/gb.sdl.sound.so
%attr(755,root,root) %{_libdir}/%{name}/gb.v4l.so
%attr(755,root,root) %{_libdir}/%{name}/gb.vb.so
%attr(755,root,root) %{_libdir}/%{name}/gb.xml.so
%attr(755,root,root) %{_libdir}/%{name}/gb.xml.xslt.so

%{_libdir}/%{name}/gb.component
%{_libdir}/%{name}/gb.chart.component
%{_libdir}/%{name}/gb.chart.gambas
%{_libdir}/%{name}/gb.compress.component
%{_libdir}/%{name}/gb.corba.component
%{_libdir}/%{name}/gb.crypt.component
%{_libdir}/%{name}/gb.db.component
%{_libdir}/%{name}/gb.db.form.component
%{_libdir}/%{name}/gb.db.form.gambas
%{_libdir}/%{name}/gb.debug.component
%{_libdir}/%{name}/gb.desktop.component
%{_libdir}/%{name}/gb.desktop.gambas
%{_libdir}/%{name}/gb.eval.component
%{_libdir}/%{name}/gb.form.component
%{_libdir}/%{name}/gb.form.gambas
%{_libdir}/%{name}/gb.form.dialog.component
%{_libdir}/%{name}/gb.form.dialog.gambas
%{_libdir}/%{name}/gb.form.mdi.component
%{_libdir}/%{name}/gb.form.mdi.gambas
%{_libdir}/%{name}/gb.gtk.component
%{_libdir}/%{name}/gb.gtk.ext.component
%{_libdir}/%{name}/gb.gtk.gambas
#%%{_libdir}/%{name}/gb.gtk.svg.component
%{_libdir}/%{name}/gb.gui.component
%{_libdir}/%{name}/gb.image.component
%{_libdir}/%{name}/gb.info.component
%{_libdir}/%{name}/gb.info.gambas
%{_libdir}/%{name}/gb.net.component
%{_libdir}/%{name}/gb.net.curl.component
%{_libdir}/%{name}/gb.net.smtp.component
%{_libdir}/%{name}/gb.opengl.component
%{_libdir}/%{name}/gb.option.component
%{_libdir}/%{name}/gb.pcre.component
%{_libdir}/%{name}/gb.pdf.component
%{_libdir}/%{name}/gb.qt.component
%{_libdir}/%{name}/gb.qt.gambas
%{_libdir}/%{name}/gb.qt.ext.component
%{_libdir}/%{name}/gb.qt.kde.component
%{_libdir}/%{name}/gb.qt.kde.html.component
%{_libdir}/%{name}/gb.qt.opengl.component
%{_libdir}/%{name}/gb.report.component
%{_libdir}/%{name}/gb.report.gambas
%{_libdir}/%{name}/gb.sdl.component
%{_libdir}/%{name}/gb.sdl.sound.component
%{_libdir}/%{name}/gb.settings.component
%{_libdir}/%{name}/gb.settings.gambas
%{_libdir}/%{name}/gb.v4l.component
%{_libdir}/%{name}/gb.vb.component
%{_libdir}/%{name}/gb.web.component
%{_libdir}/%{name}/gb.web.gambas
%{_libdir}/%{name}/gb.xml.component
%{_libdir}/%{name}/gb.xml.rpc.component
%{_libdir}/%{name}/gb.xml.rpc.gambas
%{_libdir}/%{name}/gb.xml.xslt.component
%{_datadir}/%{name}/info/gb.chart.info
%{_datadir}/%{name}/info/gb.chart.list
%{_datadir}/%{name}/info/gb.compress.info
%{_datadir}/%{name}/info/gb.compress.list
%{_datadir}/%{name}/info/gb.corba.info
%{_datadir}/%{name}/info/gb.corba.list
%{_datadir}/%{name}/info/gb.crypt.info
%{_datadir}/%{name}/info/gb.crypt.list
%{_datadir}/%{name}/info/gb.db.form.info
%{_datadir}/%{name}/info/gb.db.form.list
%{_datadir}/%{name}/info/gb.db.info
%{_datadir}/%{name}/info/gb.db.list
%{_datadir}/%{name}/info/gb.debug.info
%{_datadir}/%{name}/info/gb.debug.list
%{_datadir}/%{name}/info/gb.desktop.info
%{_datadir}/%{name}/info/gb.desktop.list
%{_datadir}/%{name}/info/gb.eval.info
%{_datadir}/%{name}/info/gb.eval.list
%{_datadir}/%{name}/info/gb.form.dialog.info
%{_datadir}/%{name}/info/gb.form.dialog.list
%{_datadir}/%{name}/info/gb.form.info
%{_datadir}/%{name}/info/gb.form.list
%{_datadir}/%{name}/info/gb.form.mdi.info
%{_datadir}/%{name}/info/gb.form.mdi.list
%{_datadir}/%{name}/info/gb.gtk.ext.info
%{_datadir}/%{name}/info/gb.gtk.ext.list
%{_datadir}/%{name}/info/gb.gtk.info
%{_datadir}/%{name}/info/gb.gtk.list
#%%{_datadir}/%{name}/info/gb.gtk.svg.info
#%%{_datadir}/%{name}/info/gb.gtk.svg.list
%{_datadir}/%{name}/info/gb.gui.info
%{_datadir}/%{name}/info/gb.gui.list
%{_datadir}/%{name}/info/gb.image.info
%{_datadir}/%{name}/info/gb.image.list
%{_datadir}/%{name}/info/gb.info.info
%{_datadir}/%{name}/info/gb.info.list
%{_datadir}/%{name}/info/gb.net.curl.info
%{_datadir}/%{name}/info/gb.net.curl.list
%{_datadir}/%{name}/info/gb.net.info
%{_datadir}/%{name}/info/gb.net.list
%{_datadir}/%{name}/info/gb.net.smtp.info
%{_datadir}/%{name}/info/gb.net.smtp.list
%{_datadir}/%{name}/info/gb.opengl.info
%{_datadir}/%{name}/info/gb.opengl.list
%{_datadir}/%{name}/info/gb.option.info
%{_datadir}/%{name}/info/gb.option.list
%{_datadir}/%{name}/info/gb.pcre.info
%{_datadir}/%{name}/info/gb.pcre.list
%{_datadir}/%{name}/info/gb.pdf.info
%{_datadir}/%{name}/info/gb.pdf.list
%{_datadir}/%{name}/info/gb.qt.ext.info
%{_datadir}/%{name}/info/gb.qt.ext.list
%{_datadir}/%{name}/info/gb.qt.info
%{_datadir}/%{name}/info/gb.qt.kde.html.info
%{_datadir}/%{name}/info/gb.qt.kde.html.list
%{_datadir}/%{name}/info/gb.qt.kde.info
%{_datadir}/%{name}/info/gb.qt.kde.list
%{_datadir}/%{name}/info/gb.qt.list
%{_datadir}/%{name}/info/gb.qt.opengl.info
%{_datadir}/%{name}/info/gb.qt.opengl.list
%{_datadir}/%{name}/info/gb.report.info
%{_datadir}/%{name}/info/gb.report.list
%{_datadir}/%{name}/info/gb.sdl.info
%{_datadir}/%{name}/info/gb.sdl.list
%{_datadir}/%{name}/info/gb.sdl.sound.info
%{_datadir}/%{name}/info/gb.sdl.sound.list
%{_datadir}/%{name}/info/gb.settings.info
%{_datadir}/%{name}/info/gb.settings.list
%{_datadir}/%{name}/info/gb.v4l.info
%{_datadir}/%{name}/info/gb.v4l.list
%{_datadir}/%{name}/info/gb.vb.info
%{_datadir}/%{name}/info/gb.vb.list
%{_datadir}/%{name}/info/gb.web.info
%{_datadir}/%{name}/info/gb.web.list
%{_datadir}/%{name}/info/gb.xml.info
%{_datadir}/%{name}/info/gb.xml.list
%{_datadir}/%{name}/info/gb.xml.rpc.info
%{_datadir}/%{name}/info/gb.xml.rpc.list
%{_datadir}/%{name}/info/gb.xml.xslt.info
%{_datadir}/%{name}/info/gb.xml.xslt.list

%files doc
%defattr(644,root,root,755)
%{_datadir}/%{name}/help

%files ide
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gambas2
%attr(755,root,root) %{_bindir}/gambas2.gambas
%attr(755,root,root) %{_bindir}/gambas2-database-manager.gambas
%attr(755,root,root) %{_bindir}/gba2
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png

%files examples
%defattr(644,root,root,755)
%{_datadir}/%{name}/examples

%if 0
%files gb-compress
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.compress.*
%{_datadir}/%{name}/info/gb.compress.*

%files gb-db
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.db.so*
%{_libdir}/%{name}/lib.gb.db.component
%{_datadir}/%{name}/info/gb.db.info
%{_datadir}/%{name}/info/gb.db.list

%files gb-db-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.db.mysql.*

%files gb-db-postgresql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.db.postgresql.*

%files gb-db-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.db.sqlite.*

%files gb-debug
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.debug.*
%{_datadir}/%{name}/info/gb.debug.*

%files gb-eval
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.eval.*
%{_datadir}/%{name}/info/gb.eval.*

%files gb-net
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.net.so*
%{_libdir}/%{name}/lib.gb.net.component
%{_datadir}/%{name}/info/gb.net.info
%{_datadir}/%{name}/info/gb.net.list

%files gb-net-curl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.net.curl.so*
%{_libdir}/%{name}/lib.gb.net.curl.component
%{_datadir}/%{name}/info/gb.net.curl.info
%{_datadir}/%{name}/info/gb.net.curl.list

%files gb-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.qt.so*
%{_libdir}/%{name}/lib.gb.qt.component
%{_datadir}/%{name}/info/gb.qt.info
%{_datadir}/%{name}/info/gb.qt.list

%files gb-qt-ext
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.qt.ext.so*
%{_libdir}/%{name}/lib.gb.qt.ext.component
%{_datadir}/%{name}/info/gb.qt.ext.info
%{_datadir}/%{name}/info/gb.qt.ext.list

%files gb-qt-editor
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.qt.editor.so*
%{_libdir}/%{name}/lib.gb.qt.editor.component
%{_datadir}/%{name}/info/gb.qt.editor.info
%{_datadir}/%{name}/info/gb.qt.editor.list

%files gb-qt-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.qt.kde.so*
%{_libdir}/%{name}/lib.gb.qt.kde.component
%{_datadir}/%{name}/info/gb.qt.kde.info
%{_datadir}/%{name}/info/gb.qt.kde.list

%files gb-qt-kde-html
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.qt.kde.html.so*
%{_libdir}/%{name}/lib.gb.qt.kde.html.component
%{_datadir}/%{name}/info/gb.qt.kde.html.info
%{_datadir}/%{name}/info/gb.qt.kde.html.list

%files gb-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.sdl.so*
%{_libdir}/%{name}/lib.gb.sdl.component
%{_datadir}/%{name}/info/gb.sdl.info
%{_datadir}/%{name}/info/gb.sdl.list

%files gb-vb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.vb.so*
%{_libdir}/%{name}/lib.gb.vb.component
%{_datadir}/%{name}/info/gb.vb.info
%{_datadir}/%{name}/info/gb.vb.list

%files gb-xml
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.xml.libxml.*
%{_datadir}/%{name}/info/gb.xml.libxml.*
%endif
