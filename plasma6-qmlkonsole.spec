%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20200826
#define commit 681221de61a234667ad832fc62441a4bd267741c

Name:		plasma6-qmlkonsole
Version:	24.01.90
Release:	%{?git:0.%{git}.}2
Summary:	Terminal application for Plasma Mobile
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma-mobile/qmlkonsole/-/archive/master/qmlkonsole-master.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/qmlkonsole-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6KirigamiAddons)
Requires:	qml(QMLTermWidget)

%description
Terminal application for Plasma Mobile

%prep
%if 0%{?git}
%autosetup -p1 -n qmlkonsole-master
%else
%autosetup -p1 -n qmlkonsole-%{?git:master}%{!?git:%{version}}
%endif
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja -G Ninja

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
