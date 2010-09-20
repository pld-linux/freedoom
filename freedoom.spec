%define		_rc	rc1
Summary:	FreeDoom - free WAD file for DOOM games
Summary(pl.UTF-8):	FreeDoom - wolnodostępny plik WAD dla gier DOOM
Name:		freedoom
Version:	0.7
Release:	0.%{_rc}.1
Epoch:		1
License:	BSD
Group:		Applications/Games
Source0:	http://mirror.lihnidos.org/GNU/savannah/freedoom/freedoom-iwad/%{name}-iwad-%{version}-%{_rc}.zip
# Source0-md5:	57ecc553a14ef6d79e2fb9c1f7df9b25
URL:		http://freedoom.sourceforge.net/
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreeDoom - free DOOM II-compatible WAD file for DOOM games.

%description -l pl.UTF-8
FreeDoom - wolnodostępny plik WAD kompatybilny z DOOM II dla gier
DOOM.

%package -n doomlegacy-data-freedoom
Summary:	FreeDoom data for doomlegacy
Summary(pl.UTF-8):	Dane FreeDoom dla gry doomlegacy
Group:		Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	doomlegacy-common

%description -n doomlegacy-data-freedoom
FreeDoom data for doomlegacy.

%description -n doomlegacy-data-freedoom -l pl.UTF-8
Dane FreeDoom dla gry doomlegacy.

%package -n doomsday-data-freedoom
Summary:	FreeDoom data for doomsday
Summary(pl.UTF-8):	Dane FreeDoom dla gry doomsday
Group:		Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	doomsday

%description -n doomsday-data-freedoom
FreeDoom data for doomsday.

%description -n doomsday-data-freedoom -l pl.UTF-8
Dane FreeDoom dla gry doomsday.

%package -n prboom-data-freedoom
Summary:	FreeDoom data for prboom
Summary(pl.UTF-8):	Dane FreeDoom dla gry prboom
Group:		Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	prboom

%description -n prboom-data-freedoom
FreeDoom data for prboom.

%description -n prboom-data-freedoom -l pl.UTF-8
Dane FreeDoom dla gry prboom.

%prep
%setup -q -n %{name}-iwad-%{version}-%{_rc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/{games/{freedoom,doom},doomlegacy,deng/Data/jDoom}

install doom2.wad $RPM_BUILD_ROOT%{_datadir}/games/freedoom
ln -sf %{_datadir}/games/freedoom/doom2.wad $RPM_BUILD_ROOT%{_datadir}/doomlegacy
ln -sf %{_datadir}/games/freedoom/doom2.wad $RPM_BUILD_ROOT%{_datadir}/games/doom
ln -sf %{_datadir}/games/freedoom/doom2.wad $RPM_BUILD_ROOT%{_datadir}/deng/Data/jDoom/Doom2.wad

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING CREDITS ChangeLog NEWS README
%{_datadir}/games/freedoom

%files -n doomlegacy-data-freedoom
%defattr(644,root,root,755)
%{_datadir}/doomlegacy/doom2.wad

%files -n doomsday-data-freedoom
%defattr(644,root,root,755)
%{_datadir}/deng/Data/jDoom/Doom2.wad

%files -n prboom-data-freedoom
%defattr(644,root,root,755)
%{_datadir}/games/doom/doom2.wad
