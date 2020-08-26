%define snapshot 20200826
%define commit 681221de51a234567ad832fc52441a4bd267741c

Name:		qmlkonsole
Version:	0.0
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Terminal application for Plasma Mobile
Source0:	https://invent.kde.org/plasma-mobile/qmlkonsole/-/archive/master/qmlkonsole-master.tar.bz2
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

%description
Terminal application for Plasma Mobile

%prep
%autosetup -p1 -n qmlkonsole-master
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/qmlkonsole
%{_datadir}/applications/org.kde.mobile.qmlkonsole.desktop
%{_datadir}/config.kcfg/terminalsettings.kcfg
%{_datadir}/metainfo/org.kde.mobile.qmlkonsole.appdata.xml
