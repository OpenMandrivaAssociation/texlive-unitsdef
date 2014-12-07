# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/unitsdef
# catalog-date 2007-01-20 15:20:16 +0100
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-unitsdef
Version:	0.2
Release:	9
Summary:	Typesetting units in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/unitsdef
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unitsdef.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unitsdef.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unitsdef.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
There are a lot of packages for typesetting units in LaTeX2e.
Some define macros to typeset a lot of units but do not suit to
the actual font settings, some make the characters needed
available but do not predefine any unit. This package tries to
comply with both requirements. It predefines common units,
defines an easy to use interface to define new units and
changes the output concerning to the surrounding font settings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/unitsdef/ampabbrv.cfg
%{_texmfdistdir}/tex/latex/unitsdef/enerabbr.cfg
%{_texmfdistdir}/tex/latex/unitsdef/freqabbr.cfg
%{_texmfdistdir}/tex/latex/unitsdef/lengabbr.cfg
%{_texmfdistdir}/tex/latex/unitsdef/molabbrv.cfg
%{_texmfdistdir}/tex/latex/unitsdef/timeabbr.cfg
%{_texmfdistdir}/tex/latex/unitsdef/unitsdef.sty
%{_texmfdistdir}/tex/latex/unitsdef/volabbrv.cfg
%{_texmfdistdir}/tex/latex/unitsdef/voltabbr.cfg
%{_texmfdistdir}/tex/latex/unitsdef/weigabbr.cfg
%doc %{_texmfdistdir}/doc/latex/unitsdef/README.1st
%doc %{_texmfdistdir}/doc/latex/unitsdef/defedpraef.tex
%doc %{_texmfdistdir}/doc/latex/unitsdef/defedunits.tex
%doc %{_texmfdistdir}/doc/latex/unitsdef/unitsdef.pdf
#- source
%doc %{_texmfdistdir}/source/latex/unitsdef/unitsdef.dtx
%doc %{_texmfdistdir}/source/latex/unitsdef/unitsdef.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 757289
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 719852
- texlive-unitsdef
- texlive-unitsdef
- texlive-unitsdef

