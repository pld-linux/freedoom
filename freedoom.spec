Summary:	FreeDoom - free WAD file for DOOM games
Summary(pl):	FreeDoom - wolnodostêpny plik WAD dla gier DOOM
Name:		freedoom
Version:	2
Release:	2
License:	?
Group:		Applications/Games
Source0:	http://freedoom.sourceforge.net/deutex/wads/doom2.wad.gz
# Source0-md5:	32610843ccad90028257595c3ca1a8a5
URL:		http://freedoom.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreeDoom - free DOOM II-compatible WAD file for DOOM games.

%description -l pl
FreeDoom - wolnodostêpny plik WAD kompatybilny z DOOM II dla gier
DOOM.

%package -n doomlegacy-data-freedoom
Summary:	FreeDoom data for doomlegacy
Summary(pl):	Dane FreeDoom dla gry doomlegacy
Group:		Applications/Games
Requires:	%{name} = %{version}
Requires:	doomlegacy-common

%description -n doomlegacy-data-freedoom
FreeDoom data for doomlegacy.

%description -n doomlegacy-data-freedoom -l pl
Dane FreeDoom dla gry doomlegacy.

%package -n prboom-data-freedoom
Summary:	FreeDoom data for prboom
Summary(pl):	Dane FreeDoom dla gry prboom
Group:		Applications/Games
Requires:	%{name} = %{version}
Requires:	prboom

%description -n prboom-data-freedoom
FreeDoom data for prboom.

%description -n prboom-data-freedoom -l pl
Dane FreeDoom dla gry prboom.

%package -n doomsday-data-freedoom
Summary:	FreeDoom data for doomsday
Summary(pl):	Dane FreeDoom dla gry doomsday
Group:		Applications/Games
Requires:	%{name} = %{version}
Requires:	doomsday

%description -n doomsday-data-freedoom
FreeDoom data for doomsday.

%description -n doomsday-data-freedoom -l pl
Dane FreeDoom dla gry doomsday.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/{games/{freedoom,doom},doomlegacy,deng/Data/jDoom}

gzip -dc %{SOURCE0} > $RPM_BUILD_ROOT%{_datadir}/games/freedoom/doom2.wad
ln -sf %{_datadir}/games/freedoom/doom2.wad $RPM_BUILD_ROOT%{_datadir}/doomlegacy
ln -sf %{_datadir}/games/freedoom/doom2.wad $RPM_BUILD_ROOT%{_datadir}/games/doom
ln -sf %{_datadir}/games/freedoom/doom2.wad $RPM_BUILD_ROOT%{_datadir}/deng/Data/jDoom/Doom2.wad

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/freedoom

%files -n doomlegacy-data-freedoom
%defattr(644,root,root,755)
%{_datadir}/doomlegacy/doom2.wad

%files -n prboom-data-freedoom
%defattr(644,root,root,755)
%{_datadir}/games/doom/doom2.wad

%files -n doomsday-data-freedoom
%defattr(644,root,root,755)
%{_datadir}/deng/Data/jDoom/Doom2.wad
