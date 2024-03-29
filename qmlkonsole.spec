%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20200826
#define commit 681221de51a234567ad832fc52441a4bd267741c

Name:		qmlkonsole
Version:	23.08.4
Release:	%{?git:0.%{git}.}2
Summary:	Terminal application for Plasma Mobile
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma-mobile/qmlkonsole/-/archive/master/qmlkonsole-master.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5KirigamiAddons)
Requires:	qml(QMLTermWidget)

%description
Terminal application for Plasma Mobile

%prep
%if 0%{?git}
%autosetup -p1 -n qmlkonsole-master
%else
%autosetup -p1
%endif
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang qmlkonsole

%files -f qmlkonsole.lang
%{_bindir}/qmlkonsole
%{_datadir}/applications/org.kde.qmlkonsole.desktop
%{_datadir}/config.kcfg/terminalsettings.kcfg
%{_datadir}/metainfo/org.kde.qmlkonsole.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/org.kde.qmlkonsole.svg
